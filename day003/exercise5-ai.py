print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = (name1 + name2).lower()

count_true = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')
count_love = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')

total_score = int(str(count_true) + str(count_love))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 < total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
