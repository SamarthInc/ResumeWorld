from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from resumeworld.settings import BASE_DIR
import os
from django.core.files.uploadedfile import InMemoryUploadedFile

import json

def check_file_type(file_name):
    if file_name.lower().endswith('.pdf'):
        return 'PDF'
    elif file_name.lower().endswith(('.doc', '.docx')):
        return 'Word Document'
    else:
        return 'Unknown'
    
def resumejsonparser(resume_data,resume_name):
        file_path = str(BASE_DIR)+'/files/resume_json.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                json_data = json.load(json_file)
                for i in range(len(json_data['Resume'])):
                    if json_data['Resume'][i]["resume_data"] == resume_data:
                        return "this resume is already exist with resumeId: "+ str(json_data['Resume'][i]["resume_id"])
                resume_id = len(json_data['Resume']) + 1
            new_data = {"resume_id":resume_id, "resume_name":resume_name,"resume_data":resume_data}
            json_data['Resume'].append(new_data)
            with open(file_path, 'w') as json_file:
                json.dump(json_data, json_file, indent=4)
            return "success"
        else:
            print(file_path+"------- not exist")

import re

def extract_contact_number_from_resume(text):
    contact_number = None

    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()

    return contact_number
def extract_email_from_resume(text):
    email = None

    # Use regex pattern to find a potential email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()

    return email    

import spacy
from spacy.matcher import Matcher

def extract_name_from_resume(text):
    name = None

    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()

    return name


def extract_education_from_resume(text):
    education = []

    # List of education keywords to match against
    education_keywords = ['Bsc', 'B. Pharmacy', 'B Pharmacy', 'Msc', 'M. Pharmacy', 'Ph.D', 'Bachelor', 'Master']

    for keyword in education_keywords:
        pattern = r"(?i)\b{}\b".format(re.escape(keyword))
        match = re.search(pattern, text)
        if match:
            education.append(match.group())

    return education

import PyPDF2
from docx import Document
class ResumeJobStoring(APIView):
    def post(self,request):
        resume = request.FILES["resume"]
        extracted_text = ""
        file_type = check_file_type(resume.name)
        if file_type == "PDF":
            print("in pdf")
            if isinstance(resume, InMemoryUploadedFile):
                pdf_reader = PyPDF2.PdfReader(resume)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    extracted_text += page.extract_text()
        elif file_type == "Word Document":
            print("in doc")
            doc_path = resume
            doc = Document(doc_path)
            for para in doc.paragraphs:
                extracted_text += para.text + " "
        else:
            return Response("please enter the file in PDF or WORD format")
        resumejsonparser_output = resumejsonparser(extracted_text,resume.name)
        # print(resumejsonparser_output)
        a=extract_contact_number_from_resume(extracted_text)
        print(a)
        b=extract_email_from_resume(extracted_text)
        print(b)
        c = extract_name_from_resume(extracted_text)
        print(c)
        d = extract_education_from_resume(extracted_text)
        print(d)
        return Response("success")