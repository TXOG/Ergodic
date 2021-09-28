#imports below
import random
import time
import colorama
from tkinter import *
import pyperclip


def guigeneratestr():
    global issecure
    global docopy
    global entry
    global button
    global entry1
    docopyc = docopy.get()
    issecurec = issecure.get()
    numofstr = entry.get()
    numofstr = int(numofstr)
    numofchar = entry1.get()
    numofchar = int(numofchar)
    button.grid(row=8, column=0, sticky=W)
    text = Text(window, width=90, height=20, wrap=WORD, background="yellow")
    text.grid(row=7, column=0, columnspan=6, sticky=W)
    copytext = str()
    if numofstr <= 0:
        text.insert(END, "You can't generate less than 1 strings")
    elif numofstr == 1:
        if issecurec == 1:
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
            for x in range(0, numofchar):
                random_str_from_list = random.choice(shuffle_str)
                text.insert(END, random_str_from_list)
                copytext = (copytext + random_str_from_list)
            if docopyc == 1:
                pyperclip.copy(copytext)
        elif issecurec == 0:
            strchoices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                          'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                          '*', '(', ')', '<']
            for x in range(0, numofchar):
                random_str_from_list = random.choice(strchoices)
                text.insert(END, random_str_from_list)
                copytext = (copytext + random_str_from_list)
                if docopyc == 1:
                    pyperclip.copy(copytext)
    elif numofstr > 1:
        if issecurec == 1:
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
            for x in range(0, numofstr):
                for x in range(0, numofchar):
                    random_str_from_list = random.choice(shuffle_str)
                    text.insert(END, random_str_from_list)
                text.insert(END, "\n \n")
                if docopyc == 1:
                    cantcopylabel = Label(window, text="You can't copy with more than 1 string generated")
                    cantcopylabel.grid(row=6, column=1, sticky=W)
        elif issecurec == 0:
            strchoices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                          'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                          'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                          'z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                          '*', '(', ')', '<']
            for x in range(0, numofstr):
                for x in range(0, numofchar):
                    random_str_from_list = random.choice(strchoices)
                    text.insert(END, random_str_from_list)
                text.insert(END, "\n \n")
                if docopyc == 1:
                    cantcopylabel = Label(window, text="You can't copy with more than 1 string generated")
                    cantcopylabel.grid(row=6, column=1, sticky=W)
    window.mainloop()


def guigenerateint():
    global issecure
    global docopy
    global entry
    global button
    global entry1
    global entry2
    global numofresultssecureentry
    global numofresultsstandardrangeentry
    global numofresultsstandarddigitsentry
    window.geometry("682x484")
    docopyc = docopy.get()
    securec = issecure.get()
    src = isrange.get()
    sdc = isdigits.get()
    numofintdigits = entry.get()
    numofintdigitsc = int(numofintdigits)
    rangeofint = entry1.get()
    rangeofintc = int(rangeofint)
    numofintdigitss = entry2.get()
    numofintdigitssc = int(numofintdigitss)
    secure_digits_amount = numofresultssecureentry.get()
    secure_digits_amount_int = int(secure_digits_amount)
    standard_range_amount = numofresultsstandardrangeentry.get()
    standard_range_amount_int = int(standard_range_amount)
    standard_digits_amount = numofresultsstandarddigitsentry.get()
    standard_digits_amount_int = int(standard_digits_amount)
    text = Text(window, width=85, height=20, wrap=WORD, background="yellow")
    text.place(x=0, y=160)
    copytext = str()
    if securec == 1:
        if src == 1:
            text.insert(END, "Please select 1 type of generation")
        elif sdc == 1:
            text.insert(END, "Please select 1 type of generation")
        else:
            number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            #shuffling the number_list
            shuffle = random.sample(number_list, len(number_list))
            if secure_digits_amount_int > 1:
                for x in range(0, secure_digits_amount_int):
                    for x in range(0, numofintdigitsc):
                        random_number_from_list = random.choice(shuffle)
                        text.insert(END, random_number_from_list)
                    text.insert(END, "\n \n")
                random_number_from_list = ("")
                if docopyc == 1:
                    text.insert(END, "\n \n \n You cannot copy more than one integer")
            else:
                for x in range(0, numofintdigitsc):
                    random_number_from_list = random.choice(shuffle)
                    text.insert(END, random_number_from_list)
                    copytext = (str(copytext) + str(random_number_from_list))
                if docopyc == 1:
                    pyperclip.copy(copytext)

    elif src == 1:
        if sdc == 1:
            text.insert(END, "please select 1 type of generation")
        else:
            #loop for number of items user wants
            for x in range(0, standard_range_amount_int):
                #selects number from range
                number = random.randint(0, rangeofintc)
                #prints result
                text.insert(END, number)
                text.insert(END, "\n \n")
                copytext = (str(copytext) + str(number))
                if docopyc == 1:
                    if standard_range_amount_int >= 2:
                        text.insert(END, "\n \n \n You can't copy more than one integer")
                    elif standard_range_amount_int == 1:
                        pyperclip.copy(copytext)
    elif sdc == 1:
        number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if standard_digits_amount_int > 1:
            for x in range(0, standard_digits_amount_int):
                for x in range(0, numofintdigitssc):
                    random_number_from_list = random.choice(number_list)
                    text.insert(END, random_number_from_list)
                text.insert(END, "\n \n")
            random_number_from_list = ("")
            if docopyc == 1:
                text.insert(END, "\n \n \n You cannot copy more than one integer")
        else:
            for x in range(0, numofintdigitssc):
                random_number_from_list = random.choice(number_list)
                text.insert(END, random_number_from_list)
                copytext = (str(copytext) + str(random_number_from_list))
            if docopyc == 1:
                pyperclip.copy(copytext)
    else:
        text.insert(END, "Please select a generation type")
    window.mainloop()


def guichoosefuncstr():
    global window
    global docopy
    global issecure
    global entry
    global button
    global entry1
    window.destroy()
    window = Tk()
    window.title("Generate")
    label = Label(window, text="Please select all the relevant options:      ")
    label.grid(row=0, column=0, sticky=W)
    label2 = Label(window, text="Number of results:  ")
    label2.grid(row=2, column=0, sticky=W)
    entry = Entry(window, width=35, bg="light green")
    entry.grid(row=3, column=0, sticky=W)
    entry.insert(END, "1")
    label3 = Label(window, text="Number of characters in string:  ")
    label3.grid(row=4, column=0, sticky=W)
    entry1 = Entry(window, width=35, bg="light green")
    entry1.grid(row=5, column=0, sticky=W)
    entry1.insert(END, "10")
    issecure = IntVar()
    c1 = Checkbutton(window, text="Secure", variable=issecure)
    c1.grid(row=6, column=0, sticky=W)
    docopy = IntVar()
    c2 = Checkbutton(window, text="Copy", variable=docopy)
    c2.grid(row=6, column=0, sticky=N)
    button = Button(window, width=7, text="Generate", command=guigeneratestr)
    button.grid(row=7, column=0, sticky=W)
    window.mainloop()


def guichoosefuncint():
    global window
    global docopy
    global issecure
    global entry
    global button
    global entry1
    global isdigits
    global isrange
    global entry2
    global numofresultssecureentry
    global numofresultsstandardrangeentry
    global numofresultsstandarddigitsentry
    window.destroy()
    window = Tk()
    window.title("Generate")
    window.geometry("425x157")
    label = Label(window, text="Please select all the relevant options:  ")
    label.place(x=0, y=0)
    issecure = IntVar()
    csplit31 = Checkbutton(window, text="Secure", variable=issecure)
    csplit31.place(x=0, y=20)
    isrange = IntVar()
    csplit32 = Checkbutton(window, text="Standard Range", variable=isrange)
    csplit32.place(x=150, y=20)
    isdigits = IntVar()
    csplit33 = Checkbutton(window, text="Standard digits", variable=isdigits)
    csplit33.place(x=300, y=20)
    label2 = Label(window, text="Number of digits:")
    label2.place(x=0, y=50)
    entry = Entry(window, width=20, bg="light green")
    entry.place(x=0, y=70)
    entry.insert(END, "10")
    norsl = Label(window, text="Number of results:")
    norsl.place(x=0, y=90)
    numofresultssecureentry = Entry(window, width=20, bg="light green")
    numofresultssecureentry.place(x=0, y=110)
    numofresultssecureentry.insert(END, "1")
    label3 = Label(window, text="Range of 0 - ?:  ")
    label3.place(x=150, y=50)
    entry1 = Entry(window, width=20, bg="light green")
    entry1.place(x=150, y=70)
    entry1.insert(END, "1")
    norstr = Label(window, text="Number of results:")
    norstr.place(x=150, y=90)
    numofresultsstandardrangeentry = Entry(window, width=20, bg="light green")
    numofresultsstandardrangeentry.place(x=150, y=110)
    numofresultsstandardrangeentry.insert(END, "1")
    label4 = Label(window, text="Number of digits:")
    label4.place(x=300, y=50)
    entry2 = Entry(window, width=20, bg="light green")
    entry2.place(x=300, y=70)
    entry2.insert(END, "10")
    norstd = Label(window, text="Number of results")
    norstd.place(x=300, y=90)
    numofresultsstandarddigitsentry = Entry(window, width=20, bg="light green")
    numofresultsstandarddigitsentry.place(x=300, y=110)
    numofresultsstandarddigitsentry.insert(END, "1")
    docopy = IntVar()
    c2 = Checkbutton(window, text="Copy", variable=docopy)
    c2.place(x=300, y=130)
    button = Button(window, width=7, text="Generate", command=guigenerateint)
    button.place(x=365, y=130)
    window.mainloop()


def strorint():
    global isstring
    global isinteger
    isstringc = isstring.get()
    isintegerc = isinteger.get()
    if isstringc == 1:
        if isintegerc == 1:
            ooplabel = Label(window, text="2 boxes selected")
            ooplabel.grid(row=3, column=0, sticky=S)
        else:
            guichoosefuncstr()
    elif isintegerc == 1:
        if isstringc == 1:
            ooplabel = Label(window, text="2 boxes selected")
            ooplabel.grid(row=3, column=0, sticky=S)
        else:
            guichoosefuncint()
    else:
        ooplabel = Label(window, text="You need to select integer or string")
        ooplabel.grid(row=3, column=0, sticky=S)


def start():
    global window
    global isstring
    global isinteger
    window = Tk()
    window.title("Welcome to Ergodic")
    label = Label(window, text="Welcome to Ergodic, the better way to generate strings and integers")
    label.grid(row=0, column=0, sticky=E)
    isstring = IntVar()
    checkboxa = Checkbutton(window, text="String", variable=isstring)
    checkboxa.grid(row=1, column=0, sticky=E)
    isinteger = IntVar()
    checkboxb = Checkbutton(window, text="Integer", variable=isinteger)
    checkboxb.grid(row=1, column=0, sticky=W)
    button = Button(window, width=7, text="START", command=strorint)
    button.grid(row=2, column=0, sticky=S)
    window.mainloop()


start()
