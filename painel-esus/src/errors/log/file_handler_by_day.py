from logging.handlers import TimedRotatingFileHandler

from .config import LEVELS, formatter, logger

# WHEN Value	Type of interval
# 'S'	Seconds
# 'M'	Minutes
# 'H'	Hours
# 'D'	Days
# 'W'	Week day (0=Monday)
# 'midnight'	Roll over at midnight

WHEN = "midnight"
FILE_NAME = 'painel-esus.log'
BACKUP_COUNT = 5

file_handler = TimedRotatingFileHandler(
    FILE_NAME,
    when=WHEN,
    backupCount=BACKUP_COUNT,
)

file_handler.setLevel(LEVELS)


file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
