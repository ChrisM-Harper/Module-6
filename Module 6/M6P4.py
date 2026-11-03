# Christopher Monarrez M6P4

# Variables
number_of_tickets = int(input("Enter Number of Concert Tickets: "))



# Calculations
if number_of_tickets >= 25:
    price_per_ticket = 50
elif 10 <= number_of_tickets <= 24:
    price_per_ticket = 60
elif 5 <= number_of_tickets <= 9:
    price_per_ticket = 70
else:
    price_per_ticket = 75

# Total Cost
total_cost = number_of_tickets * price_per_ticket



# Display 
print("Number of Tickets: ", number_of_tickets)
print("Price per Ticket", price_per_ticket)
print("Total Cost: ", total_cost)