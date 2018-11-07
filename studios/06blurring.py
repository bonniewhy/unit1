# WALKTHROUGH -------------------------------------------------------------------
# For this walkthrough, we will write a program to apply a red filter to an image.
# (Note that when you run the code, it will take a few seconds to process.)

import image
import sys

image = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(0, img.getWidth()):
    for j in range(0, img.getHeight()):
        old_p = img.getPixel(i, j)
        red = old_p.getRed()
        new_p = image.Pixel(red, 0, 0)
        new_img.setPixel(i, j, new_p)

new_img.draw(win)
win.exitonclick()

# STUDIO -----------------------------------------------------------------------
# For this studio, your job is to write an algorithm that processes an image to
# make it "fuzzy" looking. SEE TEXTBOOK FOR EXAMPLES / TO RUN YOUR CODE.
# 
# The algorithm to achieve this effect is actually fairly simple: for each pixel,
# randomly choose one of its neighboring pixels, and use that pixel's color
# instead.
# 
# For example, imagine that the table below is a zoomed-in view of the pixels in
# our image, and that we are trying to alter the center pixel (the one whose color
# is "E"):
# 
# A B C
# D E F
# G H I
# 
# We want to randomly choose one of the 9 pixels in this grid, and insert its
# color to replace the center one. Let's say we choose the bottom-left. This will
# alter the resulting image like so:
# 
# A B C
# D G F
# G H I
# 
# Notice that the center pixel recieved the color "G".
# 
# Of course, you want to run every pixel through this same process, so the outer
# ones should change as well (but in the example above, we only focused on the
# particular moment when the center pixel was being altered).
# 
# Also note that it is okay if, when randomly selecting a neighbor, you happen
# to choose the center pixel itself. The resulting pixel will be unchanged, but
# this should happen rarely enough (once per 9 tries) that the overall image will
# still be nice and fuzzy. Not worrying about this fluke will shorten the amount
# of code you need to write.
# 
# TIPS:
#   - If you use pixel idexes "i" and "j", you can access the neighbors by adding
#     and subtracting one from those numbers, ie i + 1, i - 1, ...
#   - If your pixel is on the very edge of the image, then you won't have 8
#     neighbors to choose from. For example, on the left edge, you don't have any
#     neighbors to your left. Lucky for you, we've given you started code in which
#     the iteration starts at 1 instead of 0, and stops 1 pixel short of the max.
#     You're welcome!

#import image
#import sys
#import random

#img = image.Image("luther.jpg")
#new_img = image.EmptyImage(img.getWidth(), img.getHeight())
#win = image.ImageWin(img.getWidth(), img.getHeight())

#for i in range(1, img.getWidth() - 1):
#    for j in range(1, img.getHeight() - 1):
#        # TODO: Randomly choose the coordinates of a neighboring pixel

#        # TODO: In the new image, set this pixel's color to the neighbor's color.

#new_img.draw(win)
#win.exitonclick()

# BONUS MISSIONS --------------------------------------------------------------
# 1. Write a function that takes in an integer and then displays the multiplication
# table of that size. For example, if given integer was 3, the following
# multiplication table would be displayed:
# 
# 0 0 0 0
# 0 1 2 3
# 0 2 4 6
# 0 3 6 9
# 
# 2. Write a program that allows someone to play the classic game of rock, paper,
# scissors against the computer. First, prompt the user to enter how many games
# should be played in the "best of" format, ie best of 5 would require someone to
# win 3 times, best of 9 would require someone to win 5 times, etc.
# 
# Next, start to simulate the games. For the human player, you should prompt them
# to enter whether they would like to play rock, paper, or scissors. The computer
# player should randomly choose one of the the three options. You should then
# display the result of the match and current number of wins for each player. If a
# tie occurs, it should not count towards the total number of matches played.
# 
# HINT: It may be easier to use numbers to represent the three different choices of
# "rock", "paper", and "scissors".)