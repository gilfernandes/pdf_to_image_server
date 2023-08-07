
import os
from pathlib import Path


import pytesseract
from dotenv import load_dotenv

from pdf_to_image_server.log_init import logger

load_dotenv()

from pdf_image_ocr.config import cfg

logger.info("Pytesseract command: %s", pytesseract.pytesseract.tesseract_cmd)


def create_if_not_exists(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)


class Config:
    temp_file_path = Path(os.getenv('TEMP_FILE_PATH'))
    create_if_not_exists(temp_file_path)
    # Define max HTTP data size to 100 MB
    max_upload_MB = os.getenv('MAX_UPLOAD_MB')
    max_message_size = max_upload_MB * 1024 * 1024
    fast_api_port = int(os.getenv('FAST_API_PORT'))
    remote_server = os.getenv('REMOTE_SERVER')
    # For testing purposes
    doc_location = Path(os.getenv('DOC_LOCATION'))
    create_if_not_exists(doc_location)
    cache_folder = Path(os.getenv('CACHE_FOLDER'))
    create_if_not_exists(cache_folder)

    

cfg = Config()
    
if __name__ == "__main__":
    logger.info(os.getenv('DOC_LOCATION'))
    logger.info(cfg.fast_api_port)
