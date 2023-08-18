print("Welcome to Python Pizza Deliveries!")

# Get user input for pizza size, pepperoni, and extra cheese
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Initialize the base price according to pizza size
price = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Wrong size")  # Notify user about incorrect input
    exit()  # Exit the program if the input is incorrect

# Add pepperoni cost based on size
if add_pepperoni == "Y":
    if size != "S":  # Pepperoni costs $3 for sizes M and L, $2 for size S
        price += 3
    else:
        price += 2

# Add extra cheese cost
if extra_cheese == "Y":
    price += 1

# Display the final bill
print(f"Your final bill is: ${price}.")
