import math
import requests
from sentence_transformers import SentenceTransformer,util

def score(input1,input2):
    url = 'https://api.jina.ai/v1/embeddings'
    headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer jina_ae1798c1ab3b401fb9d4ed0356147e33oyfb23u1GNjRyV-t3wY4YQovjwG4'
    }
    data = {
  'input': [input1,input2],
  'model': 'jina-embeddings-v2-base-en'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        data = response.json()
        embedding1=data['data'][0]['embedding']

        embedding2=data['data'][1]['embedding']

        final_score=util.cos_sim(embedding1,embedding2)[0].item()
    else:
      model=SentenceTransformer('sentence-transformers/sentence-t5-large')
      embedding1=model.encode(input1)
      embedding2=model.encode(input2)
      final_score=util.cos_sim(embedding1,embedding2)[0].item()
    return final_score

def scoreToPercentage(score):
   return (math.pi - math.acos(score)) * 100 / math.pi

def scoreV2(input1,input2):
  model=SentenceTransformer('MNG123/msmarco-distilbert-base-tas-b-resume-fit-v2-epoch-3')
  embedding1=model.encode(input1)
  embedding2=model.encode(input2)
  final_score=util.cos_sim(embedding1,embedding2)[0].item()    
  return final_score

