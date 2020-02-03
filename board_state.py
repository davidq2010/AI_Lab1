from position import Position_2D
from directions import Direction, Orientation, orientation_positions
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
        self.goal = Position_2D(self.rows-1, self.cols-1)
        self.grid = [[False for i in range(self.cols)] for i in range(self.rows)] #ADDED THIS for print
        # Init Vehicles
        self.initial_vehicles = [Vehicle(Position_2D(3, 5), 2, False), Vehicle(Position_2D(3, 0), 2, False), Vehicle(Position_2D(2, 2), 2, True), Vehicle(Position_2D(1, 0), 2, True) ]
        
    def print_grid(self,grid):
        for row in reversed(grid):
            print(row)

    def compute_valid_actions(self, _vehicles):
        # Iterate over each Vehicle and check immediately forward/backward cells
        # as free/not (in the board member variable and also at edge/not)
        # Action can be defined by Vehicle and move function, so have a dict
        # representation of action:
        # {"vehicle_idx": idx in vehicles list
        #  "new_head": Position2D, 
        #  "action": "forward/backward"}
        self.print_grid(self.grid)
        # Initialize the grid's occupancy
        print(_vehicles[0].len)
        grid = [[False for i in range(self.cols)] for j in range(self.rows)]
        
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
        possible_actions = []
        # Compute valid actions given current vehicles
        for idx, vehicle in enumerate(_vehicles):
            # Assuming no vehicle is longer than the board
            # vertical
            if vehicle.horizontal:
                forward_pos = vehicle.head + orientation_positions[Orientation.HORIZONTAL]
                if forward_pos.x >= 0 and not grid[forward_pos.y][forward_pos.x]:
                    possible_actions.append({"vehicle_idx": idx,
                                             "new_head": forward_pos,
                                             "action": "forward"})
                backward_pos = (vehicle.head + orientation_positions[Orientation.HORIZONTAL]
                                                * Direction.BACKWARD)
                tail_x = backward_pos.x + vehicle.len - 1
                if tail_x < self.cols and \
                    not grid[backward_pos.y][tail_x]:
                        possible_actions.append({"vehicle_idx": idx,
                                                 "new_head": backward_pos,
                                                 "action": "backward"})
            # horizontal
            else:
                forward_pos = vehicle.head + orientation_positions[Orientation.VERTICAL]
                if forward_pos.y < self.rows and not grid[forward_pos.y][forward_pos.x]:
                    possible_actions.append({"vehicle_idx": idx,
                                             "new_head": forward_pos,
                                             "action": "forward"})
                backward_pos = (vehicle.head + orientation_positions[Orientation.VERTICAL]
                                                * Direction.BACKWARD)
                tail_y = backward_pos.y - vehicle.len + 1
                if tail_y >= 0 and \
                    not grid[tail_y][backward_pos.x]:
                        possible_actions.append({"vehicle_idx": idx,
                                                 "new_head": backward_pos,
                                                 "action": "backward"})

        return possible_actions
