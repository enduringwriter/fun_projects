# Calculate Weekly Paycheck
# Given hourly rate and the number of hours worked in one week
# Overtime pay is time and a half if working more than 40 hours

# set variables
forty = 40.00

# get user input
hourly_rate = float(input("Enter your hourly rate: "))
hours_worked = float(input("Enter the number of hours you worked: "))

if hours_worked > forty:  # calculate overtime pay
    weekly_base_pay = hourly_rate * forty
    weekly_overtime_pay = 1.5 * (hours_worked - forty) * hourly_rate
    weekly_paycheck = weekly_base_pay + weekly_overtime_pay
else:  # if hours is less than or equal to 40
    weekly_base_pay = hourly_rate * hours_worked
    weekly_paycheck = weekly_base_pay

print(f"Your weekly paycheck is: ${weekly_paycheck}")
