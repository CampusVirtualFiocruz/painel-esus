from logging.handlers import RotatingFileHandler

from .config import formatter, levels, logger

# MAX_SIZE = 10 * 1024 * 1024
MAX_SIZE = 10*1024
FILE_NAME = "painel-esus.log"
BACKUP_COUNT = 5

file_handler = RotatingFileHandler(
    FILE_NAME, 
    maxBytes=MAX_SIZE, 
    backupCount=BACKUP_COUNT,
)

file_handler.setLevel(levels)


file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
