# Calculate Weekly Paycheck
# Given hourly rate and the number of hours worked in one week
# Overtime pay is time and a half if working more than 40 hours

# set variables
play_game = True  # can use any arbitrary variable, such as: run_program = True
forty = 40.00


# function to calculate weekly paycheck
def get_weekly_paycheck(rate, hours):
    if hours > forty:  # calculate overtime pay
        weekly_base_pay = rate * forty
        weekly_overtime_pay = 1.5 * (hours - forty) * rate
        weekly_paycheck = weekly_base_pay + weekly_overtime_pay
    else:  # if hours is less than or equal to 40.00
        weekly_base_pay = rate * hours
        weekly_paycheck = weekly_base_pay
    return print(f"Your weekly paycheck is: ${weekly_paycheck:.2f}")


print("Welcome to the Weekly Pay program. \nPress 'q' to quit at anytime.")

while play_game:

    # get user input - hourly rate
    hourly_rate = input("Enter your hourly rate: ")
    if hourly_rate == 'q' or hourly_rate == 'Q':
        play_game = False
        break
    else:
        hourly_rate = float(hourly_rate)

    # get user input - hours worked
    hours_worked = input("Enter the number of hours you worked: ").lower()  # alternative option
    if hours_worked == 'q':
        play_game = False
        break
    else:
        hours_worked = float(hours_worked)

    get_weekly_paycheck(rate=hourly_rate, hours=hours_worked)
