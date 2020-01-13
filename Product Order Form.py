# import modules for this application
import tkinter as tk
from tkinter import *
from tkinter import ttk

import sqlite3
from sqlite3 import Error

# Product Database, sqlite3


def sql_connection():
    try:
        connection = sqlite3.connect('pro_database.db')
        return connection
    except Error:
        print(Error)

    # finally:
    #     connection.close()


# def create_table(connection):
#     try:
#         cursor_obj = connection.cursor()
#         cursor_obj.execute("CREATE TABLE product( first_name text, \
#                        last_name text, \
#                        address text, \
#                        city text, \
#                        state text, \
#                        zipcode integer )")
#         connection.commit()
#     except Error:
#         print('table product already exists')
#

# customer = (1, f, l, a, c, s, z)


def insert_table(connection, customer):
    cursor_obj = connection.cursor()
    cursor_obj.execute("INSERT INTO product(first_name, last_name,\
                                              address, city, state, zipcode) \
                                              VALUES(?, ?, ?, ?, ?, ?)", customer)
    connection.commit()



# call create_table function and pass sql_connection as the argument
# create_table(sql_connection())





root = Tk()
root.title('Product Order Form')
root.geometry('980x580')
root.minsize(width=980, height=450)

# label and textbox font
labelfont = ('Arial', 20)

# define Frame
lbl_frame = LabelFrame(root, labelanchor='n', font=('Arial', 20), pady=30)
lbl_frame.pack(fill='both', expand='yes',)

# top = Label(lbl_frame, text='Product Order Form', font=('Arial', 20), pady=40)
# top.grid(row=0, column=2)


# # Submit button function
# def btn(arg=None):
#     """This function retrieves the textbox input
#      and delete input after you submit"""
#     global del_entry
#     for d in del_entry:
#         # get text input
#         dr = d.get()
#         lb.config(text=dr)
#         print(dr)
#         # delete text after submit
#         d.delete(0, END)


def btn(arg=None):
    """This function retrieves the textbox input
     and delete input after you submit"""
    global del_entry
    global f, l, a, c, s, z
    f = f_entry.get()
    l = l_entry.get()
    a = address_entry.get()
    c = city_entry.get()
    s = state_entry.get()
    z = zipcode_entry.get()
    final = f + '\n' + l + '\n' + a + '\n' + c + '\n' + s + '\n' + z
    lb.config(text=final)

# delete entry (textbox)
    for d in del_entry:
        d.delete(0, END)

# resize the window after submit
    lb.config(font=('Arial', 20))

# call create_table function and pass sql_connection as the argument
    customer = (f, l, a, c, s, z)

    # create_table(sql_connection())
    insert_table(sql_connection(), customer)


# define Labels and Entry textbox
f_name = Label(lbl_frame, text='First Name', font=labelfont, padx=30, pady=10)
f_name.grid(row=1, column=0)
f_entry = ttk.Entry(lbl_frame, width=20,)
f_entry.grid(row=1, column=1)
f_entry.focus()


l_name = Label(lbl_frame, text='Last Name', font=labelfont, padx=30, pady=10)
l_name.grid(row=2, column=0, padx=10)
l_entry = ttk.Entry(lbl_frame, width=20)
l_entry.grid(row=2, column=1)

address = Label(lbl_frame, text='Address', font=labelfont, padx=30, pady=10)
address.grid(row=3, column=0)
address_entry = ttk.Entry(lbl_frame, width=20)
address_entry.grid(row=3, column=1)

city = Label(lbl_frame, text='City', font=labelfont, padx=30, pady=10)
city.grid(row=4, column=0)
city_entry = ttk.Entry(lbl_frame, width=20)
city_entry.grid(row=4, column=1)

state = Label(lbl_frame, text='State', font=labelfont, padx=30, pady=10)
state.grid(row=5, column=0)
state_entry = ttk.Entry(lbl_frame, width=20)
state_entry.grid(row=5, column=1)

zipcode = Label(lbl_frame, text='Zipcode', font=labelfont, padx=30, pady=10)
zipcode.grid(row=6, column=0)
zipcode_entry = ttk.Entry(lbl_frame, width=20)
zipcode_entry.grid(row=6, column=1)

p_name = Label(lbl_frame, text='Product Name', font=labelfont, padx=30, pady=10)
p_name.grid(row=1, column=3)
p_name_entry = ttk.Entry(lbl_frame, width=20)
p_name_entry.grid(row=1, column=4)

p_model = Label(lbl_frame, text='Product Model', font=labelfont, padx=30, pady=10)
p_model.grid(row=2, column=3)
model_entry = ttk.Entry(lbl_frame, width=20)
model_entry.grid(row=2, column=4)

p_serial = Label(lbl_frame, text='Product Serial', font=labelfont, padx=30, pady=10)
p_serial.grid(row=3, column=3)
serial_entry = ttk.Entry(lbl_frame, width=20)
serial_entry.grid(row=3, column=4)

p_ios = Label(lbl_frame, text='Product IOS', font=labelfont, padx=30, pady=10)
p_ios.grid(row=4, column=3)
ios_entry = ttk.Entry(lbl_frame, width=20)
ios_entry.grid(row=4, column=4)

p_family = Label(lbl_frame, text='Product Family', font=labelfont, padx=30, pady=10)
p_family.grid(row=5, column=3)
family_entry = ttk.Entry(lbl_frame, width=20)
family_entry.grid(row=5, column=4)

p_price = Label(lbl_frame, text='Price $', font=labelfont, padx=30, pady=10)
p_price.grid(row=6, column=3)
price_entry = ttk.Entry(lbl_frame, width=20)
price_entry.grid(row=6, column=4)


# define tuple for textbox
ent = (f_entry, l_entry, address_entry, city_entry, state_entry, zipcode_entry)

del_entry = (f_entry, l_entry, address_entry, city_entry, state_entry, zipcode_entry,
                 p_name_entry, model_entry, serial_entry, ios_entry, family_entry, price_entry)

# configure textbox
for cfg in del_entry:
   cfg.config(font=('Arial', 20))


# button click
p_button = ttk.Button(lbl_frame, text='Submit', command=btn, )
p_button.grid(row=7, column=1, columnspan=4, sticky=W+E, pady=30, ipady=10)
p_button.bind("<Return>", btn)

lb = Label(lbl_frame)
lb.grid(row=8, column=3)


root.mainloop()