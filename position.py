class Position_2D:
	def __init__(self, _y: int, _x: int) -> None:
		self.x = _x
		self.y = _y

	def get_tuple(self):
		return (y, x)

	def __iadd__(self, _other):
		self.x += _other.x
		self.y += _other.y
		return self

	def __add__(self, _other):
		return Position_2D(self.y + _other.y, self.x + _other.x)

	def __imul__(self, _other):
		if isinstance(_other, (int, float)):
			self.x *= _other
			self.y *= _other
		else: # Could maybe implement for matrix multiplication
			raise TypeError("Operator not defined for Type {}".format(type(_other)))

	def __mul__(self, _other):
		if isinstance(_other, (int, float)):
			return Position_2D(self.y * _other, self.x * _other)
		else:
			raise TypeError("Operator not defined for Type {}".format(type(_other)))

	def __repr__(self):
		return "({}, {})".format(self.y, self.x)
