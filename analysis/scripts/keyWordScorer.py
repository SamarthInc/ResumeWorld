import spacy

def getGrams(text):
    monograms = []
    bigram = []
    trigram = []
    split_text = text.split(" ")
    for i in range(len(split_text)):
        if i <= (len(split_text) - 3):
            fw = split_text[i]
            sw = split_text[i+1]
            tw = split_text[i+2]
            monograms.append(fw)
            bigram.append(fw + " " + sw)
            trigram.append(fw + " " + sw + " " + tw)
        elif i <= (len(split_text) - 2):
            fw = split_text[i]
            sw = split_text[i+1]
            monograms.append(fw)
            bigram.append(fw + " " + sw)
        elif i == (len(split_text)-1):
            fw = split_text[i]
            monograms.append(fw)
    op = {"monogram":monograms,"bigram":bigram,"trigram":trigram}
    return op

import json
import os
def check_skill_present(getGrams_op):
    skills_file_path = os.getcwd()+"/analysis/files/skills.json"
    f = open(skills_file_path)
    data = json.load(f)
    monogram_list = data['technical']["one"] + data['soft']["one"]
    bigrams_list = data['technical']["two"] + data['soft']["two"]
    trigrams_list = data['technical']["three"] + data['soft']["three"]
    extragrams_list = data['technical']["extra"] + data['soft']["extra"]
    
    monogram_data = getGrams_op['monogram']
    bigram_data = getGrams_op['bigram']
    trigram_data = getGrams_op['trigram']
    
    m_list = list(set(monogram_list)&set(monogram_data))
    b_list = list(set(bigrams_list)&set(bigram_data))
    t_list = list(set(trigrams_list)&set(trigram_data))
    
    return m_list+b_list+t_list
    


import re
def extractSkills(text):    
    text_lower = text.lower()
    modified_text = " ".join(re.split("[^A-Za-z0-9]+", text_lower))
    skill_list = []
    getGrams_op = getGrams(modified_text)
    check_skill_present_op = check_skill_present(getGrams_op)
    skill_list = check_skill_present_op
    return skill_list

def extractSkillsScorePercentage(res,jd):
    skill_present = []
    skill_absent = []
    for i in range(len(jd)):
        if jd[i] in res:
            skill_present.append(jd[i])
        else:
            skill_absent.append(jd[i])
    score = len(skill_present)/len(jd)
    score = score*100
    return (score, skill_present, skill_absent)