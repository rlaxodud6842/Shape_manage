from enum import Enum
class Menu(Enum):
    ADD_SHAPE = 1
    DELETE_SHAPE = 2
    PRINT_SHAPE = 3
    EXIT = 4

class ShapeType(Enum):
    CIRCLE = 1
    TRIANGLE = 2
    RECTANGLE = 3