import logging

from .main import *  # noqa


DEBUG = False  # noqa

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
