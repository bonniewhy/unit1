# WEEKLY GRADED ASSIGNMENT ------------------------------------------------------
# This is a tricky one!
# 
# You have a thermostat that allows you to set the room to any temperature between
# 40 and 89 degrees.
# 
# The thermostat can be adjusted by turning a circular dial. For instance, if the
# temperature is set to 50 degrees and you turn the dial 10 clicks toward the left,
# you will set the temperature to 40 degrees. But if you keep turning 1 click to
# the left (represented as -1) it will circle back around to 89 degrees. If you
# are at 40 degrees and turn to the right by one click, you will get 41 degrees.
# As you continue to turn to the right, the temperature goes up, and the temperature
# gets closer and closer to 89 degrees. But as soon as you complete one full
# rotation (50 clicks), the temperature cycles back around to 40 degrees.
# 
# Write a program that calculates the temperature based on how much the dial has
# been turned. The number of clicks (from the starting point of 40 degrees) is
# contained in a variable. You should print the current temperature for each given
# click variable so that your output is as follows:
# 
# The temperature is 40
# The temperature is 89
# The temperature is 64
# The temperature is 41
# The temperature is 89
# The temperature is 40

# For each click variable, calculate the temperature and print it as shown in the instructions
#start_temp = 40

#click_1 = 0
#print("The temperature is", start_temp + (click_1 % 50))
#click_2 = 49
#print("The temperature is", start_temp + (click_2 % 50))
#click_3 = 74
#print("The temperature is", start_temp + (click_3 % 50))
#click_4 = 41
#print("The temperature is", start_temp + (click_4 % 50))
#click_5 = -1
#print("The temperature is", start_temp + (click_5 % 50))
#click_6 = 200
#print("The temperature is", start_temp + (click_6 % 50))

# BONUS --- Make it a function so the user can input any number of clicks they want.
# Make sure to print the number of clicks you went for testing purposes in addition
# to what the temperature is now set at.

#def thermostat(start_temp, clicks):
#    return start_temp + (clicks % 50)

#def main():
#    start_temp = int(input("What temperature is the thermostat set at? "))
#    clicks = int(input("How many clicks do you want to turn it? "))

#    print("You have set the temperature to", thermostat(start_temp, clicks), "degrees.")

#if __name__ == "__main__":
#    main()