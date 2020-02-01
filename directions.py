from position import Position_2D

from enum import IntEnum, auto, unique

@unique
class Direction(IntEnum):
	FORWARD = 1
	BACKWARD = -1

@unique
class Orientation(IntEnum):
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

cardinal_vectors = [Position_2D(1, 0),  # North
					Position_2D(0, 1),  # East
					Position_2D(-1, 0), # South
					Position_2D(0, -1)] # West