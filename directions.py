from position import Position_2D

from enum import IntEnum, unique

@unique
class Direction(IntEnum):
	FORWARD = 1
	BACKWARD = -1

class Orientation:
        HORIZONTAL = 0
        VERTICAL = 1

orientation_positions = [Position_2D(0, -1), Position_2D(1, 0)]
