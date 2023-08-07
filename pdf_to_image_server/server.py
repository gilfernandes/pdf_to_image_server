from pathlib import Path
import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile

from pdf_to_image_server.config import cfg

from pdf_image_ocr.image_ocr import convert_img_to_text

from log_init import logger

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        logger.info("Upload received")
        tmp_path = cfg.temp_file_path
        file_path: Path = tmp_path/file.filename
        with open(file_path, 'wb') as f:
            f.write(contents)
            extracted_text = convert_img_to_text(file_path)
            return {
                "message": f"Successfully uploaded {file.filename}",
                "extracted_text": extracted_text
            }
    except Exception:
        logger.exception("An error occurred during file uplodate")
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        if file_path and file_path.exists:
            try:
                os.remove(file_path)
            except Exception:
                logger.exception("Could not delete file.")


if __name__ == '__main__':
    logger.info("Fast API server starting on port: %s", cfg.fast_api_port)    
    uvicorn.run(app, host="0.0.0.0", port=cfg.fast_api_port)