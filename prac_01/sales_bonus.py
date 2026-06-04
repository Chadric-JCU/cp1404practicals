"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        percent_bonus = 10

    else:
        percent_bonus = 15

    bonus = sales * (percent_bonus /100)
    print(f"Your bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
print("Exiting program.")

