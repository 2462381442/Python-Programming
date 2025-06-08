sentence = input("Please type in a sentence: ")

# Print the first letter of the very first word
print(sentence[0])

index = 1
while index < len(sentence):
    # If the previous character was a space, this one is the first letter of a new word
    if sentence[index - 1] == ' ':
        print(sentence[index])
    # Move to the next character in every iteration
    index += 1