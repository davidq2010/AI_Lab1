from position import Position_2D
from directions import Direction

class Vehicle:
	# Orientation: up, down, left, right (each is a unit vector n s e w)
	def __init__(self, _head: Position_2D, _len: int, _horizontal: bool):
		self.head = _head
		self.len = _len
		self.horizontal = _horizontal

	def state_representation(self):
		if self.horizontal:
			return self.head.x
		else:
			return self.head.y

	def __repr__(self):
		return "Head: {}, Orientation: {}".format(self.head,
			"horizontal" and self.horizontal or "vertical")
