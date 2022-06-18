import random

print(random.randint(0,9))

mylist = ["Yes","No","Maybe"]
print(random.sample(mylist,k=1))

answer = random.randint(1,3)
if answer == 1:
    print("Yes")
if answer == 2:
    print("No")
if answer == 3:
    print("Maybe")