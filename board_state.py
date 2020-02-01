from position import Position_2D
from directions import Direction, Orientation, cardinal_vectors
from vehicle import Vehicle
"""
For each neighboring state (aka each valid action), put state in PQ.
"""
class BoardStateManager:
	# Method to iterate over every vehicle and determine valid actions
	def __init__(self):
		# Will later need config file input and class to parse config file.
		# Parser should verify that goal cell in front of red car
		self.initialize()

	def initialize(self):
		# For now, hardcode vehicles and grid/board
		# Init board/grid's cells as unoccupied
		rows = 6
		cols = 6
		self.grid = [[False for i in range(cols)] for i in range(rows)]
		# Init Vehicles
		self.vehicles = [Vehicle(Position_2D(3, 0), 2, Orientation.NORTH, False)]
		# Re-init grid's occupied status now that we have vehicles
		for vehicle in self.vehicles:
			vehicle_pos_ptr = Position_2D(vehicle.head.y, vehicle.head.x)
			for i in range(vehicle.len):
				self.grid[vehicle_pos_ptr.y][vehicle_pos_ptr.x] = True
				vehicle_pos_ptr += (cardinal_vectors[vehicle.orient] 
									* Direction.BACKWARD)

		# Init goal cell
		self.goal = Position_2D(rows-1, cols-1)

	def print_grid(self):
		for row in reversed(self.grid):
			print(row)

	def compute_valid_actions(self):
		# Iterate over each Vehicle and check immediately forward/backward cells
		# as free/not (in the board member variable and also at edge/not)
		# Action can be defined by Vehicle and move function, so have a dict
		# representation of action:
		# {"vehicle": Vehicle,
		#  "action": move, # type is function
		#  "params": [param_list]}
		pass
