import pyperclip
from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("contact notebook")
root.geometry("650x400")
background = '#0B6623'
root.config(bg=background)


# contact name label✅
# contact name entry✅
# contact number label✅
# contact number entry✅
# add contact button✅
# save list button✅
# copy phone number button✅
# open save file button✅
# delete contact button✅
# exit app button✅
# list box for contacts✅
# ___________________________
# functions
def add_contact():
    contact_string = name_entry.get()+": "+number_entry.get()
    listbox.insert(END, contact_string)
    name_entry.delete(0, END)
    number_entry.delete(0, END)


def delete_contact():
    listbox.delete(ANCHOR)


def save_list():
    """save the list to a simple txt file"""
    with open('contacts.txt.txt' , 'w') as f:
        list_tuple = listbox.get(0,END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+'\n')    
    



def open_list():
    with open("contacts.txt.txt", 'r')as f:
        for line in f:
            listbox.insert(END, line)


def copy_number():
    selected_contact = listbox.get(ANCHOR)
    number = selected_contact.split(": ")
    pyperclip.copy(number[1])


def exit():
    choice = messagebox.askquestion(
        "exit aplication", "Are you sure you want to close the app? ")
    if choice == 'yes':
        root.destroy()
    else:
        return


# __________________________
# name label and entry
background2 = '#FFFFE0'
name_label = Label(root, text="contact name:", bg=background,
                   fg='black', font=("Calibri", 15), anchor='w', justify=LEFT)

name_label.place(relx=0.1, rely=0.1, anchor='c')
name_entry = Entry(root, bg=background2, fg=background, width=30)
name_entry.place(relx=0.35, rely=0.1, anchor='c')
# __________________________
# number label and entry
background2 = '#FFFFE0'
number_label = Label(root, text="       contact number:   ", bg=background,
                     fg='black', font=("Calibri", 15), anchor='w', justify=LEFT)

number_label.place(relx=0.1, rely=0.2, anchor='c')
number_entry = Entry(root, bg=background2, fg=background, width=30)
number_entry.place(relx=0.38, rely=0.2, anchor='c')
# ___________________________
# add contact button
add_btn = Button(root, text="add contact", bg='#121212',
                 fg=background2, borderwidth=3, padx=100, command=add_contact)
add_btn.place(relx=0.225, rely=0.35, anchor='c')
# ____________________________
#save list button
save_btn = Button(root, text = 'save list' , bg='#121212' , fg= background2 , borderwidth=3 , padx=110.5 ,command=save_list )
save_btn.place(relx=0.225, rely=0.45, anchor='c')
# _____________________________
# copy phone number button
copyphone = Button(root, text="copy phone number", bg='#121212',
                   fg=background2, borderwidth=3, padx=30, command=copy_number)
copyphone.place(relx=0.15, rely=0.6, anchor='c')
# ______________________________
# delete contact button
deletephone = Button(root, text="delete contact", bg='#121212',
                     fg=background2, borderwidth=3, padx=47.4, command=delete_contact)
deletephone.place(relx=0.15, rely=0.7, anchor='c')
# ________________________________
# open save file button
opensaved = Button(root, text="open saved file", bg='#121212',
                   fg=background2, borderwidth=3, padx=47.4,)
opensaved.place(relx=0.15, rely=0.8, anchor='c')
# __________________________________
# exit app button
exit = Button(root, text="Exit App", bg='#121212',
              fg=background2, borderwidth=3, padx=66, command=exit)
exit.place(relx=0.15, rely=0.9, anchor='c')
# ___________________________________
# list box
listbox = Listbox(root, width=40, height=21)
listbox.place(relx=0.75, rely=0.47, anchor='c')
open_list()
root.mainloop()
