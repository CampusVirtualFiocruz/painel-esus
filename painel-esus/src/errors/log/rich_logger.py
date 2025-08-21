from rich.logging import RichHandler

from .config import logger

logger.addHandler(RichHandler())
