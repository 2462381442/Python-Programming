# Write your solution here
mystring = input("Editor: ")

while True:
 
 if mystring.lower() == "visual studio code":
    print("an excellent choice!")
    break
 elif mystring.lower() == "word":
    print("awful")
 elif mystring.lower() == "notepad":
    print("awful")
 else:
    print("not good")
 mystring = input("Editor: ")