# Christopher Monarrez M6P5

# Variables
employee_last_name = str(input("Enter Employee Last Name: "))
salary = float(input("Enter Salary: "))
job_level = int(input("Enter Job Level: "))



# Calculations
if job_level >= 10:
    bonus_rate = .25
elif 5 <= job_level <= 9:
    bonus_rate = .2
else:
    bonus_rate = .1

# Bonus
bonus = salary * bonus_rate



# Display
print("Employee Last Name: ", employee_last_name)
print("Bonus: ", bonus)