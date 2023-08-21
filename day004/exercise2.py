# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_len = len(names) - 1
n = random.randint(0, name_len)
print(f"{names[n]} is going to buy the meal today!")