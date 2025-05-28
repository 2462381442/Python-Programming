# Ask the user for three letters
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

# Create a list of the letters
letters = [letter1, letter2, letter3]

# Sort the list alphabetically
letters.sort()

# The middle letter will be at index 1 after sorting
middle_letter = letters[1]

# Print the result
print(f"The letter in the middle is {middle_letter}")
