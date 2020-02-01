from position import Position_2D
from directions import Direction, Orientation, cardinal_vectors

class Vehicle:
	# Orientation: up, down, left, right (each is a unit vector n s e w)
	def __init__(self, _head: Position_2D, _len: int, _orient: Orientation,
		_target=False) -> None:
		self.head = _head
		self.len = _len
		self.orient = _orient
		self.target = _target

	def move(self, _dir: Direction) -> None:
		"""This method is how AI performs an action."""
		self.head += cardinal_vectors[self.orient] * _dir