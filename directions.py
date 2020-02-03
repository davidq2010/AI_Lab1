from position import Position_2D

from enum import IntEnum, auto, unique

@unique
class Direction(IntEnum):
	FORWARD = 1
	BACKWARD = -1

cardinal_vectors = [Position_2D(1, 0),  # North
					Position_2D(0, 1),  # East
					Position_2D(-1, 0), # South
					Position_2D(0, -1)] # West