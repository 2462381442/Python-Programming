# This program asks the user for words to build a story.
# The input stops if the user types "end" or the same word twice in a row.

story_words = []
previous_word = None  # To store the last word entered

# print("Let's build a story! Type 'end' or the same word twice to finish.") # Removed this line

while True:
    # Ask the user for a word
    current_word = input("Please type in a word: ")

    # Condition 1: User types "end"
    if current_word.lower() == "end":
        break  # Exit the loop

    # Condition 2: User types the same word twice in a row
    if current_word == previous_word:
        break  # Exit the loop

    # If neither condition is met, add the word to the story
    story_words.append(current_word)
    # Update the previous word for the next iteration
    previous_word = current_word

# Join all the collected words with a space in between
final_story = " ".join(story_words)

# Print the final story
if final_story:  # Only print if there's something in the story
    print(final_story)
# If the story is empty (e.g., user types 'end' immediately),
# this condition ensures nothing is printed, not even a blank line.

