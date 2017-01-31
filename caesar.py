from helpers import alphabet_position, rotate_character
from sys import argv, exit



def encrypt(text, rot):
    '''Takes a string, rotates each character one by one, and returns the new string'''
    final = ""
    for i in text:
        newalpha = rotate_character(i, rot)
        final = final + newalpha
    return final

    #Makes sure the user inputs a digit as the command-line argument
def user_input_is_valid(cl_args):
    if len(cl_args) == 2 and cl_args[1].isdigit():
        return True
    else:
        return False

def main():
    print("I know that these are the words the user typed on the command line: ", argv)
    if user_input_is_valid(argv):
        encrypt(text=input("Type a message"), rot=argv[1])

    else:
        print('usage: python3 caesar.py n')
        exit()


if __name__ == '__main__':
    main()

