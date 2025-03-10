from rich.logging import RichHandler

from .config import formatter, levels, logger, logging

logger.addHandler(RichHandler())
