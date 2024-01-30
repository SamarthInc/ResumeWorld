import os
from pypdf import PdfReader
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile


import pdfplumber
def readPdf(file: File) -> str:
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
            text += "\n"  # Add a line break after each page

    return text