# NOTES ---
# - A value is one of the fundamental things -- like a word or number -- that a
#   program manipulates. Also known as "objects".
# - Use "type()" to figure out what type an object is (eg int, str, float, etc).
# - Triple quoted strings can span across multiple lines.
# - For variables, by convention, we don't use uppercase on them. Case matters.
# - Variables have to begin with a letter.
# - A statement is an instruction that the Python interpreter can execute.
#   Ex. while, for, if, import, etc.
# - An expression is a combination of values, variables, operators, and calls to
#   functions. Expressions need to be evaluated.
# - The input function returns a string.
# - Python follows the same precedence rules for its mathematical operators that
#   mathematics does. PEDMAS
# - While in mathematics, a statement of assignment is always true, that is not
#   the case in Python.
# - One of the most common forms of reassignment is an "update". EX x = x + 1
#   This translates to "get the current value of x, add one, and then update
#   x with the new value".
# - Before you can update a variable, you have to "initialize" it. Or you'll get
#   an error because it executes the expression on the right first.
# - Sometimes programmers talk about "bumping" a variable which means incrementing
#   it by 1.)
# - // = will result in an int value. / = will result in a float value.
# __________________________________________________________________________

# EXERCISES ----------------------------------------------------------------
# 1. Evaluate the following numerical expressions in your head, then use the
# active code window to check your results:
# 
#print(5 ** 2, 25)
#print(9 * 5, 45)
#print(15 / 12, 1.25)
#print(12 / 15, 0.8)
#print(15 // 12, 1)
#print(12 // 15, 0)
#print(5 % 2, 1)
#print(9 % 5, 4)
#print(15 % 12, 3)
#print(12 % 15, 12)
#print(6 % 6, 0)
#print(0 % 7, 7) 

# _______________________________________________________________________________
# 2. What is the order of the arithmetic operations in the following expression?
# Evaluate the expression by hand and then check your work:
# 
#print(2 + (3 - 1) * 10 / 5 * (2 + 3), 22.0) 

# _______________________________________________________________________________
# 3. Many people keep time using a 24 hour clock (11 is 11AM and 23 is 11pm, 0
# is midnight.)
# 
# If it is currently 13 and you set your alarm to go off in 50 hours, the hour will
# be 15 (3PM). Write a program to solve the general version of the above problem.
# Ask the user for the current time (in hours), and then ask for the number of
# hours to wait for the alarm.
# 
# Your program should output what the hour will be on the clock when the alarm goes
# off.
#
#current_time = input("What time is it (hours only)? ")
#current_time = int(current_time)

#alarm_length = input("How many hours until the alarm should go off? ")
#alarm_length = int(alarm_length)

#alarm_hours = current_time + alarm_length % 24

#print("Your alarm will go off at", alarm_hours, "o'clock.")

# _______________________________________________________________________________
# 4. Take the sentence: All work and no play makes Jack a dull boy. Store each word
# in a separate variable, then print out the sentence on one line using "print".
#
#word_one = "All"
#word_two = "work"
#word_three = "and"
#word_four = "no"
#word_five = "play"
#word_six = "makes"
#word_seven = "Jack"
#word_eight = "a"
#word_nine = "dull"
#word_ten = "boy."

#print(word_one, word_two, word_three, word_four, word_five, word_six, word_seven, word_eight, word_nine, word_ten)

# _______________________________________________________________________________
# 5. Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6.
# 
#print(6 * 1 - 2, 4)
#print(6 * (1 - 2), -6)

# _______________________________________________________________________________
# 6. The formula for computing the final amount if one is earning compound interest
# is given on Wikipedia as A = P(1 + r / n) ^ nt.
#   P = principal amount (initial investment)
#   r = annual nominal interest rate (as a decimal)
#   n = number of times the interest is compounded per year
#   t = number of years
# 
# Write a python program that assigns the principal amount of 10000 to variable P,
# assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then
# have the program prompt the user for the number of years, t, that the money will
# be compounded for. Calculate and print the final amount after t years.

#p = 10000
#r = 0.08
#n = 12
#t = input("What is the number of years the interest will be compounded for? ")
#t = int(t)

#result = p * ( ((1 + (r / n)) ** (n * t)) )

#print("Your final amount after", t, "years will be", result, ".")

# _______________________________________________________________________________
# 7. Write a program that will compute the area of a circle. Prompt the user to
# enter the radius, and then print the answer, like this:
# 
# What is the radius of your circle?
# >>> 7.8
# 191.0376

#radius = input("What is the radius of your circle? ")
#radius = int(radius)

#area = 3.14 * (radius ** 2)

#print(area)

# _______________________________________________________________________________
# 8. Write a program that will compute the area of a rectangle. Prompt the user
# to enter the width and height of the rectangle. Print a nice message with the
# answer.
#
#width = input("Enter the width: ")
#width = int(width)

#height = input("Enter the height: ")
#height = int(height)

#area = width * height

#print(area)
# _______________________________________________________________________________
#  
# 9. Write a program that will compute MPG for a car. Prompt the user to enter the
# number of miles driven and the number of gallons used. Print a nice message with
# the answer, like this:
# 
# How many miles have you driven?
# >>> 150
# How many gallons have you used?
# >>> 5
# Your car gets 30 miles per gallon.

#miles = input("How many miles have you driven? ")
#miles = int(miles)
#gallons = input("How many gallons did you use? ")
#gallons = int(gallons)

#mpg = miles // gallons

#print("Your car gets", mpg, "miles per gallon.")

# _______________________________________________________________________________
# 10. Write a program that will convert degress Celsius to degrees Fahrenheit.

#celsius = input("How many degrees Celcius is it? ")
#celsius = int(celsius)

#fahrenheit = celsius * (9 / 5) + 32

#print("It is", fahrenheit, "degrees Fahrenheit.")

# _______________________________________________________________________________
# 11. Write a program that will convert degress Fahrenheit to degress Celsius,
# like that:
# 
# What is the temperature in Fahrenheit?
# >>> 32
# 32.0 degress Fahrenheit is 0.0 degress Celsius. 

#fahrenheit = input("How many degrees Fahrenheit is it? ")
#fahrenheit = int(fahrenheit)

#celsius = (fahrenheit - 32) / (9 / 5)

#print("It is", celsius, "degrees Celsius.")
