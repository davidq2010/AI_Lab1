from position import Position_2D
from directions import Direction, Orientation, cardinal_vectors

class Vehicle:
	# Orientation: up, down, left, right (each is a unit vector n s e w)
	def __init__(self, _head: Position_2D, _len: int, _horizontal: bool):
		self.head = _head
		self.len = _len
		self.horizontal = _horizontal

	def state_representation(self):
		if self.horizontal:
			return head.x
		else:
			return head.y

	def move(self, _dir: Direction):
		"""This method is how AI performs an action."""
		self.head += cardinal_vectors[self.orient] * _dir