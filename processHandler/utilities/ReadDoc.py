
from django.core.files import File
from docx import Document

def readDoc(file: File) -> str:
    extracted_text = ""
    doc_path = file
    doc = Document(doc_path)
    for para in doc.paragraphs:
        extracted_text += para.text + "\n"
    return extracted_text