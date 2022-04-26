# Cipher Generator
# 22W_CST8333_450
# Josh Kreps

import tkinter
from tkinter import *
from tkinter import messagebox
from random import shuffle
import webbrowser
from os.path import exists

# Creating gui object
top = tkinter.Tk()

# Window Settings - Main menu
top.title('CipherGenerator')
top.geometry('850x550+550+250')
top.resizable(False, False)
top.configure(bg='#FFFFAA')

# Images for buttons and logo
button_generate = PhotoImage(file="Images/Main_Button_Generate_1.png")
button_generate2 = PhotoImage(file="Images/Main_Button_Generate_2.png")
logo = PhotoImage(file="Images/Main_Logo.png")
logo_text = PhotoImage(file="Images/Generate_Logo.png")
logo_icon = PhotoImage(file="Images/About_Logo.png")

# Icons - sourced from https://icons8.com -- Credited in the "About" page as per their usage agreement
copy_icon = PhotoImage(file="Images/Generate_Copy.png")  # https://icons8.com/icon/43148/copy
export_icon = PhotoImage(file="Images/Generate_Export.png")  # https://icons8.com/icon/42847/save
about_icon = PhotoImage(file="Images/Main_About.png")  # https://icons8.com/icon/67563/info
about_icon_close = PhotoImage(file="Images/About_Close.png")  # https://icons8.com/icon/KF8JI6XBGNCv/close
exit_icon = PhotoImage(file="Images/Generate_Close.png")  # https://icons8.com/icon/102350/delete
button_code = PhotoImage(file="Images/Button_Code.png")  # https://icons8.com/icon/uooD0BINPxNE/button
button_decode = PhotoImage(file="Images/Button_Decode.png")  # https://icons8.com/icon/uooD0BINPxNE/button
help_icon = PhotoImage(file="Images/Generate_Help.png")  # https://icons8.com/icon/67560/help


# Functions for changing the button image when mouse hovers
def mouse_enter(e):
    b.config(image=button_generate2)


def mouse_leave(e):
    b.config(image=button_generate)


# Function - opens the "About" page window when the about page icon is pressed
def about_window():
    # Setting new window to top level
    window_about = Toplevel(top)

    # Window settings - About
    window_about.title('About Cipher Generator')
    window_about.geometry('405x405+783+310')
    window_about.resizable(False, False)
    window_about.configure(bg='#d5eaff')
    window_about.wm_attributes('-topmost', 'true')

    # Giving the window focus
    window_about.focus_force()

    # Function - uses webbrowser to open a link in the default browser
    def hyperlink(url):
        webbrowser.open_new(url)

    # Label - Title
    about_label_1 = Label(window_about, text='Cipher Generator V.1.0.0', font=("Calibri", 20), fg='#000000',
                          bg='#d5eaff', anchor="s")
    about_label_1.place(y=35, x=70)

    about_label_icon = Label(window_about, text='Cipher Generator V.1.0.0', font=("Calibri", 20), fg='#000000',
                             bg='#d5eaff', image=logo_icon)
    about_label_icon.place(y=80, x=144)

    # Label - Created by
    about_label_2 = Label(window_about, text='Created by: ', font=("Calibri", 15), fg='#000000',
                          bg='#d5eaff', anchor="s")
    about_label_2.place(y=190, x=100)

    # Label - Github link
    about_label_3 = Label(window_about, text='Josh Kreps', font=("Calibri", 15), fg="blue", cursor="hand2",
                          bg='#d5eaff', anchor="s")
    about_label_3.place(y=190, x=205)
    about_label_3.bind("<1>", lambda e: hyperlink("https://github.com/krep0007"))

    # Label - Icon source
    about_label_2 = Label(window_about, text='Icons were provided by: ', font=("Calibri", 15), fg='#000000',
                          bg='#d5eaff', anchor="s")
    about_label_2.place(y=250, x=100)

    # Label - Icon source link
    about_label_4 = Label(window_about, text='https://icons8.com', font=("Calibri", 15), fg="blue", cursor="hand2",
                          bg='#d5eaff', anchor="s")
    about_label_4.place(y=280, x=120)
    about_label_4.bind("<1>", lambda e: hyperlink("https://icons8.com"))

    # Button - Close
    about_close = Button(window_about, text="Copy", command=window_about.destroy, width="58", height="58", bg="#5555a5",
                         fg="#E4F7E5", font=("Calibri", 12), image=about_icon_close, borderwidth=0)
    about_close.place(x=320, y=320)


# Function - opens the "About" page window when the about page icon is pressed
def help_window():
    # Setting new window to top level
    window_help = Toplevel(top)

    # Window settings - About
    window_help.title('Help Window')
    window_help.geometry('405x405+783+310')
    window_help.resizable(False, False)
    window_help.configure(bg='#d5eaff')
    window_help.wm_attributes('-topmost', 'true')

    # Giving the window focus
    window_help.focus_force()

    # Label - Title
    help_label_1 = Label(window_help, text='How to use Cipher Generator', font=("Calibri", 20), fg='#000000',
                         bg='#d5eaff', anchor="s")
    help_label_1.place(y=15, x=50)

    # Label - Step 1
    about_label_2 = Label(window_help, text='A cipher is type of code.', font=("Calibri", 13), fg='#000000',
                          bg='#d5eaff', anchor="s")
    about_label_2.place(y=60, x=120)

    # Label - Step 2
    about_label_3 = Label(window_help, text='In this code, each letter of the alphabet is assigned \na new letter to '
                                            'represent it.', font=("Calibri", 13), fg='#000000', bg='#d5eaff')
    about_label_3.place(y=100, x=20)

    # Label - Step 3
    about_label_4 = Label(window_help, text='The "Current Cipher" shows your new code, \nshowing what each letter is '
                                            'now assigned, vertically.', font=("Calibri", 13), fg='#000000',
                          bg='#d5eaff')
    about_label_4.place(y=165, x=20)

    # Label - Step 4
    about_label_5 = Label(window_help, text='Enter text in the bottom left to translate normal \ntext into a code.',
                          font=("Calibri", 13), fg='#000000', bg='#d5eaff')
    about_label_5.place(y=230, x=30)

    # Label - Step 5
    about_label_6 = Label(window_help, text='Enter text in the bottom right to translate code \ninto normal text.',
                          font=("Calibri", 13), fg='#000000', bg='#d5eaff')
    about_label_6.place(y=295, x=30)

    # Button - Close
    about_close = Button(window_help, text="Copy", command=window_help.destroy, width="58", height="58", bg="#d5eaff",
                         fg="#d5eaff", font=("Calibri", 12), image=about_icon_close, borderwidth=0)
    about_close.place(x=320, y=330)


# Function - opens a new window when the "Generate a cipher" button is pressed
def open_new_window():
    # Lists - creating two lists containing each letter A-Z
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = list(alphabet)
    cipher = list(alphabet)

    # Setting new window to top level
    generator = Toplevel(top)

    # Window settings - Generator
    generator.title('CipherGenerator')
    generator.geometry('850x550+550+250')
    generator.resizable(False, False)
    generator.configure(bg='#E4F7E5')

    # Function - message box for delete cipher button
    def close_window():

        answer = messagebox.askquestion("Delete", "Delete this cipher?", parent=generator)
        if answer == 'yes':
            generator.destroy()

    # Label - Title
    clabel_title = Label(generator, text='Cipher Generator', font=("Calibri", 35), fg='#1818a1', bg='#E4F7E5',
                         anchor="s", image=logo_text)
    clabel_title.pack(ipady=20)

    # Label - Subtitle
    clabel_subtitle = Label(generator, text='Current Cipher', font=("Calibri", 14), fg='#1818a1', bg='#E4F7E5',
                            anchor="s")
    clabel_subtitle.pack(ipady=15)

    # Label - Alphabet
    clabel_alphabet = Label(generator, text='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z', font=("Calibri", 14),
                            fg='#000000', bg='#E4F7E5', anchor="n")
    clabel_alphabet.pack(ipady=5)

    # Button - Exit to main menu
    ex = Button(generator, text="Code text", command=close_window, width="73", height="73", bg="#5555a5",
                fg="#E4F7E5", font=("Calibri", 12), image=exit_icon, borderwidth=0)
    ex.place(x=770, y=1)

    # Button - Help menu
    he = Button(generator, text="Code text", command=help_window, width="73", height="73", bg="#5555a5",
                fg="#E4F7E5", font=("Calibri", 12), image=help_icon, borderwidth=0)
    he.place(x=5, y=1)

    # Function - list shuffler, to randomize the cipher
    def list_shuffle():
        shuffle(cipher)
        return cipher

    # Running the list shuffler
    list_shuffle()

    # Create a zip object from the two lists of letters. One containing A-Z, the other randomly shuffled
    zip_translate = zip(letters, cipher)
    zip_decode = zip(cipher, letters)

    # Create a dictionary from zip object. A-Z is now mapped to the shuffled list.
    dict_cipher = dict(zip_translate)
    dict_decode = dict(zip_decode)

    # The text in the main cipher label will be updated through a variable string
    string_variable = StringVar()
    string_variable.set(cipher)

    # Function - coding using the dictionary
    def translate():
        # Get input from textbox
        text_code = inputtxt.get(1.0, "end-1c")

        # Convert the input string to uppercase
        text_code_upper = text_code.upper()

        # Create a translation table using the input text and dictionary
        translate_table = text_code_upper.maketrans(dict_cipher)

        # Use the translation table to create a translated string
        translation = text_code_upper.translate(translate_table)

        # Set the text in the Label to the translation
        label_code.config(text=translation)

    # Function - decoding using the dictionary
    def decode():
        # Get input from textbox
        text_decode = input_decode.get(1.0, "end-1c")

        # Convert the input string to uppercase
        text_code_upper_2 = text_decode.upper()

        # Create a translation table using the input text and dictionary
        decode_table = text_code_upper_2.maketrans(dict_decode)

        # Use the translation table to create a translated string
        decode_string = text_code_upper_2.translate(decode_table)

        # Set the text in the Label to the translation
        label_decode.config(text=decode_string)

    # Functions - the text from the label is copied to the clipboard
    def copy_code():
        generator.clipboard_clear()
        generator.clipboard_append(label_code.cget("text"))

    def copy_decode():
        generator.clipboard_clear()
        generator.clipboard_append(label_decode.cget("text"))

    # Functions - Export to text file
    def export_code():
        # If the file doesn't exist, print the cipher and label txt. Otherwise, append the file with only label txt
        if exists("CipherGenerator_Export.txt"):
            with open("CipherGenerator_Export.txt", "a") as text_file:
                print(f"Your coded text:\n", label_code.cget("text"), file=text_file)
        else:
            with open("CipherGenerator_Export.txt", "w") as text_file:
                print(f"Your cipher is:\n {dict_cipher}", file=text_file)
                print(f"Your coded text:\n", label_code.cget("text"), file=text_file)

    def export_decode():
        if exists("CipherGenerator_Export.txt"):
            with open("CipherGenerator_Export.txt", "a") as text_file:
                print(f"Your decoded text:\n", label_decode.cget("text"), file=text_file)
        else:
            with open("CipherGenerator_Export.txt", "w") as text_file:
                print(f"Your cipher is:\n {dict_cipher}", file=text_file)
                print(f"Your decoded text:\n", label_decode.cget("text"), file=text_file)

    # Label - Current Cipher
    clabel_cipher = Label(generator, textvariable=string_variable, font=("Calibri", 14),
                          fg='#1818a1', bg='#E4F7E5', anchor="n")
    clabel_cipher.pack(ipady=5)

    # Input - Code text
    inputtxt = Text(generator, height=2, width=30)
    inputtxt.place(x=15, y=402)

    # Button - Code text
    c = Button(generator, text="Code text", command=translate, width="94", height="71", bg="#5555a5",
               fg="#E4F7E5", font=("Calibri", 12), image=button_code, borderwidth=0)
    c.place(x=290, y=372)

    # Label - Code text
    label_code = Label(generator, text='...', font=("Calibri", 14), fg='#000000', bg='#E4F7E5',
                       wraplength=200, justify="left", borderwidth=3, relief="groove", width=20, height=4)
    label_code.place(x=32, y=445)

    # Label - Title for code text
    label_code_title = Label(generator, text='Enter text to code here:', font=("Calibri", 14), fg='#000000',
                             bg='#E4F7E5', wraplength=200, justify="left")
    label_code_title.place(x=40, y=370)

    # Button - Copy code
    copy_code = Button(generator, text="Copy", command=copy_code, width="38", height="38", bg="#5555a5",
                       fg="#E4F7E5", font=("Calibri", 12), image=copy_icon, borderwidth=0)
    copy_code.place(x=256, y=454)

    # Button - Export code
    export_code = Button(generator, text="Export", command=export_code, width="40", height="40", bg="#E4F7E5",
                         fg="#E4F7E5", font=("Calibri", 12), image=export_icon, borderwidth=0)
    export_code.place(x=256, y=500)

    # Input - Decode text
    input_decode = Text(generator, height=2, width=30)
    input_decode.place(x=440, y=401)

    # Button - Decode text
    Button(generator, text="Decode text", command=decode, width="94", height="71", bg="#E4F7E5",
           fg="#E4F7E5", font=("Calibri", 12), image=button_decode, borderwidth=0).place(x=715, y=372)

    # Label - Decode text
    label_decode = Label(generator, text='...', font=("Calibri", 14), fg='#000000', bg='#E4F7E5',
                         wraplength=200, justify="left", borderwidth=3, relief="groove", width=20, height=4)
    label_decode.place(x=457, y=445)

    # Label - Title for decode text
    label_decode_title = Label(generator, text='Enter text to decode here:', font=("Calibri", 14), fg='#000000',
                               bg='#E4F7E5',
                               wraplength=200, justify="left")
    label_decode_title.place(x=465, y=370)

    # Button - Copy decode
    copy_decode = Button(generator, text="Copy", command=copy_decode, width="38", height="38", bg="#E4F7E5",
                         fg="#E4F7E5", font=("Calibri", 12), image=copy_icon, borderwidth=0)
    copy_decode.place(x=681, y=454)

    # Button - Export decode
    export_decode = Button(generator, text="Export", command=export_decode, width="40", height="40", bg="#E4F7E5",
                           fg="#E4F7E5", font=("Calibri", 12), image=export_icon, borderwidth=0)
    export_decode.place(x=681, y=500)


# Label - Version
label2 = Label(top, text='V1.0.0', font=("Calibri", 14), fg='#5555a5', bg='#FFFFAA', anchor="w", justify='left')
label2.pack(side='top', anchor='w')

# Button - About
about = Button(top, text="About", command=about_window, width="71", height="71", bg="#5555a5",
               fg="#E4F7E5", font=("Calibri", 12), image=about_icon, borderwidth=0)
about.place(x=770, y=1)

# Label - Title
label = Label(top, text='Welcome to Cipher Generator!', font=("Calibri", 25), fg='#5555a5', bg='#FFFFAA', anchor="s",
              image=logo)
label.pack()

# Button - Generate
b = Button(top, text="Generate a Cipher", command=open_new_window, width="300", height="100", bg="#5555a5",
           fg="#E4F7E5", font=("Calibri", 12), image=button_generate, borderwidth=0)
b.pack(side="top", pady=30)
b.bind('<Enter>', mouse_enter)
b.bind('<Leave>', mouse_leave)

# Label - subtitle
label3 = Label(top, text='Created by Josh Kreps', font=("Calibri", 14), fg='#5555a5', bg='#FFFFAA', anchor="s")
label3.pack(ipadx=100, ipady=80)

top.mainloop()
