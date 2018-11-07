# WALKTHROUGH ------------------------------------------------------------------
# Imagine you're an American tourist in London. You've brought with you a bunch
# of Union Jack souvenir flags to sell, the proceeds of which will fund your
# excursions to local pubs. Each flag would be sold for $3 in the US, and the
# average pint in London costs 3 pounds, 79 pence.
# 
# We will write a program that allows us to calculate how many pints of beer we
# would be able to afford if we sell a certain quantity of souvenir flags. Since
# the flags are purchased in dollars, we'll need to convert from dollars to
# pounds to determine the cost in the UK.)

# Prompt for dollar to pound exchange
pounds_per_dollar = input("Current dollar-to-pound exchange rate: ")
pounds_per_dolla = float(pounds_per_dollar)

# Prompt for number of flags to sell
num_flags = input("How many flags did you sell?")
num_flags = int(num_flags)

# Create variables for fixed values (cost flag, cost of pint)
pounds_per_pint = 3.79
dollars_per_flag = 3

# Calculate how much a flag costs in pounds
pounds_per_flag = dollars_per_flag * pounds_per_dollar

# Calculate how many pounds I'll have after selling them all
revenue = num_flags * pounds_per_flag

# Calculate number beers I can buy with that amount of money
num_prints = revenue / pounds_per_pint
num_prints = int(num_pints)

# Print out number of pints
print("You can afford", num_pints, "pints of beer!")

# STUDIO ----------------------------------------------------------------------- 
# Here's the scenario:
# 
# You run a hip new artisanal donut shop, the Loop Hole, which, in its short
# lifetime, has alread rocked the boutique-desserts market with numerous
# "disruptions", including:
# --- A minimalist menu consisting of just one type of donut per day. Manager's
# ----- special... always Manager's special.
# --- Giving customers the option to order fractional amounts of donuts, eg.
# ----- 1.7 donutes, please.
# --- A progressive pay-what-you-want pricing system, in which the customer pays
# ----- what they think is a fair price. (Of course, you do provide a "suggested
# ----- price".)
# 
# Now it's time to implement your latest innovation, an app via which users can
# pre-order donuts remotely from the conveniences of... the command-line terminal
# on their computer.
# 
# In the editor below, write the program which introduces the flavor of the day,
# and then takes the user's order.
# 
# Taking their order involves asking two questions:
# --- 1. How many donuts do they want to buy?
# --- 2. How much do you want to pay per donut?
# 
# After getting input, you should:
# --- 3. Inform the user of the total cost of their order.
# --- 4. Don't forget to include sales-tax, which is, let's say 5%
# 
# Here's an example of how the finished program should behave. Note that lines
# starting with >>> represent user input.
# 
# Welcome to the Loop Hole!
# Today's Manager's Special is:
# Crunch Jelly: A traditional jelly donut in which the jelly filling is made
# entirely of Capn' Crunch Oops! All Berries
# How many would you like?
# >>> 3.33333
# How much would you like to pay per donut (suggested prices is $4.35 each)?
# >>> 2.5
# Ok, let me prepare that for you.....
# After tax, your total is: $8.74999125
# Thank you for snacking! Loop back around here soon!
# 
# Notice that the total price $8.74999125 went way beyond 2 decimal places.
# Obviously, it would be a little nicer to round that to $8.75. We haven't
# learned this yet, but you'll be able to do this later. Don't worry about it now.
# 
# BONUS --- Do worry about it. Figure out how to round to 2 decimal places.
# 
# (Also, don't be concerned if your program gives an answer with a slightly
# different number of decimal places than the example program above. This is just
# a precision issue.)
# 
# For the Manager's Special, you can make something up (you are the Manager, after
# all), or just use the Crunch Berries example. Whatever you decide, you can
# simply hard-code it directly into your code. In other words, the flavor doesn't
# actually have to change depending on what day it is. The important part of this
# Studio is the process involved in calculated the cost of the user's order.
# 
# BONUS --- Make the manager's special change conditional to the day of the week.
# Either add an extra input to put in the day of the week themselves, or use the
# date time module to figure it out by itself.)