from board_state import BoardStateManager

if __name__ == "__main__":
    board = BoardStateManager()
    #board.print_grid()
    test_actions = board.compute_valid_actions(board.initial_vehicles)
    #print("=======================================================")
    #board.print_grid()
    print(len(test_actions))
    for x in range(len(test_actions)): 
        print(test_actions[x])

    