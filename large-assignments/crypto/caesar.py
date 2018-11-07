# PART 1 --- CAESAR

# Now it's time for some encryption!

# In chapter 9, you might have worked on an exercise that asked
# you to write a function called "rot13", which used the Caesar
# Cipher to encrypt a message. If you need a refresher, this is
# what the exercise said:

# Write a function called "rot13" that uses the Caeser cipher to
# encrypt a message. The Caesar cipher works like a substitution
# cipher, but each character is replaced by the character 13
# characters to "its right" in the alphabet. So, for example, the
# letter "a" becomes the letter "n". If a letter is past the middle
# of the alphabet, then the counting wraps around to the letter "a"
# again, so "n" becomes "a", "o" becomes "b" and so on. Hint:
# Whenever you talk about things wrapping around its a good idea to
# think of modulo arithmetic (using the remainder operator).

# The idea is to iterate over the message character by character,
# rotating each letter 13 places to the right. So, for example:

# a becomes n
# b becomes o
# c becomes p
# etc...

# At the end of the alphabet, we wrap back around to a, so that:

# m becomes z
# n becomes a
# o becomes b
# etc...

# The end result is a super secret coded message that looks like
# gibberish to any outsiders.

# We're going to build a more general version of the rot13 algorithm that
# allows a message to be encrypted using any rotation amount, not just 13.
# Ultimately, users will be able to type a message in the terminal, and
# specify a rotation amount (13, 4, 600, etc), and your program will print
# the resulting encrypted message.

# The final interactive program will run like this:

#$ python caesar.py
#Type a message:
#Hello, World!
#Rotate by:
#5
#Mjqqt, Btwqi!

# We are going to do this in a few steps, using some helper functions. This
# will help break the problem down into manageable steps. Furthermore, you
# will be able to reuse the same helper functions when you move on to Part 2.

# ALPHABET_POSITION ---------------------------------------------------------
# Open up your "caesar.py" file in Visual Studio Code. In that file, write a
# function "alphabet_position(letter)", which receives a letter (that is, a
# string with only one alphabetic character) and returns the 0-based numerical
# position of that letter within the alphabet.

# Here are some examples:
# a -- 0
# A -- 0
# b -- 1
# y -- 24
# z -- 25
# Z -- 25

# NOTE: The function should be case-insensitive.
# NOTE: You can assume that your input will definitely be a letter. Don't worry
# about what might happen if somebody tries to use your function with an input
# parameter that is something other than a single letter, like 
# "alphabet_position("grandpa22!")"

# When (you think) you are finished, the best way to test your function is to
# fire up the Python shell in your terminal, and then import your file as a
# module.

#$ python
#>>> import caesar
#>>> caesar.alphabet_position("a")
#0
#>>> caesar.alphabet_position("E")
#4
#... etc.

# WARNING: It is important that you test your function to make sure it works
# BEFORE MOVING ON. This practice of testing each little piece of your code in
# isolation before trying to put all the pieces together will save you a lot
# of time and headaches.

#def main():
#    sample = input("What letter to check: ")
#    print(alphabet_position(sample))

# ROTATE_CHARACTER ---------------------------------------------------------------
# Next, write another helper function "rotate_character(char, rot)" which recieves
# a character "char" (that is, a string of length 1), and an integer "rot". Your
# function should return a new string of length 1, the result of rotating "char" by
# "rot" number of places to the right.

# Here are some example input values, with the corresponding return values.
# char -- rot -- return
# a -- 13 -- n
# a -- 14 -- o
# a -- 0 -- a
# c -- 26 -- c
# c -- 27 -- d
# A -- 13 -- N
# z -- 1 -- a
# Z -- 2 -- B
# ! -- 37 -- !
# 6 -- 13 -- 6

# NOTE: The upper or lower case of the letters should be preserved. For example,
#       "rotate_character("A", 13)" results in "N", rather than "n".
# NOTE: For non-alphabetical characters, you should ignore the "rot" argument and
#       simply return "char" untouched. For example, "!" and "6" in the table above.

# Okay, go code like a champ.

# HINT: You should make use of your own alphabet_position function! If feeling
# confused, you may want to re-read about how Functions Can Call Other Functions (link).
# 
# WARNING: Once again, before moving on to the next stage, make sure to test
# "rotate_character" with a wide variety of input values (beyond just the examples
# given)

#def main():
#    sample = input("Check yo self: ")
#    rotation = input("Rotate by... ")

#    print(alphabet_position(sample))
#    print(rotate_character(sample, rotation))

# ENCRYPT --------------------------------------------------------------------------
# Now let's get to the heart of the matter. Write one more function called
# "encrypt(text, rot)", which recieves as input a string and an integer. This is just
# like the rot13 function, but instead of hardcoding the number 13, your function
# should recieve a second argument, rot which specifies the rotation amount. Your
# function should return the result of rotating each letter in the "text" by "rot"
# places to the right.
# 
# Here are some examples:
# 
# text -- rot -- return
# a -- 13 -- n
# abcd -- 13 -- nopq
# LaunchCode -- 13 -- YnhapuPbqr
# LaunchCode -- 1 -- MbvodiDpef
# Hello, World! -- 5 -- Mjqqt, Btwqi!
# 
# NOTE: The "text" argument might contain non-alphabetic characters (spaces, numbers,
# symbols). You should leave these as they are.
# 
# HINT: You should make use of your own "rotate_character" function (which should
# make it very easy to satisfy the condition above).
# 
# WARNING: DON'T FORGET TO TEST!!
# 
# MAKE IT INTERACTIVE -------------------------------------------------------------
# You're almost done with Caesar! The last step is simply to write some "print" and
# "input" statements so the user can run your program from the terminal. Remember,
# you should ask the user for their message and rotation amount, and then print the
# encrypted message:
# 
# $ python caesar.py
# Type a message:
# Hello, World!
# Rotate by:
# 5
# Mjqqt, Btqwi!
# 
# Recall that, as described (link) in the Initials assignment, you should place
# everything "loose" inside a "main" function.
# _________________________________________________________________________________ 

import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    punctuation = string.digits + string.punctuation + " "
    encrypted_message = ""

    for char in text:
        if char in punctuation:
            encrypted_message = encrypted_message + char

        else:
            encrypted_message = encrypted_message + rotate_character(char, rot)

    return encrypted_message
        


def main():
    sample = input("Check yo self: ")
    rotation = input("Rotate by... ")

    print(sample)
    print(encrypt(sample, rotation))

    

if __name__ == "__main__":
    main()