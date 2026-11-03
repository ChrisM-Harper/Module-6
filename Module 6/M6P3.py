# Christopher Monarrez M6P3

# Variables
principle_amount = float(input("Enter Principle Amount: "))
years_to_mature = int(input("Enter Years to Maturity of CD: "))


# Calculations
if principle_amount > 100000 and years_to_mature == 5:
    interest_rate = .06
elif 50000 <= principle_amount <= 100000 and years_to_mature == 10:
    interest_rate = .05
elif 50000 <= principle_amount <= 100000 and years_to_mature == 5:
    interest_rate = .04
else:
    interest_rate = .02

# First year interest
first_year_interest = principle_amount * interest_rate



# Display 
print("Principle: ", principle_amount)
print("Interest: ", interest_rate)
print("First Year Interest Amount: ", first_year_interest)