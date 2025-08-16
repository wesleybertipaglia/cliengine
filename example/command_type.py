from enum import Enum, auto

class CommandType(Enum):
    FILE = auto()
    FOLDER = auto()
    ARCHIVE = auto()