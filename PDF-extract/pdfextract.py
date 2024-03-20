#!/usr/bin/env python3

import fitz  # PyMuPDF
import sys

def extract_text_from_pdf(pdf_path):
    # Open the provided PDF file
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""

        # Iterate through each page in the PDF
        for page_num in range(len(pdf_document)):
            # Get a page
            page = pdf_document.load_page(page_num)
            
            # Extract text from the page
            text += page.get_text()

        # Close the PDF after extraction
        pdf_document.close()
        
        return text
    except Exception as e:
        print(f"[X] Error: {e}")

# Specify the path to your PDF file
if len(sys.argv) != 2:
    print("[X] Usage: pdfextract.py /file/document.pdf")
    sys.exit(1)
pdf_path = sys.argv[1]
extracted_text = extract_text_from_pdf(pdf_path)

# Print to stdout
print(extracted_text)

