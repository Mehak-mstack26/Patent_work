# Patent Project

## Overview
This project automates the extraction and processing of patent documents using OCR and text extraction techniques. It also integrates with PubChem to fetch chemical data based on compound names.

## Features
- Convert PDF patent documents into readable text using OCR.
- Clean and format extracted text using PyMuPDF4LLM.
- Use Docling DocumentConverter for additional text extraction.
- Fetch molecular properties from PubChem using REST API.

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/Mehak-mstack26/Patent_work.git
cd Patent_work
```

### 2. Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage

### Extract Text from PDFs
Place PDF files in the `pdfs/` directory and run:
```sh
python parse_patents.py
```
This will generate three output text files for each PDF:
- **OCR extracted text** (`*_ocr.txt`)
- **Cleaned text using PyMuPDF4LLM** (`*_pymupdf4llm.txt`)
- **Docling extracted text** (`*_docling.txt`)

### Fetch Chemical Data from PubChem
Use the `pubchem.py` script to get molecular properties of a compound:
```sh
python pubchem.py
```
This script fetches properties like Molecular Weight, SMILES, and InChIKey from PubChem.

## Configuration
If required, update the API endpoint URLs in `pubchem.py` for better integration.

## Dependencies
- `pymupdf` (PDF parsing)
- `pillow` (Image processing)
- `pytesseract` (OCR)
- `pymupdf4llm` (Text cleaning)
- `docling` (Document conversion)
- `requests` (HTTP API calls)

Install dependencies manually if needed:
```sh
pip install pymupdf pillow pytesseract pymupdf4llm docling requests
```

