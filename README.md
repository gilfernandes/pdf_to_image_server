# PDF to Image Server

A simple server which converts PDFs to Text via OCR.

```PDF -> Image -> OCR -> Text```

# Installation

```
conda create -n pdf_to_image_server python=3.11
conda activate pdf_to_image_server

conda install -c conda-forge poppler
pip install pdf2image opencv-python
conda install -c conda-forge pytesseract
pip install python-dotenv
pip install fastapi python-multipart
pip install --force-reinstall C:\development\playground\langchain\hr_image_ranker\pdf_image_ocr-1.0-py3-none-any.whl
pip install uvicorn
pip install -e .

```