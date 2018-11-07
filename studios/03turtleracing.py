# WALKTHROUGH -----------------------------------------------------------------
# Zach and Jesse have had a long day working at LaunchCode, so after work they
# go to Dressel's Pub down the street to blow off some steam. Problem is, they
# blow off a bit too much steam. Upon leaving, they have completely lost their
# sense of direction and each walks in random directions.
# 
# We will write a program with Turtles to simulate their journey after leaving
# the pub.

#import turtle
#import random

#win = turtle.Screen()

## Create 2 turtles
#zach = turtle.Turtle()
#jesse = turtle.Turtle()

## Speed them up!
#zach.speed(10)
#jesse.speed(10)

#jesse.color("green")
#zach.color("orange")

## Make them walk randomly, loop variable represents distance to travel forward
#for distance in range(0, 50, 2): # generates [0,2,4,6,8...46,48]

#    # Create a random angle for each turtle
#    zach_angle = random.randrange(0, 181)
#    jesse_angle = random.randrange(0, 181)

#    # Turn each turtle in that random direction
#    zach.left(zach.angle)
#    jesse.left(jesse.angle)

#    # Move each turtle forward by distance
#    zach.forward(distance)
#    jesse.forward(distance)

# STUDIO --------------------------------------------------------------------
# In this studio we are going to work step by step through the problem of racing
# turtles. The idea is that we want to create two or more turtles and have them
# race across the screen from left to right. The turtle that goes the farthest
# is the winner.
# 
# There are several different, and equally plausible, solutions to this problem.
# Let's look at what needs to be done, and then look at some of the options for
# the solution. When you are faced with a problem like this in computer science
# it is often a good idea to find a solution to a simple problem first and then
# figure out how to make the solution more general. So to start, let's think
# about a solution to the simplest form of the problem, a race between two
# turtles. We'll look at more complex races later.
# 
# Here is a possible sequence of steps taht we will need to accomplish:
# 
# 1. Import the modules we need
# 2. Create a screen
# 3. Create two turtles
# 4. Move the turtles to their starting position
# 5. Send them racing across the screen
# 
# Here is the Python code for the first 4 steps above. Continue below for a
# discussion on possible solutions.)

import turtle # 1. Import the modules
import random

wn = turtle.Screen() # 2. Create a screen
wn.bgcolor('lightblue')

lance = turtle.Turtle() # 3. Create two turtles
andy = turtle.Turtle()

lance.color('red')
andy.color('blue')

lance.shape('turtle')
andy.shape('turtle')

andy.up() # 4. Move turtles to their starting point
lance.up()
andy.goto(-100, 20)
lance.goto(-100, -20)

# Your code goes here

wn.exitonclick()

# You have several choices for how to fill in the code for step 5. Below are some
# possibilities. Try coding each of the following in the box above to see the
# different kinds of behavior.
# 
# 1. Use a single call to forward for each turtle, using a random number as the
#       distance to move.
# 2. Create a for loop, using a random number for the argument passed to the range
#       function. Inside the for loop move each of the turtles forward by some
#       random number of units.
# 3. Be creative! What other ways might you simulate a race between two
#       participants?
# 
# So, which of these programs is better? Which of these programs is most correct?
# These are excellent questions. Program 1 is certainly the simplest, but it isn't
# very satisfying as far as a race is concerned. Each turtle simply moves their
# distance on their turn. Program 2 is probably the most "realistic" assuming
# realism is very important when we're talking about a simulated race of virtual
# turtles.
# 
# You may be thinking why can't each turtle just move forward until they cross
# some artificial finish line? Good question! We'll get to the answer to this, and
# look at the program in a later lesson, when we learn about something called the
# while loop.
# 
# BONUS --- Use a while loop to do the above!)