from pathlib import Path
import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile

from pdf_to_image_server.config import cfg
from pdf_to_image_server.log_init import logger
from pdf_to_image_server.caching import read_file, write_file

from pdf_image_ocr.image_ocr import convert_img_to_text

import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CODE_OK = 'OK'
CODE_FAIL = 'FAIL'


def message_factory(file_name: str, contents: str, code: str) -> dict:
    return {
        "code": code,
        "message": f"Successfully uploaded {file_name}",
        "extracted_text": contents
    }


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    cached_contents = read_file(file.filename)
    if cached_contents is not None:
        return message_factory(file.filename, cached_contents, CODE_OK)
    try:
        contents = file.file.read()
        logger.info("Upload received")
        tmp_path = cfg.temp_file_path
        file_path: Path = tmp_path/file.filename
        with open(file_path, 'wb') as f:
            f.write(contents)
            extracted_text = convert_img_to_text(file_path)
            write_file(content=extracted_text, file_name=file.filename)
            return message_factory(file.filename, extracted_text, CODE_OK)
    except Exception:
        logger.exception("An error occurred during file uplodate")
        return {'code': CODE_FAIL, "message": "There was an error uploading the file"}
    finally:
        try:
            file.file.close()
            if file_path and file_path.exists:
                    os.remove(file_path)
        except Exception:
            logger.exception("Could not delete file.")


if __name__ == '__main__':
    logger.info("Fast API server starting on port: %s", cfg.fast_api_port)    
    uvicorn.run(app, host="0.0.0.0", port=cfg.fast_api_port)