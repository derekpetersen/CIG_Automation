from enum import Enum


class Timeout(Enum):
    def small(self):
        return 1.0

    SMALL = 1
    MEDIUM = 3
    LARGE = 5
    X_LARGE = 10
