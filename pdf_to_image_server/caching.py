from typing import Optional
from pdf_to_image_server.config import cfg
from pdf_to_image_server.log_init import logger

def build_cache_name(file_name: str):
    return cfg.cache_folder/(file_name + ".txt")


def read_file(file_name: str) -> Optional[str]:
    file = build_cache_name(file_name)
    logger.info("Reading file: %s", file)
    if not file.exists():
        return None
    with open(file, 'r') as f:
        return f.read()
    

def write_file(content: str, file_name: str):
    file = build_cache_name(file_name)
    logger.info("Writing file to: %s", file)
    with open(file, 'w') as f:
        f.write(content)
