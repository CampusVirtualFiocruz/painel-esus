from .config import formatter, levels, logger, logging

console_handler = logging.StreamHandler()
# console_handler.setLevel(levels)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
