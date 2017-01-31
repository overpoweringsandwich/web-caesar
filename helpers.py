low_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import sys


def alphabet_position(letter):
    '''Takes a letter character and returns it's index value in the alphabet'''

    # Returns the index value of a capital letter
    if letter.isupper() == True:

        return upper_alpha.index(letter)
    # Returns the index value of a lower case letter
    elif letter.islower() == True:

        return low_alpha.index(letter)
    else:
        return letter
        sys.exit()


def rotate_character(char, rot):
    '''Takes a character, rotates it's index, and returns the new character'''

    # finds the index and rotates it, if non-alpha it is returned
    if char.isalpha() == False:
        return char
        sys.exit()

    idx_position = alphabet_position(char)
    new_index = idx_position + int(rot)

    # Wraps the index around the alphabet and returns new character
    if char.isupper():
        rotated_idx = (new_index % 26)
        return upper_alpha[rotated_idx]
    else:
        rotated_idx = (new_index % 26)
        return low_alpha[rotated_idx]
