# Christopher Monarrez M6P2

# Variables
part_number = int(input("Enter Part Number: "))
quantity = int(input("Enter Quantity: "))
cost_per_unit = 0


# Calculations

# if statements for cost per unit
if part_number == 10 or part_number == 50:
    cost_per_unit = 1
elif part_number == 99:
    cost_per_unit = 2
elif part_number == 80 or part_number == 70:
    cost_per_unit = 3
else:
    cost_per_unit = 5


# Total Cost
total_cost = quantity * cost_per_unit


# Display
print("Part Number: ", part_number)
print("Cost Per Unit: ", cost_per_unit)
print("Total Cost: ", total_cost)