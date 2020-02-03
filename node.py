from vehicle import Vehicle
from board_state import BoardStateManager

from copy import deepcopy
from Typing import Tuple

class Node:
	def __init__(self, _vehicles: Tuple[Vehicle], _prev_action, _parent):
		self.vehicles = _vehicles
		self.prev_action = _prev_action
		self.parent = _parent

		self.g = 0
		self.h = 0
		self.f = 0

	def state_representation(self):
		return (vehicle.state_representation for vehicle in self.vehicles)

	def generate_successors(self, _actions):
                successors = []
                for action in _actions:
                        vehicle_idx = action["vehicle_idx"]
                        new_head = action["new_head"]
                        successor = Node(deepcopy(self.vehicles), action, self)
                        successor.vehicles[vehicle_idx].head = new_head
                        successors.append(successor)


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
		successor_nodes = curr_node.generate_successor_nodes(valid_actions)

