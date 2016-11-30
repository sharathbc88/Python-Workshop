"""Add a loop to the sales bonus exercise, so that the program repeatedly asks for the user's sales
and prints the bonus until they enter a negative number. """


MENU = "What is the sales amount ? to display your Bonus"
print (MENU)
sales = float(input("Enter Sales: $"))
if sales >=0:
    if sales >= 0 and sales < 1000:
        bonus = sales * 0.1
        print("Bonus: $",(bonus))
        sales = float(input("Enter Sales: $"))
    elif sales >= 1000:
        bonus = sales * 0.15
        print("Bonus: $",(bonus))
        sales = float(input("Enter Sales: $"))
else:
    exit()