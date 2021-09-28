#imports below
import random
import time
import colorama

print("""
      ███████╗██████╗  ██████╗  ██████╗ ██████╗ ██╗ ██████╗
      ██╔════╝██╔══██╗██╔════╝ ██╔═══██╗██╔══██╗██║██╔════╝
      █████╗  ██████╔╝██║  ███╗██║   ██║██║  ██║██║██║
      ██╔══╝  ██╔══██╗██║   ██║██║   ██║██║  ██║██║██║
      ███████╗██║  ██║╚██████╔╝╚██████╔╝██████╔╝██║╚██████╗
      ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝
      Welcome to ergodic v1.1
      """)


def srandomnum():
    #create urange and rn variables global
    global urange
    global rn
    print("\n \n")
    #get input for rn, if not an integer return error message
    try:
        rn = int(input("Enter how many random numbers you want: "))
    except ValueError:
        print("Invalid input: enter an integer, please re-enter request \n")
        srandomnum()
    #get input for urange, if not an integer return error message
    try:
        urange = int(input("Enter number range: "))
    except ValueError:
        print("Invalid input: enter an integer, please re-enter request \n")
        srandomnum()
    #loop for number of items user wants
    for x in range(0, rn):
        #selects number from range
        number = random.randint(0, urange)
        #prints result
        print(number)
    #prints finished and allows option to go back to menu
    print("\n Finished! Would you like to go back to the menu? (y/n)")
    endoption = input()
    endoption = endoption.lower()
    if endoption == ("y"):
        print("\n \n")
        choosefunc()
    elif endoption == ("n"):
        exit()
    else:
        lastinput = input("Invalid: will exit, press anything to continue")


def srandomstr():
    global slength
    print("\n \n")
    try:
        slength = int(input("Enter number of characters in string: "))
    except ValueError:
        print("Invalid - please enter an integer \n")
    strchoices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                  'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                  'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                  'z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                  '*', '(', ')', '<']
    for x in range(0, slength):
        random_str_from_list = random.choice(strchoices)
        print(random_str_from_list, end="")
    print("\n Finished! Would you like to go back to the menu? (y/n)")
    endoption = input()
    endoption = endoption.lower()
    if endoption == ("y"):
        print("\n \n")
        choosefunc()
    elif endoption == ("n"):
        exit()
    else:
        lastinput = input("Invalid: will exit, press anything to continue")


def crandomnum():
    user_range = int(input("Enter number of digits: "))

    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #shuffling the number_list
    shuffle = random.sample(number_list, len(number_list))

    for x in range(0, user_range):
        random_number_from_list = random.choice(shuffle)
        print(random_number_from_list, end="")
    print("\n Finished! Would you like to go back to the menu? (y/n)")
    endoption = input()
    endoption = endoption.lower()
    if endoption == ("y"):
        print("\n \n")
        choosefunc()
    elif endoption == ("n"):
        exit()
    else:
        lastinput = input("Invalid: will exit, press anything to continue")


def crandomstr():

    user_range = int(input("Enter number of characters in string: "))

    string_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                   'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                   'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                   'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                   'z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                   '*', '(', ')', '<']
    #shuffling the number_list
    shuffle_str = random.sample(string_list, len(string_list))

    for x in range(0, user_range):
        random_str_from_list = random.choice(shuffle_str)
        print(random_str_from_list, end="")
    print("\n Finished! Would you like to go back to the menu? (y/n)")
    endoption = input()
    endoption = endoption.lower()
    if endoption == ("y"):
        print("\n \n")
        choosefunc()
    elif endoption == ("n"):
        exit()
    else:
        lastinput = input("Invalid: will exit, press anything to continue")


def choosefunc():
    intorstr = input("Are you looking to generate an integer or a string (int or str): ")
    intorstr = str(intorstr)
    intorstr = intorstr.lower()
    if intorstr == ("int"):
        ot = input("Choose your output type (standard or secure): ")
        ot = str(ot)
        ot = ot.lower()
        if ot == ("standard"):
            srandomnum()
        elif ot == ("secure"):
            crandomnum()
        elif ot == ("c"):
            crandomnum()
        else:
            print("Invalid \n")
            choosefunc()
    elif intorstr == ("str"):
        ot = input("Choose your output type (standard or secure): ")
        ot = str(ot)
        ot = ot.lower()
        if ot == ("standard"):
            srandomstr()
        elif ot == ("secure"):
            crandomstr()
        else:
            print("Invalid \n")
            choosefunc()
    else:
        print("Invalid \n")
        choosefunc()


choosefunc()
