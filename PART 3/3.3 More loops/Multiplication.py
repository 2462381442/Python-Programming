# Prompt the user for a number
limit_str = input("Please type in a number: ")
limit = int(limit_str)

while True:
        # Check if the number is positive
        if limit <= 0:
            print("Please enter a positive number.")
            continue

        # Initialize the first operand for the outer loop
        i = 1
        # The outer loop iterates through the first operand
        while i <= limit:
            # Initialize the second operand for the inner loop
            j = 1
            # The inner loop iterates through the second operand
            while j <= limit:
                # Calculate the product
                product = i * j
                # Print the result in the specified format
                print(f"{i} x {j} = {product}")
                # Increment the inner loop counter
                j += 1
            # Increment the outer loop counter
            i += 1
        
        # Exit the main loop after successfully generating the table
        break

