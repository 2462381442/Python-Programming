def chessboard(length):
    """
    Prints a chessboard pattern of 1s and 0s.

    Args:
        length (int): The width and height of the board.
    """
    # Iterate through each row of the board
    for row in range(length):
        # Iterate through each column of the board
        for col in range(length):
            # Check if the sum of row and column indices is even or odd
            # If (row + col) is even, print '1'
            if (row + col) % 2 == 0:
                print("1", end="")
            # If (row + col) is odd, print '0'
            else:
                print("0", end="")
        # After printing all characters in a row, print a newline to move to the next row
        print()