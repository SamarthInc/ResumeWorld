import os
from pypdf import PdfReader
from django.core.files import File

def readPdf(file: File) -> str:
    """
    Read a single PDF file and extract the text from each page.
    Args:
        file: File
    Returns:
        list: A list containing the extracted text from each page of the PDF file.
    """
    output = []
    try:
        pdf_reader = PdfReader(file)
        count = len(pdf_reader.pages)
        for i in range(count):
            page = pdf_reader.pages[i]
            output.append(page.extract_text())
    except Exception as e:
        print(f"Error reading file '{file.name}': {str(e)}")
    return str("".join(output))