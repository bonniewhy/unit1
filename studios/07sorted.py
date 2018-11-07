# WALKTHROUGH -------------------------------------------------------------------
# Write a function "remove_char" that takes two string arguments, "string" and
# "char". The first argument should be a string and the second should be a
# character (i.e. a string of length one). The function should return a new
# string, the result of which is "string" with each instance of "char" removed.

#def remove_char(string, char):
#    new_str = ""

#    for index in range(len(string)):
#        if string[index] != char:
#            new_str = new_str + string[index]

#    return new_str

#def main():
#    print(remove_char('aardvark', 'a'), 'rdvrk')
#    print(remove_char('aardvark', 'k'), 'aardvar')
#    print(remove_char('asdf', 'z'), 'asdf')
#    print(remove_char('', 'a'), '')

#if __name__ == "__main__":
#    main()

# Here's another slightly different solution that uses the fact that a string is
# a list. This one is generally a better way to loop over strings than what we
# did above, if you don't need to use the index of the current character.

#def remove_char(string, char):
#    new_str = ""

#    for this_char in string:
#        if this_char != char:
#            new_str = new_str + this_char

#    return new_str

# STUDIO -----------------------------------------------------------------------
# Since a string is just a sequence of characters, they can be sorted from least
# to greatest. Sorting can be hard so we're just going to check if a string is
# sorted. Write a function which returns a boolean indicating if the string is
# sorted or not.
# 
# Here's an example of how your function should behave. (Recall that the order
# operators are case-sensitive, so that "A" < "a" evaluates to True.)
# 
# is_sorted("ABC") == True
# is_sorted("aBc") == False
# is_sorted("dog") == False

def is_sorted(string):
    # Returns True if string is sorted from least to greatest. False otherwise.

    # TODO: Fill in details
    return False

# BONUS MISSIONS ------------------------------------------------------------
# 1. Write a function that takes a sentence with an introductory preposition
# phrase and returns the number of characters (including whitespace and
# punctuation) remaining in the string after the comma. For example, "Before
# you go to bed, you need to brush your teeth." returns 30 and "Under the warm
# sun, the cat slept deeply." returns 22.
# 
# 2. Write a function that takes in a string and converts that string to pig
# latin. Pig latin involves moving the first letter of a word to the end, then
# appending "ay". For example, the phrase "python code wins" would turn into
# "ythonpay odecay insway".
# 
# For an extra challengte, handle the case where a word starts with a vowel.
# In this case, the word should be unmodified excpet for adding ay at the end.
# For example, "all open androids" would become "allay openay androidsay".)