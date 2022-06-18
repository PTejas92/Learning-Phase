import random

lucky_num = random.randint(1,100)
fortune_num = random.randint(1,3)

if fortune_num == 1:
    fortune_text = "You will have a great day!"
if fortune_num == 2:
    fortune_text = "You will have a tough day!"
if fortune_num == 3:
    fortune_text = "You will get married this year!"
print(f"{fortune_text} Your Lucky Number is {lucky_num}")