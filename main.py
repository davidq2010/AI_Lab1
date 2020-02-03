from board_state import BoardStateManager
from node import Node

if __name__ == "__main__":
    board = BoardStateManager()
    #board.print_grid()
    test_actions = board.compute_valid_actions(board.initial_vehicles)
    #print("=======================================================")
    #board.print_grid()
    print("Num Test Actions:", len(test_actions))
    #for test_action in test_actions: 
        #print(test_action)

    node = Node(board.vehicle_list_2, None, None)
    print("\nSuccessors:")
    node.generate_successors(test_actions)

    