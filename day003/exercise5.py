# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name=(name1+name2).lower()
count1=0
count1+=name.count('t')
count1+=name.count('r')
count1+=name.count('u')
count1+=name.count('e')

count2=0
count2+=name.count('l')
count2+=name.count('o')
count2+=name.count('v')
count2+=name.count('e')

total=int(str(count1)+str(count2))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")