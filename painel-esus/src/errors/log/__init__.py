from rich.logging import RichHandler

from .config import formatter, logger
from .console_handler import console_handler

# from .file_handler_by_size import file_handler
from .file_handler_by_day import file_handler
