from .config import levels, logger, logging

formatter = logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler = logging.StreamHandler()
console_handler.setLevel(levels)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
