# NOTE TAKING --
# Simple or primitive data types (int, float, bool) are values not composed of
# ----- any smaller parts. They cannot be broken down.
# Strings and lists are different because they are made up of small pieces.
# ----- In the case of strings, they are made up of smaller strings each
# ----- containing one "character".
# Strings and lists are called "collection data types".
# "+" operator represents "concatenation" on strings.
# "*" performs repetition. 'Fun'*3 = 'FunFunFun'
# Comparison operators also work on strings.
# "==" can tell if the two strings are the same.
# Other comparison operators are useful for putting words in lexicographical
# ----- order. Similar to dictionary order, except all the uppercase letters
# ----- come before the lowercase letters.
# You can find out the "ordinal value" for a given character by using a string
# ----- method called "ord".
# You can also print out the character at a given position with "chr".
# An index specifies a member of an ordered collection.
# Indexing returns a string. Python has no special type for a single character.
# ----- It is just a string of length 1.
# A substring of a string is called a "slice".
# The slice operator [n:m] returns the part of the string from the n'th character
# ----- to the m'th character, including the first but excluding the last.
# If you remove the first index (before the colon), the slice starts at the
# ----- beginning of the string. "string[:3]"
# If your remove the second index (after the colon), the slice goes to the end
# ----- of the string.
# Strings are immutable, which means you cannot change the existing string. The
# ----- best thing you can do is create a new string that is a variation on
# ----- the original.
# "Traversal" is the pattern of processing each charater in turn, doing
# ----- something to it, and continuing until the end.
# For a "while" loop, you can set up a condition, but you are responsible for
# ----- making sure that the condition is correct and making sure that
# ----- something changes inside the body to guarantee that the condition will
# ----- eventually fail and we avoid an infinite loop.
# ----- EX: fruit = "apple"
# ----- 
# ----- position = 0
# ----- while position < len(fruit):
# -----     print(fruit[position])
# -----     position += 1 # enumerate
# The "string" module provides several constants to help test wheter a character
# ----- is upper- or lowercase, or whether it is a character or a digit.
# "string.digits" is equivalent to "0123456789".
# "string.ascii_lowercase" contains all of the ascii letters that the system
# ----- considers to be lowercase.
# "string.ascii_uppercase" is all the uppercase ascii letters.
# "string.punctuation" comprises all the characters considered to be
# ----- punctuation.

# TO FIND OUT IF A PARTICULAR CHARACTER IS IN A STRING --
# 
#       def find_char(text):
#           char_exists = False
#
#       for char in "Go Spot Go":
#           if char == text:
#               char_exists = True
#
#       return char_exists
#
#           OR JUST USE THE "IN" OPERATOR.
#       print('p' in 'apple')

# ACCUMULATOR PATTERN WITH STRINGS -----

# EXAMPLE 1 ---
#def remove_vowels(s):
#    vowels = "aeiouAEIOU"
#    no_vowels = ""
#    for each_char in s:
#        if each_char not in vowels:
#            no_vowels = no_vowels + each_char
#    return no_vowels

#def main():
#    print(remove_vowels("compsci"))
#    print(remove_vowels("aAbEefIijOopUus"))

#if __name__ == "__main__":
#    main()

# EXAMPLE 2 ---
#def count(text, char):
#    letter_count = 0
#    for c in text:
#        if c == char:
#            letter_count = letter_count + 1
#    return letter_count

#def main():
#    print(count("banana", "a"))

#if __name__ == "__main__":
#    main()

# EXAMPLE 3 --- PRINT TEXT IN REVERSE
#s = "ball"
#r = ""
#for item in s:
#    r = item.upper() + r # put item first so it adds to the front
#print(r)

# ___________________________________________________________________________

# Exercise 1 --
# What is the result of each of the following:
# a. 'Python'[1]
# ----- 'y'
# b. "Strings are sequences of characters."[5]
# ----- 'g'
# c. len("wonderful")
# ----- 9
# d. 'Mystery'[:4]
# ----- Myst
# e. 'p' in 'Pineapple'
# ----- True
# f. 'apple' in 'Pineapple'
# ----- True
# g. 'pear' not in 'Pineapple'
# ----- True
# h. 'apple' > 'pineapple'
# ----- False
# i. 'pineapple' < 'Peach'
# ----- False

# ___________________________________________________________________________

# Exercise 2 --
# Write a function that will return the number of digits in an integer.

#def num_digits(number):
#    str_num = str(number)
#    return len(str_num)

#def main():
#    print(num_digits(100))
#    print(num_digits(50))
#    print(num_digits(20000))
#    print(num_digits(1))

#if __name__ == "__main__":
#    main()
    
# ___________________________________________________________________________

# Exercise 3 --
# Write a function that removes the first occurrence of a string from another 
# string.

#def remove(substr, original_string):
#    index = original_string.find(substr)
    
#    if index < 0: #substr doesn't exist in original_string
#        return original_string

#    return_str = original_string[:index] + original_string[index+len(substr):]
#    return return_str
    
#def main():
#    print(remove('an', 'banana'), 'bana')
#    print(remove('cyc', 'bicycle'), 'bile')
#    print(remove('iss', 'Mississippi'), 'Missippi')
#    print(remove('egg', 'bicycle'), 'bicycle')
#    print(remove('oo', 'Yahoohoo'), 'Yahhoo')

#if __name__ == "__main__":
#    main()

# ____________________________________________________________________________

# Exercise 4 --
# Write a function "reverse" that receives a string argument, and returns a 
# reversed version of the string.

#def reverse(text):
#    org_str = text
#    reverse = ""

#    for item in org_str:
#        reverse = item + reverse

#    return reverse

#def main():
#    print(reverse("happy"), "yppah")
#    print(reverse("Python"), "nohtyP")
#    print(reverse(""), "")

#if __name__ == "__main__":
#    main()

# ____________________________________________________________________________

# Exercise 5 --
# Write a function that recognizes palindromes. (Hint: use your reverse function
# to make this easy.)

#def reverse(text):
#    org_str = text
#    reverse = ""

#    for item in org_str:
#        reverse = item + reverse

#    return reverse

#def is_palindrome(text):
#    if reverse(text) == text:
#        return True
#    else:
#        return False

#print(is_palindrome('abba'), True)
#print(is_palindrome('abab'), False)
#print(is_palindrome('straw warts'), True)
#print(is_palindrome('a'), True)
#print(is_palindrome(''), True)

# ____________________________________________________________________________

# Exercise 6 --
# Write a function that mirrors its argument. For example, mirror('good') should
# return a string holding the value gooddoog. (Hint: Make use of the reverse
# function.)

#def mirror(text):
#    return text + reverse(text)

#def reverse(text):
#    org_str = text
#    reverse = ""

#    for item in org_str:
#        reverse = item + reverse

#    return reverse

#print(mirror('good'), 'gooddoog')
#print(mirror('Python'), 'PythonnohtyP')
#print(mirror(''), '')
#print(mirror('a'), 'aa')

# ____________________________________________________________________________

# Exercise 7 --
# Write a function that implements a substitution cipher. In a substitution
# cipher, one letter is substituted for another to garble the message. For
# example A -> Q, B -> T, C -> G, etc. Your function should take two
# parameters, the message you want to encrypt, and a string that represents
# the mapping of the 26 letters in the alphabet. Your function should return
# a string that is the encrypted version of the message.

#def encrypt_message(message, cipher):
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    encrypted_message = ""

#    for char in message:
#        if char == ' ':
#            encrypted_message = encrypted_message + ' '
#        else:
#            pos = alphabet.index(char)
#            encrypted_message = encrypted_message + cipher[pos]
    
#    return encrypted_message

#def main():
#    cipher = "badcfehgjilknmporqtsvuxwzy"

#    encrypted = encrypt_message('hello world', cipher)
#    print(encrypted)

#if __name__ == "__main__":
#    main()

# ____________________________________________________________________________

# Exercise 8 --
# Write a function that decrypts the message from the previous exercise. It
# should also take two parameters -- the encrypted message and the mixed up
# alphabet. The function should return a string that is the same as the
# original unencrypted message.

#def encrypt_message(message, cipher):
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    encrypted_message = ""

#    for char in message:
#        if char == ' ':
#            encrypted_message = encrypted_message + ' '
#        else:
#            pos = alphabet.index(char)
#            encrypted_message = encrypted_message + cipher[pos]
    
#    return encrypted_message

#def decrypt_message(message, cipher):
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    decrypted_message = ""

#    for char in message:
#        if char == ' ':
#            decrypted_message = decrypted_message + ' '
#        else:
#            pos = cipher.index(char)
#            decrypted_message = decrypted_message + alphabet[pos]

#    return decrypted_message

#def main():
#    cipher = "badcfehgjilknmporqtsvuxwzy"

#    encrypted = encrypt_message('hello world', cipher)
#    print(encrypted)
#    decrypted = decrypt_message(encrypted, cipher)
#    print(decrypted)

#if __name__ == "__main__":
#    main()

# ____________________________________________________________________________

# Exercise 9 --
# Write a function called "rot13" that uses the Caesar cipher to encrypt a
# message. The Ceasar cipher works like a substitution cipher, but each
# character is replaced by the character 13 characters to "its right" in the
# alphabet. So, for example, the letter "a" becomes the letter "n". If a letter
# is past the middle of the alphabet, then the counting wraps around to the
# letter "a" again, so "n" becomes "a", "o" becomes "b", and so on. 
# Hint: Whenever you talk about things wrapping around its a good idea to think
# of modulo arithmetic (using the remainder operator).

def rot13(mess):
    alphabet = "abcdefghijklmnopqrstuvwxyz" # establish the alphabet
    encrypted_message = "" # hold the encrypted string for returning

    for char in mess:
        if char == ' ':
            encrypted_message = encrypted_message + ' '
        else:
            rotated_index = alphabet.index(char) + 13
            if rotated_index < 26:
                encrypted_message = encrypted_message + alphabet[rotated_index]
            else:
                encrypted_message = encrypted_message + alphabet[rotated_index % 26]

    return encrypted_message


    # _________________ tutorial walk through ___________________________________
    #for item in range(len(mess)): # iterate loop for as long as the string is
    #    character = mess[item] # get the actual character value at the index
    #    character_location = alphabet.find(character) # find the location of the character in the alphabet list you established
    #    new_location = character_location + 3 # establish the new character to be used
    #    string_output += alphabet[new_location] # enumerate the new characters to the empty list you established at the beginning
    
    #return string_output
    # ______________________ continue main body of stuff ________________________
    

def main():
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))

if __name__ == "__main__":
    main()