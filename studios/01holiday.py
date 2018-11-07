# WALKTHROUGH ----------------------------------------------------------------
# We will create a tip calculator. This will allow us to work with input and
# output, and type conversion functions. We'll also use comments to stub out
# our file before coding.
# 
# The program should prompt the user for the subtotal for their meal, along 
# with the tip percentage, and print out the calculated tip.
# BONUS --- Make it so they can't put less than 20% in.

# Prompt the user for meal subtotal
#subtotal = input("Meal subtotal: ")
#subtotal = float(subtotal)

# Prompt the user for the tip %
#tip_pct = input("Tip %: ")

# Convert % value to decimal value
#tip_pct = float(tip_pct) * 0.01

# Calculate the tip amount
#tip = subtotal * tip_pct

# Print tip amount
#print("Tip:", tip)

#def tip_calculator(subtotal, tip_pct):
#    subtotal_converted = float(subtotal)
#    tip_converted = float(tip_pct) * 0.01

#    if tip_converted < 0.20:
#        return "Sorry, that is not high enough for your server to make a living wage."

#    else:
#        tip = subtotal_converted * tip_converted
#        return "The amount to tip will be {}.".format(tip)

#def main():
#    subtotal = input("Meal subtotal: ")
#    tip_pct = input("Tip %: ")
#    print(tip_calculator(subtotal, tip_pct))

#if __name__ == "__main__":
#    main()

# STUDIO ----------------------------------------------------------------------
# It is possible to name the days 0 through 6, where day 0 is Sunday and day 6 is
# Saturday. If you go on a wonderful holiday leaving on day 3 (a Wednesday) and
# you return home after 10 nights, you arrive home on day 6 (a Satruday).
# 
# Write a general version of the program which asks for the day number that your
# vacation starts on and the length of your holiday, and then tells you the
# number of the day of the week you will return on.)

def leaving_converter(leaving_day):
    if leaving_day == 0:
        return "You will leave on a Sunday."
    elif leaving_day == 1:
        return "You will leave on a Monday."
    elif leaving_day == 2:
        return "You will leave on a Tuesday."
    elif leaving_day == 3:
        return "You will leave on a Wednesday."
    elif leaving_day == 4:
        return "You will leave on a Thursday."
    elif leaving_day == 5:
        return "You will leave on a Friday."
    elif leaving_day == 6:
        return "You will leave on a Saturday."
    else:
        return "You did not enter a valid number, 0 - 6. Try again!"

def vacation_calculator(leaving_day, arriving_day):
    return_day = (leaving_day + arriving_day) % 6
    
    if leaving_day > 6:
        return "Oops. Something isn't quite right there..."
    elif return_day == 0:
        return "After {} vacation days, you will arrive home on a Sunday!".format(arriving_day)
    elif return_day == 1:
        return "After {} vacation days, you will arrive home on a Monday!".format(arriving_day)
    elif return_day == 2:
        return "After {} vacation days, you will arrive home on a Tuesday!".format(arriving_day)
    elif return_day == 3:
        return "After {} vacation days, you will arrive home on a Wednesday!".format(arriving_day)
    elif return_day == 4:
        return "After {} vacation days, you will arrive home on a Thursday!".format(arriving_day)
    elif return_day == 5:
        return "After {} vacation days, you will arrive home on a Friday!".format(arriving_day)
    else:
        return "After {} vacation days, you will arrive home on a Saturday!".format(arriving_day)

def main():
    leaving_day = input("What day of the week (using a number 0 - 6) are you leaving? ")
    leaving_day = int(leaving_day)
    arriving_day = input("How many days is your vacation? ")
    arriving_day = int(arriving_day)

    print(leaving_converter(leaving_day))
    print(vacation_calculator(leaving_day, arriving_day))

if __name__ == "__main__":
    main()