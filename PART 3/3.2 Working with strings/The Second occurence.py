# Ask the user for the main string and the substring to find
main_string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

# Find the first occurrence of the substring.
# .find() returns the starting index, or -1 if not found.
first_occurrence_index = main_string.find(substring)

# We will only search for a second occurrence if a first one was found.
if first_occurrence_index == -1:
    # If the first occurrence was not found, there cannot be a second one.
    print("The substring does not occur twice in the string.")
else:
    # To find a non-overlapping occurrence, we must start our search 
    # *after* the first one ends. The starting point for the next
    # search is the index of the first occurrence plus the length
    # of the substring itself.
    search_start_point = first_occurrence_index + len(substring)
    
    # Now, find the next occurrence, but this time starting from our new point.
    second_occurrence_index = main_string.find(substring, search_start_point)

    if second_occurrence_index == -1:
        # If the second search returns -1, it means we found one, but not two.
        print("The substring does not occur twice in the string.")
    else:
        # If the second search found an index, we have our answer.
        print(f"The second occurrence of the substring is at index {second_occurrence_index}.")