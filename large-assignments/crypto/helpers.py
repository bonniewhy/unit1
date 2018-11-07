import string

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
punctuation = string.digits + string.punctuation + " "


def alphabet_position(letter):

    if letter.isalpha() == True:
        if letter in lower_alphabet:
            index = lower_alphabet.index(letter)
            return index
        elif letter in upper_alphabet:
            index = upper_alphabet.index(letter)
            return index
    else:
        return "Needs to be a letter, plz."

def rotate_character(char, rot):

    rot = int(rot)
    if len(char) == 1: #make sure it's length 1

        if char in lower_alphabet: #return the correct lower case letter
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                return lower_alphabet[rotated_index]
            else:
                return lower_alphabet[rotated_index % 26]

        if char in upper_alphabet: #return the correct upper case letter
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                return upper_alphabet[rotated_index]
            else:
                return upper_alphabet[rotated_index % 26]

    else:
        return "String too long. D:"