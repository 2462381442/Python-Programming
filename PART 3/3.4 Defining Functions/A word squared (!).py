def squared(text, size):
    """
    Prints a square of characters by repeating a given text.

    Args:
        text: The string to be repeated.
        size: The width and height of the square.
    """
    # Calculate the total number of characters needed for the square.
    total_length = size * size
    
    # Repeat the input string until it's long enough to fill the square.
    # We add 1 after the division to ensure we have enough characters
    # even if total_length is not a multiple of the text length.
    full_text = (text * (total_length // len(text) + 1))
    
    # Use an index to keep track of our position in the repeated string.
    index = 0
    # Loop 'size' times to print each row of the square.
    for _ in range(size):
        # Get the slice for the current row.
        row_text = full_text[index : index + size]
        # Print the row.
        print(row_text)
        # Move the index to the start of the next row.
        index += size