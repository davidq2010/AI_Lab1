from vehicle import Vehicle
from board_state import BoardStateManager
from position import Position_2D
from directions import Direction, Orientation, orientation_positions

from pqdict import minpq
from copy import deepcopy

class Node:
    class_id = 0

    def __init__(self, _vehicles, _prev_action, _parent):
        self.vehicles = _vehicles
        self.prev_action = _prev_action
        self.parent = _parent
        self.id = Node.class_id
        Node.class_id += 1

        self.g = 0
        self.f = 0

    def __hash__(self):
        return hash(self.state_representation())

    def __eq__(self, _other):
        return self.state_representation() == _other.state_representation()

    def __lt__(self, _other):
        return self.__hash__() < _other.__hash__()

    def state_representation(self):
        return tuple(vehicle.state_representation() for vehicle in self.vehicles)

    def generate_successors(self, _actions):
        successors = []
        for action in _actions:
            vehicle_idx = action["vehicle_idx"]
            new_head = action["new_head"]
            successor = Node(deepcopy(self.vehicles), action, self)
            successor.vehicles[vehicle_idx].head = new_head
            successors.append(successor)
        #for successor in successors:
        #    print(successor)
        return successors

    def __repr__(self):
        #return "Parent: {},\nPrevAction: {},\nVehicles: {}".format(self.parent.id if self.parent else None,
        #    self.prev_action, self.vehicles)
        return str(self.state_representation())


def AStarWithPQ(_board: BoardStateManager):
    start = Node(_board.initial_vehicles, None, None)

    visited = set()

    pq = minpq()

    # Initialize pqdict with start node
    # Assign it score of 0 (which is what start.f is initialized to)
    pq.additem(start, (0, start))

    while pq:
        curr_node, score_tup = pq.popitem()
        score = score_tup[0]

        vehicles = curr_node.vehicles

        if goal_state_reached(vehicles[0], _board):
            return compute_path(curr_node)

        # So we never visit this node again
        visited.add(curr_node)

        valid_actions = _board.compute_valid_actions(vehicles)

        successor_nodes = curr_node.generate_successors(valid_actions)

        for successor in successor_nodes:
            # No need to re-process visited nodes
            if successor in visited:
                continue

            successor.g = curr_node.g + 1
            h = 0
            #h = compute_heuristic(successor.vehicles, _board)
            successor.f = successor.g + h

            # Update scores as needed
            # successor is a temporary Node state, not the same as
            # the one in the pq
            if successor in pq:
                if successor.f < pq[successor][0]:
                    pq[successor][1].f = successor.f
                    pq[successor][1].g = successor.g
                    pq.updateitem(successor, (successor.f, pq[successor][1]))
            else:
                pq.additem(successor, (successor.f, successor))
    return None



def AStar(_board: BoardStateManager):
    start = Node(_board.initial_vehicles, None, None)

    frontier = [start]
    visited = set()

    while frontier:
        idx = compute_best_node(frontier)
        curr_node = frontier.pop(idx)
        vehicles = curr_node.vehicles

        # Remember, vehicle[0] is the target
        if goal_state_reached(vehicles[0], _board):
            return compute_path(curr_node)

        visited.add(curr_node)

        # Actions dicts have vehicle idx, forward/backward direction of movement,
        # and new head Position
        valid_actions = _board.compute_valid_actions(vehicles)

        # For each action, construct a new Node object and deep copy the vehicles
        # list when passing the param. Then, change the vehicle at vehicle_idx to
        # have the new head Position
        successor_nodes = curr_node.generate_successors(valid_actions)
        # For each successor, update score if lower and add to frontier (if not in there)
        for successor in successor_nodes:
            if successor in visited:
                continue

        # If successor is in frontier, compare its current score to potential score
            # from this path
            # Successor's potential updated values
            h = 0
            successor.g = curr_node.g + 1
            h = compute_heuristic(successor.vehicles, _board)
            successor.f = successor.g + h

            #inFrontier = False
            for state in frontier: #is this valid if frontier is a PQ
                #update the f value if nodes are same and new f value is smaller
                if successor == state:
                    if successor.f < state.f:
                        state.f = successor.f
                        state.g = successor.g
                    break
            else:
                frontier.append(successor)
    return None


#finds the node in the frontier with the lowest f value
def compute_best_node(_frontier):
    current = _frontier[0]
    curr_index = 0
    for i, node in enumerate(_frontier):
        if node.f < current.f:

            current = node
            curr_index = i

    return curr_index

def goal_state_reached(red_car, _board):
    if red_car.horizontal:
        if red_car.head.x is _board.goal.x or red_car.head.x + red_car.len - 1 is _board.goal.x:
            return True
    else:
        if red_car.head.y is _board.goal.y or red_car.head.y - red_car.len + 1 is _board.goal.y:
            return True
    return False

#computes path from start to goal
def compute_path(_curr_node):
    path = []
    while _curr_node is not None:
        path.append(_curr_node.prev_action)
        _curr_node = _curr_node.parent
    return path[::-1]

def compute_heuristic(_vehicles, board):
    #initialize grid -- BETTER WAY OF DOING THIS????
    grid = [[False for i in range(board.cols)] for j in range(board.rows)]

    for vehicle in _vehicles:
        vehicle_pos_ptr = Position_2D(vehicle.head.y, vehicle.head.x)
        for i in range(vehicle.len):
            grid[vehicle_pos_ptr.y][vehicle_pos_ptr.x] = True
            if vehicle.horizontal:
                vehicle_pos_ptr += (orientation_positions[Orientation.HORIZONTAL]
                        * Direction.BACKWARD)
            else:
                vehicle_pos_ptr += (orientation_positions[Orientation.VERTICAL]
                        * Direction.BACKWARD)

                #initialize heuristic variables
    dist = 0
    num_blocked_squares = 0
    _goal = board.goal
    red_car = _vehicles[0]

    #get position of red car
    red_car_ptr = Position_2D(red_car.head.y, red_car.head.x)
    #if red car is horizontal...
    if red_car.horizontal:
        #distance from head to goal
        dist_head = abs(_goal.x - red_car_ptr.x)
        #tail position
        tail_ptr = red_car_ptr.x + red_car.len-1
        #distance from tail to goal
        dist_tail = abs(_goal.x - tail_ptr)
        #if tail is closer, set heuristic distance and compute # of blocked squares
        if(dist_head > dist_tail ):
            dist = dist_tail
            start_coord = tail_ptr + 1
            while start_coord <= _goal.x:
                if grid[red_car_ptr.y][start_coord]:
                    num_blocked_squares += 1
                start_coord += 1
        else:
            start_coord = red_car_ptr.x - 1
            while start_coord >= _goal.x:
                if grid[red_car_ptr.y][start_coord]:
                    num_blocked_squares += 1
                start_coord -= 1
    #if red car is vertical
    else:
    #distance from head to goal
        dist_head = abs(_goal.y - red_car_ptr.y)
        #tail position
        tail_ptr = red_car_ptr.y - red_car.len+1
        #distance from tail to goal
        dist_tail = abs(_goal.y - tail_ptr)
        #if tail is closer, set heuristic distance and compute # of blocked squares
        if(dist_head > dist_tail ):
            dist = dist_tail
            start_coord = tail_ptr - 1
            while start_coord >= _goal.y:
                if grid[start_coord][red_car_ptr.x]:
                    num_blocked_squares += 1
                start_coord -= 1
        else:
            dist = dist_head
            start_coord = red_car_ptr.y + 1
            while start_coord <= _goal.y:
                if grid[start_coord][red_car_ptr.x]:
                    num_blocked_squares += 1
                start_coord += 1

        return dist + num_blocked_squares 

