# Write your solution here
word = input("Please type in a word: ")

if len(word) > 1:
    print(f"There are {len(word)} letters in the word {str(word)}")
    print("Thank you!")

elif len(word) <= 1:
    print("Thank you!") 