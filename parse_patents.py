import fitz  # PyMuPDF
from PIL import Image
import pytesseract
from io import BytesIO
import os
import pymupdf4llm
import tempfile
from docling.document_converter import DocumentConverter

pdf_directory = "/Users/mehakjain/Desktop/patent-project/pdfs" 

def pdf_to_text_ocr(pdf_path):
    doc = fitz.open(pdf_path)
    all_page_text = []
    for page_num in range(doc.page_count):
        page = doc[page_num]
        pix = page.get_pixmap()
        img_data = pix.tobytes("png")
        img = Image.open(BytesIO(img_data)).convert("L") 
        text = pytesseract.image_to_string(img)
        all_page_text.append(f"--- Page {page_num + 1} ---\n{text}\n")
        img.close()
    doc.close()
    return "\n".join(all_page_text)

def clean_text_with_pymupdf4llm(ocr_text):
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".txt") as temp_file:
            temp_file.write(ocr_text)
            temp_file_path = temp_file.name
        cleaned_text = pymupdf4llm.to_markdown(temp_file_path)
        os.unlink(temp_file_path)
        return cleaned_text if cleaned_text.strip() else "⚠️ No text extracted."
    except Exception as e:
        return f"⚠️ PyMuPDF4LLM Error: {e}"

def parse_with_docling_converter(pdf_path):
    try:
        converter = DocumentConverter()
        result = converter.convert(pdf_path)
        return result.document.export_to_markdown()
    except Exception as e:
        return f"⚠️ Docling Converter Error: {e}"

for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, filename)
        file_name_no_ext = os.path.splitext(filename)[0]

        ocr_text = pdf_to_text_ocr(pdf_path)
        with open(f"{file_name_no_ext}_ocr.txt", "w", encoding="utf-8") as f:
            f.write(ocr_text)

        cleaned_text = clean_text_with_pymupdf4llm(ocr_text)
        with open(f"{file_name_no_ext}_pymupdf4llm.txt", "w", encoding="utf-8") as f:
            f.write(cleaned_text)
            
        docling_text = parse_with_docling_converter(pdf_path)
        with open(f"{file_name_no_ext}_docling.txt", "w", encoding="utf-8") as f:
            f.write(docling_text)

        print(f"✅ Processed: {filename}")

print("✅ All PDFs processed!")