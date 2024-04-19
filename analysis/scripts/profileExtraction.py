
import re

#import Levenshtein
def stringSimilarity(str1, str2):
        #distance = Levenshtein.distance(str1, str2)
        distance = 0
        similarity = 1 - (distance / max(len(str1), len(str2)))
        return similarity
    
def extractContactNumberFromResume(text):
    text = text.replace(" ", "")
    text = text.replace("-", "")
    phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    if len(phone)>0:
        return phone[0]
    else:
        return None

def extractEmailFromResume(text):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    if len(emails)>0:
        return emails[0]
    else:
        return None
    

def extractNameFromResume(text):
    name = None
    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()
    return name

def extractGithubFromResume(text):
    text = text.replace(" ", "")
    pattern = r'https://github\.com/[\w-]+/[\w-]+'
    match = re.search(pattern, text)
    
    if match:
        return match.group(0)
    else:
        return None
    
def extractLinkedinUrlsFromResume(text):
    text = text.replace(" ", "")
    urls = re.findall('linkedin.com/in/(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    text = text.replace("\n", "")
    check_linkedin = re.findall('https://www.linkedin.com/in/(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    
    if len(urls)>0:
        return urls[0]
    elif len(check_linkedin)>0:
        return check_linkedin[0]
    else:
        return None
    


