# Depending on an employee’s hourly wage, total regular hours, and total overtime hours, we are going to calculate that employee’s total weekly pay:

# Input the hourly wage, total regular hours, and total overtime hours
hourlyWageString = input("What is the employee's hourly wage? $")
totalRegHoursString = input("How many regular hours did they work this week? ")
totalOverHoursString = input("How many overtime hours did they work this week? ")

hourlyWage = float(hourlyWageString)
totalRegHours = int(totalRegHoursString)
totalOverHours = int(totalOverHoursString)

# First, compute the regular pay from the total regular hours using the formula:
# Total regular pay = Hourly wage * total regular hours
totalRegularPay = hourlyWage * totalRegHours

# Second, compute the overtime pay from the total overtime hours using the formula:
# Total overtime pay = Total Overtime hours * (Hourly wage * 1.5)
totalOvertimePay = totalOverHours * (hourlyWage * 1.5)

# Lastly, compute the total weekly pay from the regular pay and the overtime pay using the formula:
# Total weekly pay = Total regular pay + Total overtime pay
totalWeeklyPay = totalRegularPay + totalOvertimePay

# Print the total weekly pay
print("The employee made $" + str(totalWeeklyPay) + " this week.")