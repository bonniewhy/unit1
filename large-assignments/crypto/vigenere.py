# PART 2 --- VIGENERE
# 
# If you're trying to pass notes in the back of class with your best friend Suzie,
# the Caesar cipher would be fairly easy for a nosy outsider to decode. Let's
# implement a more complicated cipher algorithm.
# 
# First, watch this short video (link) on the Vigenere cipher, courtesy of the CS50
# folks at Harvard.
# 
# As you can see in the video, Vigenere uses a word as the encryption key, rather
# than an integer. Your finished program will behave like this:
# 
# $ python vigenere.py
# Type a message:
# The crow flies at midnight!
# Encryption key:
# boom
# Uvs osck rmwse bh auebwsih!
# 
# Above, the user entered a message of "The crow flies at midnight!" and an encryption
# key of "boom", and the program printed "Uvs osck rmwse bh auebwsih!"
# 
# How did we arrive at the result? Here is a detailed breakdown:
# 
# char from input string -- char from key -- rotation amount -- result char
# T -- b -- 1 -- U
# h -- o -- 14 -- v
# e -- o -- 14 -- s
# space -- n/a -- n/a -- space
# c -- m -- 13 -- o
# r -- b -- 1 -- s
# o -- o -- 14 -- c
# w -- o -- 14 -- k
# and so on...
# 
# NOTE: As with Caesar, the upper and lower case of each character should be preserved
# and non-alphabetical characters like " " and "!" should not get encrypted.
# 
# NOTE: When we encounter a non-alphabetical character in the message, the encryption
# key does not use up another letter. For example, notice how the "m" in "boom" does
# not get "wasted", so to speak, on the space character. Instead, it is "saved" for the
# next alphabetical character, the "c" in "crow".
# 
# NOTE: Whenever we reach the end of the encryption key ("boom") before reaching the
# end of the message, the encryption key wraps back around to the beginning again (the
# letter "b").
# 
# NOTE: You may assume that the encryption key("boom") will not contain any numbers or
# special characters. Letters only.
# 
# REUSING YOUR CAESAR CODE ----------------------------------------------------------
# You probably noticed that Vigenere is very similar to Caesar. The only difference is
# that the rotation amount varies throughout the course of the message.
# 
# Whenever you find yourself in a situation like this -- faced with a coding task that
# is very similar to one you did previously -- your instinct should be to sniff around
# for more ways to reuse the code you have already written. Ideally, all the work that
# is required by both tasks should be factored out into reusable components (like
# functions).
# 
# In this case, the majority of the logic that Vigenere has in common with Caesar is
# encapsulated in those two helper functions you wrote, "alphabet_position" and 
# "rotate_character". Indeed, that is why we intentionally guided you down the path of
# writing those functions. You are going to find both of those functions equally
# helpful for implementing Vigenere.
# 
# Go ahead and copy / paste those functions into vigenere.py so you can use them. (In
# reality, copy / pasting is not a very smart thing to do here, and there is a better
# way, which you will see farther down in this assignment. But for now, just do it.)

# ENCRYPT ---------------------------------------------------------------------------
# Now that you have your helper functions, go ahead and write a new version of the
# "encrypt" function which uses the Vigenere cipher rather than Caesar.
# 
# Your first step is to figure out what the function signature should say. How should
# it be different from the Caesar version, "def encrypt(text, rot)"?
# 
# As usual, don't move on until you have tested your function against a lot of
# different inputs and seen the results you expect.
import string
from helpers import alphabet_position, rotate_character

def encrypt(text, phrase):

    punctuation = string.digits + string.punctuation + " "
    encrypted_message = ""
    index = 0

    for char in text:
        if index > len(phrase) - 1:
            index = 0

        if char in punctuation:
            encrypted_message += char

        else:
            encrypted_message += rotate_character(char, alphabet_position(phrase[index]))
            index += 1

    return encrypted_message

def main():
    sample = input("Check yo self: ")
    rotation = input("Rotate by... ")

    print(sample)
    print(encrypt(sample, rotation))

    

if __name__ == "__main__":
    main()

# 
# MAKE IT INTERACTIVE ---------------------------------------------------------------
# Finally, add the appropriate "print" and "input" statements inside a "main" function
# so that your program behaves as specified:
# 
# $ python vigenere.py
# Type a message:
# The crow flies at midnight!
# Encryption key:
# boom
# Uvs osck rmwse bh auebwsih!
# 
# PART 3 --- REFACTORING SHARED CODE -------------------------------------------------
# Remember when we said that copy / pasting those helper functions is not a smart thing
# to do? Now, let's do something better.
# 
# The reason that copy / paste is a bad idea is that now you have two copies of the 
# same exact code lying around. What happens if you realize you need to change the
# function? You will have to remember to make the same changes in both copies. That
# might not sound so bad, but imagine if you had not two, but three copies, or six,
# or eleven? Given that you want to use the same function everywhere, that function
# should only ever be defined once.
# 
# IMPORT TO THE RESCUE!!
# If a function is only defined in one place, a particular file somewhere, then how can
# some other file use it? It is actually quite easy: the other file simply needs to 
# "import" the function. You have already used the "import" keyword throughout this
# course, whenever you wanted to access code written by other people, such as the "math"
# and "random" modules. It is also possible to create and import your own code. Here's
# how:
# 
# 1. In your editor, open up a new file called helpers.py. Paste both helper functions,
#    alphabet_position and rotate_character into this new file.
# 
# 2. Next, open up caesar.py, and delete both of those functions.
# 
# 3. Finally, add this line to the top of caesar.py:
# 
# from helpers import alphabet_position, rotate_character
# 
# This says that we want to import code from a module "helpers", but that we only want
# to import particular pieces of that module, specifically the functions alphabet_position
# and rotate_character.
# 
# Now we should be able to use those functions! Try running "python caesar.py" again, and
# you should find that it works just like it did before.
# 
# NOTE: In order for this to work, it is essential that "helpers.py" be in the same
# directory as caesar.py.
# 
# NOTE: The technique we are using here is a little simpler than the way this is normally
# done. For larger projects, where the structure is a tree of folders within folders, 
# there is slightly more involved procedure for reusing code, which does not require both
# modules to live together in the same folder. If you're curious, you can read up more
# about created modules in Python in the Python module documentation(link).
# 
# Once you have Caesar working, do the same thing for Vignere: simply delete the two helper
# functions, and "import" them from "helpers.py".
# 
# Now your helper functions are defined only once, and your code remains nice and 
# DRY (Don't Repeat Yourself)!
# 
# BONUS MISSIONS! ----------------------------------------------------------------------
# Congrats! You have created two very cool encryption programs.
# 
# If you want an extra challenge, keep reading here. Otherwise, you can skip to the
# Submission section below. This section is entirely options.
# 
# Let's make a few improvements to the project by adding two new features:
# 
# 1. COMMAND-LINE ARGUMENTS
#    Add a feature that improves the user experience by allowing the user to type their
#    rotation amount as a command-line argument rather than waiting for a prompt.
# 
# 2. VALIDATION
#    Add some validation on user input, so that if the user types something dumb, your
#    program handles it gracefully, rather than crashing.
# 
# BONUS MISSION 1 --- COMMAND LINE ARGUMENTS -------------------------------------------
# Each of our programs requires two pieces of input from the user:
# ----- Caesar requires a message and rotation amount
# ----- Vigenere requires a message and an encryption key-word.
# 
# Let's now make the following tweak: instead of prompting the user for both pieces of
# info, let's allow the user to include the second value right away at the beginning.
# 
# For example, rather than Caesar behaving like this:
# $ python caesar.py
# Type a message:
# Hello, World!
# Rotate by:
# 5
# Mjqqt, Btwqi!
# 
# ... we want Caesar to instead behave like this:
# 
# $ python caesar.py 5
# Type a message:
# Hello, World!
# Mjqqt, Btwqi!
# 
# Notice how, on the first line, the user included the number 5 as an argument when
# running the program. This means that the program only needed to make on additional
# input prompt, asking for the text message. This makes for a slightly nicer user
# experience.
# 
# In order to implement this feature, you obviously need some way of knowing, inside
# your caesar.py script, that the user typed the number "5" as a command-line argument.
# 
# Conveniently enough, it just so happens that inside any Python program, you do have
# access to a list containing each of the words the user type on the command line. This
# list of strings lives in a module called "sys", and has the variable name "argv",
# short for "argument vector" ("vector" is another word for a list).
# 
# Try adding the following two lines to the beginning of your main function in your
# caesar.py file:
# 
# def main():
#   from sys import argv
#   print("This is what the user typed on the command line:", argv)
#   # the rest of your code
# 
# Now run your program, and you should see output like this:
# 
# $ python caesar.py 5
# This is waht the user typed on the command line: ['caesar.py', '5']
# Type a message:
# ... etc.
# 
# The important part is the second line. Notice that:
# 
# ----- The word "python" is not included.
# ----- The first item, argv[0] is always the name of your script (in this case, 'caesar.py').
# ----- The other arguments follow. (In this case, we only have one additional argument, '5').
# 
# Ok! Now you have all the tools you need to implement this feature. Remember that the argv
# variable is just a normal list like any other. The rotation number (5 or whatever it is),
# is sitting there inside that list, waiting for you.
# 
# First modify caesar.py to match the behavior specified above, which, once again for easy
# reference, looks like this:
# 
# $ python caesar.py 5
# Type a message:
# Hello, World!
# Mjqqt, Btwqi!
# 
# Once you have finished Caesar, make similar changes to Vigenere so that the user can
# specify their encryption key on the command-line while typing the program command.
# Vigenere should behave like this:
# 
# $ python vigenere.py boom
# Type a message:
# The crow flies at midnight!
# Uvs osck rmwse bh auebwsih!
# 
# BONUS MISSION 2 --- VALIDATION --------------------------------------------------------
# You may or may not have noticed that if the user types certain things, your program will
# freak out.
# 
# There are two main cases to handle:
# 1. User fails to type a number when specifying rotation amount.
#       $ python caesar.py grandpa
#    If the user gives you something like "grandpa" instead of "5", your program will
#    crash, probably with this error:
# 
#       ValueError: invalid literal for int() with base 10: 'grandpa' on line X
# 
# 2. User fails to provide a command-line argument.
#    Now that you are expecting the user to specify the rotation amount via a
#    command-line argument, there is a danger that the user will fail to type anything at
#    all, i.e.:
#       $ python caesar.py
# 
#    In this case, you will probably see:
#       
#       IndexError: list index out of range
# 
#    because you are trying to read from argv at an index that does not exist, since argv
#    only contains one string, rather than two.
# 
# Rather than simply crash whenever one of these things happens, your program should handle
# it more gracefully, by printing a helpful "usage" message (explaining how to properly use
# your program), and then exiting immediately, rather than continuing on and crashing.
# 
# CAESAR VALIDATION ---
# Below is an example of the Caesar program you are trying to achieve. In the example,
# Caesar repeatedly exits gracefully as the user messes up, re-runs the program, messes up
# again, etc. before finally getting it right... EXAMPLE IN TEXTBOOK
# 
# To check if the argument is an integer, there is a string method called isdigit which
# you should use. It works just like isalpha, but checks for integers rather than
# alphabetic characters.
# 
# To exit your program early, you can invoke the exit function, which is part of the sys
# module. Simply import the function by adding exit to your previous import statement:
# 
# from sys import argv, exit
# 
# and then invoke the function like this::
# 
# exit()
# 
# Ok, go validate that input!
# 
# VIGENERE VALIDATION ---
# After Caesar, make similar changes to Vigenere by validating the encryption key. Recall
# that previously, we said you could assume the encryption key (e.g. "boom") would 
# contain letters only, no numbers or special characters. Now, you may no longer make that
# assumption. The user could type any crazy thing. You must enforce the letters-only rule
# yourself.
# 
# EXAMPLE BEHAVIOR TEST IN TEXTBOOK
# 
# NOTE: You might have noticed that in this case, our usage message could certainly stand
# to be a little more helpful. If the user types an invalid encryption key, the current
# usage message doesn't really explain why their attempt was rejected.
# 
# If you want a Bonus Bonus Mission (and why not, since you have already come this far),
# you can beef up the usage message like so:
# 
# $ python vigenere.py boom!
# usage: python vigenere.py keyword
# Arguments:
# -keyword : The string to be used as a "key" to encrypt your message. Should only contain
# alphabetic characters-- no numbers or special characters.
# 
# SUBMITTING YOUR WORK -----------------------------------------------------------------
# To submit your work, you must upload your files directly, using the Upload button in the
# top-left of the Vocareum window. Upload all 3 files:
# 
# ----- caesar.py
# ----- vigenere.py
# ----- helpers.py
# 
# Finally, as usual, click Submit!
# 
# WARNING! Remember that you should not have any input statements anywhere outside of your
# main funtion. This is true for both Caesar and Vigenere. If you find yourself waiting a
# very long time (30 seconds or more) for your grade, then this is the reason why.
# 
# NOTE: If you completed the Bonus Mission, you are eligible to recieve one Pat on the
# Head from your TF. In order to redeem your Pat on the Head, you must demo your code in
# front of the TF, and show him or her that your program behaves as specified in the
# instructions.