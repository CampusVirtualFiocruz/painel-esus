# import logging.config
import json
import logging.config
import os
import pathlib

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_json_path = os.path.join(ROOT_DIR, "logger","config.json")
config_file = pathlib.Path(config_json_path)


with open(config_file, "r", encoding="utf-8") as f_in:
    config = json.load(f_in)
logging.config.dictConfig(config)

logger = logging.getLogger("test")
logger.handlers.clear()
