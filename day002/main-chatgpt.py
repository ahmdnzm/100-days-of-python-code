#main.py refactor by chatgpt
print("Welcome to the Tip Calculator")
total = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
split_bill = int(input("How many people to split the bill?"))
payment = (total * (1 + tip_percentage / 100)) / split_bill
print(f"Each person should pay: ${payment:.2f}")