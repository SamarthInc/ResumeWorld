import pandas as pd 
import re 
import json
from tqdm.autonotebook import tqdm
from sentence_transformers import SentenceTransformer,CrossEncoder,InputExample,losses
from pinecone import Pinecone, PodSpec
from transformers import T5Tokenizer, T5ForConditionalGeneration
import time
from tqdm.auto import tqdm
import torch
from huggingface_hub import notebook_login


def preprocess(text):
    text = re.sub(r"[^a-zA-Z0-9,.'?]+", ' ', str(text))
    text = [text[:len(text)//2],text[len(text)//2:]]
    return text

def split_first(text):
    return len(text.split())

def convert_str(text):
    return str(text)+"_"

def get_text():
    with open('pairs.tsv', 'r', encoding='utf-8') as fp:
        lines = fp.read().split('\n')
    for line in tqdm(lines):
        try:
            query, passage = line.split('\t')
            yield query, passage
        except ValueError:
            pass

def get_lines():
    # loop through each file
    with open('triplets.tsv', 'r', encoding='utf-8') as fp:
        lines = fp.read().split('\n')
    for line in tqdm(lines):
        q, p, n = line.split('\t')
        yield q, p, n

def script(file):
    df = pd.read_csv(file) # file being in csv
    df['new_text']= df.Resume_test.apply(preprocess)
    df = df.explode("new_text")
    df['text']=df['new_text'].astype(str)

    df[[ 'instruction', 'text']].to_json('corpus.json',orient='records')
    df[['instruction', 'text']].to_json('corpus.jsonl',orient='records',lines=True)

    f = open('corpus.json')

    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    with open('corpus.jsonl', 'w') as outfile:
        for entry in data:
            json.dump(entry, outfile)
            outfile.write('\n')

    filepath = 'corpus.jsonl'
    with open(filepath, 'r') as infile, open('output.json', 'w') as outfile:
        data = [json.loads(line) for line in infile]
        json.dump(data, outfile)

    df = pd.read_json('output.json')

    df.to_csv('final_process.csv')

    df = pd.read_csv('final_process.csv')
    target = 100000
    batch_size = 128 
    num_queries = 3  
    count = 0
    lines = []
    passage_batch = []
    passages = df['text'].to_numpy()
    model_name = 'doc2query/msmarco-t5-base-v1'
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    with tqdm(total=target) as progress:
        for passage in passages:
            if count >= target: break
            passage_batch.append(passage.replace('\t', ' ').replace('\n', ' '))
            if len(passage_batch) == batch_size:
                inputs = tokenizer(
                    passage_batch,
                    truncation=True,
                    padding=True,
                    max_length=256,
                    return_tensors='pt'
                )
                input_ids=inputs['input_ids']
                attention_mask=inputs['attention_mask']

                outputs = model.generate(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    max_length=64,
                    do_sample=True,
                    top_p=0.95,
                    num_return_sequences=num_queries
                )

                decoded_output = tokenizer.batch_decode(
                    outputs,
                    skip_special_tokens=True
                )
                for i, query in enumerate(decoded_output):
                    query = query.replace('\t', ' ').replace('\n', ' ')  
                    passage_idx = int(i/num_queries)  
                    lines.append(query+'\t'+passage_batch[passage_idx])
                    count += 1

                passage_batch = []
                progress.update(len(decoded_output))

    with open('pairs.tsv', 'w', encoding='utf-8') as fp:
        fp.write('\n'.join(lines))
    
    model = SentenceTransformer('msmarco-distilbert-base-tas-b')
    model.max_seq_length = 256
    
    API_KEY = "639751b0-d839-467f-af93-1f579dd7a6dc"  

    pc = Pinecone(api_key=API_KEY)
    
    if 'query' not in pc.list_indexes():
        pc.create_index(
            'query',
            dimension=model.get_sentence_embedding_dimension(),
            metric='dotproduct',
            spec=PodSpec(
        environment="gcp-starter"
      )
        )
    index = pc.Index('query')

    pc.describe_index("query")

    pair_gen = get_text()

    pairs = []
    to_upsert = []
    passage_batch = []
    id_batch = []
    batch_size = 64

    for i, (query, passage) in enumerate(pair_gen):
        pairs.append((query, passage))
        if passage not in passage_batch: 
            passage_batch.append(passage)
            id_batch.append(str(i))
        if len(passage_batch) == batch_size:
            embeds = model.encode(passage_batch).tolist()
            index.upsert(vectors=list(zip(id_batch, embeds)))
            passage_batch = []
            id_batch = []

    index.describe_index_stats()

    import random

    batch_size = 100
    triplets = []

    for i in tqdm(range(0, len(pairs), batch_size)):
        i_end = min(i+batch_size, len(pairs))
        queries = [pair[0] for pair in pairs[i:i_end]] 
        pos_passages = [pair[1] for pair in pairs[i:i_end]] 
        query_embs = model.encode(queries, convert_to_tensor=True, show_progress_bar=False) 

        res = dict()
        res['results'] = [index.query(vector=i.tolist(), top_k=10) for i in query_embs]


        for query, pos_passage, query_res in zip(queries, pos_passages, res['results']):
            top_results = query_res['matches']
            random.shuffle(top_results)
            for hit in top_results:
                neg_passage = pairs[int(hit['id'])][1]
                if neg_passage != pos_passage:
                    triplets.append(query+'\t'+pos_passage+'\t'+neg_passage)
                    break

    with open('triplets.tsv', 'w', encoding='utf-8') as fp:
        fp.write('\n'.join(triplets))

    model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

    lines = get_lines()
    label_lines = []

    i=0
    for line in lines:
        i+=1
        q, p, n = line
        p_score = model.predict((q, p))
        n_score = model.predict((q, n))
        margin = p_score - n_score
        label_lines.append(
            q + '\t' + p + '\t' + n + '\t' + str(margin)
        )

    with open("triplets_margin.tsv", 'w', encoding='utf-8') as fp:
        fp.write('\n'.join(label_lines))

    training_data = []

    with open('triplets_margin.tsv', 'r', encoding='utf-8') as fp:
        lines = fp.read().split('\n')
    # loop through each line and return InputExample
    for line in tqdm(lines):
        q, p, n, margin = line.split('\t')
        training_data.append(InputExample(
            texts=[q, p, n],
            label=float(margin)
        ))
    torch.cuda.empty_cache()

    batch_size = 32

    loader = torch.utils.data.DataLoader(
        training_data, batch_size=batch_size, shuffle=True
    )
    model = SentenceTransformer('msmarco-distilbert-base-tas-b')
    model.max_seq_length = 256
    loss = losses.MarginMSELoss(model)
    # decrease the number of epochs if we are not using GPU.
    epochs = 10
    warmup_steps = int(len(loader) * epochs * 0.1)

    model.fit(
    train_objectives=[(loader, loss)],
    epochs=epochs,
    warmup_steps=warmup_steps,
    output_path='msmarco-distilbert-base-tas-b-final',
    show_progress_bar=True
    )
    
    # there is a login for huggingface which is required to save a model into huggingface 
    # there is no requirement of login for using the model but for saving it prompts a login by this command
    
    notebook_login()
    
    # change the organization and train_datasets can be empty the name can be different which is the first string.
    model.save_to_hub(
    "msmarco-distilbert-base-tas-b-resume-fit-v2-epoch-2",
    organization="MNG123",
    train_datasets=["MNG123/first"],
    exist_ok=True,
    )
    # now this model is 
    
                
       
                
    return None
