__all__ = [
    "SQLITE_PATH",
    "JUMPPLUS_URL",
]

from os import environ

SQLITE_PATH = environ["MANGATRACKER_SQLITE_PATH"]
JUMPPLUS_URL = environ["MANGATRACKER_JUMPPLUS_URL"]
