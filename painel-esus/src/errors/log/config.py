import logging

levels = logging.DEBUG

formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


logger = logging.getLogger(__name__)
logger.setLevel(levels)


