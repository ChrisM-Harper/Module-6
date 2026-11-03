# Christopher Monarrez M6P1

# Variables
quantity_of_widgets = int(input("Enter Quantity of Widgets: "))
price = 0


# Calculations

# if statements to determine price from quantity of widgets
if quantity_of_widgets >10000:
    price = 10
elif quantity_of_widgets >=5000:
    price = 20
else:
    price = 30

# Extended Price Calc.
extended_price = quantity_of_widgets * price

# Tax
tax = extended_price * .07

# Total Amount
total_amount = extended_price + tax



# Display
print("Extended Price: ", extended_price)
print("Tax: ", tax)
print("Total: ", total_amount)

