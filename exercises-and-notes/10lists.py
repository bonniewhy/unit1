# NOTE TAKING ---

# __________________________________________________________________________________
# EXERCISE 1 ---

# Draw a reference diagram for "a" and "b" before and after the third line of the
# following Python code is executed.

# __________________________________________________________________________________
# EXERCISE 2 ---

# Create a list called "my_list" with the following six items:
# 76, 92.3, "hello", True, 4, 76
# Do it with both append and with concatenation, one item at a time.

# __________________________________________________________________________________
# EXERCISE 3 ---

# Starting with the list in Exercise 2, write Python statements to do the following:
# a. Append "apple" and 76 to the list.
# b. Insert the value "cat" at position 3.
# c. Insert the value 99 at the start of the list.
# d. Find the index of "hello"
# e. Count the number of 76s in the list.
# f. Remove the first occurrence of 76 from the list.
# g. Remove True from the list using pop and index.

# __________________________________________________________________________________
# EXERCISE 4 ---

# Write a function to count how many odd numbers are in a list.

# _________________________________________________________________________________
# EXERCISE 5 ---

# Write a Python function that will take a list of 100 random integers between 0 and
# 1000 (you can use iteration, append, and the random module to create a test list)
# and return the maximum value. (Note: there is a built-in function named "max", but
# do not use it for this exercise.)

# __________________________________________________________________________________
# EXERCISE 6 ---

# Write a function "sum_of_squares(xs)" that computes the sum of the squares of the
# numbers in the list "xs". For example, "sum_of_squares([2, 3, 4]" should return
# 4 + 9 + 16 which is "29":

# _________________________________________________________________________________
# EXERCISE 7 ---

# Sum up all the negative numbers in a list.

# _________________________________________________________________________________
# EXERCISE 8 ---

# Count how many words in a list have length 5.

# _________________________________________________________________________________
# EXERCISE 9 ---

# Although Python provides us with many list methods, it is good practice and very
# instructive to think about how they are implemented. Implement your own Python
# functions that works like the following built-in ones:
# a. count
# b. in
# c. reverse
# d. index
# e. insert
#
# Note that you cannot call your version of the in function "in", since that is a
# reserved keyword. You could call it "is_in" instead.

# __________________________________________________________________________________
# EXERCISE 10 ---

# Write a function "replace(s, old, new)" that replaces all occurences of "old" with
# "new" in a string "s":
# 

# print(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
# string = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"
# print(replace(string, 'om', 'am'), 'I love spam! Spam is my favorite food. Spam, spam, spam, yum!')
# print(replace(string, 'o', 'a'), 'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!')

# __________________________________________________________________________________
# EXERCISE 11 ---

# Write a function that will sum up all the elements in a list up to, but not
# including, the first even number.

# def sum_of_initial_odds(nums):
#    # your code here

#print(sum_of_initial_odds([1, 3, 1, 4, 3, 8]), 5)
#print(sum_of_initial_odds([6, 1, 3, 5, 7]), 0)
#print(sum_of_initial_odds([1, -7, 10, 23]), -6)
#print(sum_of_initial_odds(range(1,555,2)), 76729)