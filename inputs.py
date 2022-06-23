text = input("Enter text: ")
number = int(input("Enter 1 for uppercase and 2 for lowercase: "))

if number ==1:
    print(text.upper())
if number ==2:
    print(text.lower())
else:
    print("Enter proper number")
