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
pip install python-dotenv fastapi python-multipart
pip install --force-reinstall pdf_image_ocr-1.0-py3-none-any.whl
pip install uvicorn
pip install requests
pip install -e .

```

Please note that you need https://github.com/gilfernandes/pdf_ocr installed.

# Environment

You will need an `.env` file with the following variables:

```
# Used as a temporary directory
TEMP_FILE_PATH=C:/tmp/pdf_to_image_server
# Used as a temporary directory for image generation
TEMP_IMG_PATH=C:/tmp/pdf_to_image_server
# Location of the OCR programme used internally
TESSERACT_LOCATION=C:/Program Files/Tesseract-OCR/tesseract.exe
DOC_LOCATION=c:/tmp
MAX_UPLOAD_MB=100

FAST_API_PORT=8000
```

# Running

```
python .\pdf_to_image_server\server.py
```