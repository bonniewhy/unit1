# NOTES ---
# - Syntax errors - refers to the structure of a program and the rules about that
#   structure. For example, in English, a sentence must being with a capital letter
#   and end with a period. this sentence contains a syntax error. So does this one.
# - Runtime errors - the error doesn't appear until you run the program. These are
#   called "exceptions" and they usually indicate that something exceptional (and
#   bad) has happened.
# - Semantic errors - It will run without prompting any error messages, however,
#   your program will not do the right thing. These can be tricky because it
#   requires you to work backward by looking at the output of the program and
#   trying to figure out what it is doing. They are also called "logic errors" as
#   they are generally caused by a flaw in the logic of your program.
# - To avoid debugging...
#       - Start small! It's best to do break down larger process into smaller
#         steps so you can make sure each part is working. And give yourself an
#         endorphin boost along the way.
#       - Keep It Working. Once you have a small step working, move on to the
#         next small step and add it. If you keep adding small pieces of the
#         program one at a time, it is much easier to find out what went wrong
#         if and when something does.
# - REPEAT THE MANTRA "GET SOMETHING WORKING AND KEEP IT WORKING!"
# - It is really important to test your "boundary conditions" to make sure that
#   they are right.
# - TIP -- Everyone is a suspect -- EXCEPT PYTHON. That should be the last thing
#   you think.
# - TIP -- Find clues using the error messages and making print statments to
#   find out what values are in which areas.
# - ParseError -- happens when you make a syntax error in your program, like
#   grammatical errors in writing.
#       - Usually can be traced back to missing punctuation characters
# - TypeError -- occurs when you try to combine two objects that are not
#   compatible, like an int and a str.
#       - Usually can be isolated to lines that are using mathematical operators
# - NameError -- almost always mean you have used a variable before it has a value.
#       - Usually simply caused by typos in your code
# - ValueError -- occurs when you pass a parameter to a function and the function
#   is expecting a certain type, but you pass it a different type.

# _____________________________________________________________________________

# EXERCISES -------------------------------------------------------------------
# 1. Below is a short program that prompts the user to input the number of miles
# they are to drive on a given trip and converts their anser to kilometers,
# printing the result. However, it doesn't work properly. Find and fix the error
# in the program.

#miles = input("How many miles do you have to drive? ")

#kilometers = miles * 1.60934

#print("That distance is equal to", kilometers, "kilometers.")

# What type of error did the above program have? Syntax, --runtime--, or semantic.
# Didn't convert the user's input to an int, so therefore, we can't use mathematical
# operators on it.
# 
# 2. Picture a compass where 0 degress represents North, 90 degrees represents
# East, and so on, all the way around to 360 degrees, which is again the same
# as 0 degrees: true north.
# 
# The program below envisions the scenario in which a person is facing North (aka
# 0 degrees) and spins some number of rotations, either clockwise or counter-
# clockwise (-1 represents a full counter-clockwise spin and 1 represents a full
# clockwise spin). It calculates the direction they end up facing in degrees.
# However, it doesn't work properly. Find and fix the error in the program.
# 
#spins = input("How many times did you spin? (Enter a negative number for counter-clockwise.")
#degrees = float(spins) * 360
#print("You are facing", degrees, "degrees relative to north.")
# 
# What type of error did your program have? Syntax, runtime, or --semantic--.
# The logic of the program is flawed becuase it doesn't use the modulo operator to
# start back at 0 after 360 degrees have gone by.
# 
# 3. You've written a program to convert degrees Celsius to degrees Fahrenheit. The
# program below makes the conversion in the opposite direction, from Fahrenheit
# to Celsius. However, it doesn't work properly. Find and fix the error in the
# program.
# 
#current_temp_string = input("Enter a temperature in degress Fahrenheit: ")
#current_temp = int(current_temp_string)
# 
#current_temp_celsius = (current_tmp - 32) * (5/9)
#print("The temperature in Celsius is:", current_temp_celsius)
# 
# What type of error did your program have? --Syntax--, runtime, or semantic.
# It would return a name error as there is a typo in the variable used in
# current_temp_celsius formula. It says "current_tmp" which is missing a
# necessary "e".)
# 
# 4. Football Scores -- Suppose you've written the program below. The given
# program asks the user to input the number of touchdowns and field goals scored
# by an American football team, and prints out the team's score. (We generously
# assume that for each touchdown, the team always makes the extra point.)
# 
# The European Union has decided that they want to start an American football
# league, and they want to use your killer program to calculate scores, but
# they like things that are multiples of 10 (e.g. the Metric System), and have
# decided that touchdowns will be worth 10 points (including the extra point
# they might score) and field goals are worth 5 points. Modify the program below
# to work on both continents, and beyond. It should ask the user how many points
# a touchdown is worth and how many points a field goal is worth. Then it should
# ask in turn for both the number of touchdowns and the number of field goals
# scored, and then print the team's total score.
# 
#num_touchdowns = input("How many touchdowns were scored? ")
#num_field_goals = input("How many field goals were scored? ")

#total_score = 7 * int(num_touchdowns) + 3 * int(num_field_goals)
#print("The team has", total_score, "points.")

#touchdowns = input("How many touchdowns were scored? ")
#touchdowns = int(touchdowns)
#touchdown_val = input("How many points are touchdowns worth? ")
#touchdown_val = int(touchdown_val)

#field_goals = input("How many field goals were scored? ")
#field_goals = int(field_goals)
#field_goal_val = input("How many points are field goals worth? ")
#field_goal_val = int(field_goal_val)

#total_score = (field_goal_val * field_goals) + (touchdown_val * touchdowns)

#print("The team has", total_score, "points.")