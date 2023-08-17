#main.py refactor by chatgpt
print("Welcome to the Tip Calculator")
total=input("What was the total bill? $")
tip=input("What percentage tip would you like to give? 10, 12, or 15?")
split_bill=input("How many people to split the bill?")
payment=(float(total)*(1+float(tip)/100))/int(split_bill)
print(f"Each person should pay: ${round(payment,2)}")