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

	# Configuration file:
	# Dimensions of board
	# List of Vehicles (one of them is red)
	# Goal
	def initialize(self):
		# TODO: For now, hardcode vehicles and grid/board
		# Init board/grid's cells as unoccupied
		self.rows = 6
		self.cols = 6
		self.goal = Position_2D(rows-1, cols-1)


		# Init Vehicles
		self.initial_vehicles = [Vehicle(Position_2D(3, 0), 2, Orientation.NORTH, False)]		

		# Init goal cell

	def print_grid(self):
		for row in reversed(self.grid):
			print(row)

	def compute_valid_actions(self, _vehicles):
		# Iterate over each Vehicle and check immediately forward/backward cells
		# as free/not (in the board member variable and also at edge/not)
		# Action can be defined by Vehicle and move function, so have a dict
		# representation of action:
		# {"vehicle_idx": idx in vehicles list
		#  "action": move, # type is function
		#  "params": [param_list]}

		# Initialize the grid's occupancy
		grid = [[False for i in range(self.cols)] for j in range(self.rows)]
		for vehicle in _vehicles:
			vehicle_pos_ptr = Position_2D(vehicle.head.y, vehicle.head.x)
			for i in range(vehicle.len):
				grid[vehicle_pos_ptr.y][vehicle_pos_ptr.x] = True
				vehicle_pos_ptr += (cardinal_vectors[vehicle.orient] 
									* Direction.BACKWARD)

		possible_actions = []
		# Compute valid actions given current vehicles
		for vehicle in self.vehicles:
			# North/South aka vertical
			pass
			# East/West aka horizontal
		
