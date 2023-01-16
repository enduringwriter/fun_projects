# Calculate Weekly Paycheck
# Given hourly rate and the number of hours worked in one week
# Overtime pay is time and a half if working more than 40 hours

# set variables
play_game = True
forty = 40.00


# function to calculate weekly paycheck
def get_weekly_paycheck(rate, hours):
    if hours > forty and rate > 0:  # calculate overtime pay
        weekly_base_pay = rate * forty
        weekly_overtime_pay = 1.5 * (hours - forty) * rate
        weekly_paycheck = weekly_base_pay + weekly_overtime_pay
    elif hours > 0 and rate > 0:  # if hours is less than or equal to 40.00, and greater than 0
        weekly_base_pay = rate * hours
        weekly_paycheck = weekly_base_pay
    else:
        weekly_paycheck = 0
    return print(f"Your weekly paycheck is: ${weekly_paycheck:.2f}")


print("Welcome to the Weekly Pay program. \nPress 'q' to quit at anytime.")

while play_game:

    # get user input - hourly rate
    hourly_rate = input("Enter your hourly rate: ").lower()
    if hourly_rate == 'q':
        play_game = False
        break

    # get user input - hours worked
    hours_worked = input("Enter the number of hours you worked: ").lower()
    if hours_worked == 'q':
        play_game = False
        break

    # test conditions for valid input by using try, except, else
    try:
        if float(hourly_rate) < 0:
            print("Invalid entry. Please enter a positive number for hourly rate.")
            break
            # while float(rate) < 0:
            #     rate = float(input("Enter your hourly rate: "))
            # hourly_rate = rate
        else:  # float(hourly_rate) >= 0
            hourly_rate = float(hourly_rate)
        if float(hours_worked) < 0:
            print("Invalid entry. Please enter a positive number for hours worked.")
            break
            # while float(hours) < 0:
            #     hours = float(input("Enter the number of hours your worked: "))
            # hours_worked = hours
        else:  # float(hours_worked) >= 0
            hours_worked = float(hours_worked)

    # prevent crash error when hourly rate or hours worked is a string instead of a number
    except ValueError:
        print("Invalid entry. Please enter a valid number.")

    # execute the calculation, if the try block and except block work correctly
    else:
        get_weekly_paycheck(rate=hourly_rate, hours=hours_worked)

# Still working on a better solution for negative inputs. Current code is to break the loop and end the program.
