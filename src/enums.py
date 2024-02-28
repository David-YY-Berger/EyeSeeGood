from enum import Enum, auto


class Options(Enum):
    CREATE_QUESTION_FILES = auto()
    READ_ANSWER_FILES = auto()
    EXIT = auto()


class QuestionOptions(Enum):
    DEFAULT_HEBREW = auto()
    DEFAULT_ENGLISH = auto()
    CUSTOM_USER_ENTERED = auto()