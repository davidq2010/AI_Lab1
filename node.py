from vehicle import Vehicle
from board_state import BoardStateManager

from Typing import Tuple

class Node:
	def __init__(self, _vehicles: Tuple[Vehicle], _prev_action: Action, _parent):
		self.vehicles = _vehicles
		self.prev_action = _prev_action
		self.parent = _parent

		self.g = 0
		self.h = 0
		self.f = 0

	def state_representation(self):
		return (vehicle.state_representation for vehicle in self.vehicles)


def AStar(_board: BoardStateManager):
	start = Node(_board.initial_vehicles, None)

	frontier = [start]
	visited = set()

	while frontier:
		curr_node = compute_best_node(frontier)

		vehicles = curr_node.vehicles

		# Remember, vehicle[0] is the target
		if goal_state_reached(vehicles[0], _board):
			return compute_path(curr_node)

		visited.add(curr_node.state_representation())

                # Actions dicts have vehicle idx, forward/backward direction of movement,
                # and new head Position
		valid_actions = _board.compute_valid_actions(vehicles)

		# For each action, construct a new Node object and deep copy the vehicles
		# list when passing the param. Then, change the vehicle at vehicle_idx to
		# have the new head Position
		successor_nodes = generate_successor_nodes(curr_node, valid_actions)

