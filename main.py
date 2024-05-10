import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.title('Employees Management System')
app.geometry('1200x520')
app.config(bg='#161C25')
app.resizable(False,False)

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 12, 'bold')

def add_to_treeview():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0,END)
    name_entry.delete(0,END)
    variable1.set('Male')
    position_entry.delete(0,END)
    address_entry.delete(0,END)
    contact_entry.delete(0,END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0,row[0])
        name_entry.insert(0,row[1])
        variable1.set(row[2])
        position_entry.insert(0,row[3])
        address_entry.insert(0,row[4])
        contact_entry.insert(0,row[5])
    else:
        pass

def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose employee to delete.')
    else:
        id = id_entry.get()
        database.delete_employee(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Employee has been deleted.')

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Choose employee to update.')
    else:
        id = id_entry.get()
        name = name_entry.get()
        gender = variable1.get()
        position = position_entry.get()
        address = address_entry.get()
        contact = contact_entry.get()
        database.update_employee(name,gender,position,address,contact,id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Employee has been updated.')

def insert():
    id = id_entry.get()
    name = name_entry.get()
    gender = variable1.get()
    position = position_entry.get()
    address = address_entry.get()
    contact = contact_entry.get()
    if not (id and name and gender and position and address and contact):
        messagebox.showerror('Error', 'Enter all fields.')
    elif database.id_exists(id):
        messagebox.showerror('Error', 'ID already exists.')
    else:
        database.insert_employee(id,name,gender,position,address,contact)
        add_to_treeview()
        clear()
        messagebox.showinfo('SUccess', 'Employee has been inserted.')

id_label = customtkinter.CTkLabel(app, font=font1,text='ID:',text_color='#fff', bg_color='#161C25')
id_label.place(x=20,y=20)

id_entry = customtkinter.CTkEntry(app, font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
id_entry.place(x=110,y=20)

name_label = customtkinter.CTkLabel(app, font=font1,text='Name:',text_color='#fff',bg_color='#161C25')
name_label.place(x=20,y=80)

name_entry = customtkinter.CTkEntry(app, font=font1,text_color='#000',fg_color='#fff',bg_color='#0C9295',border_width=2,width=180)
name_entry.place(x=110,y=80)

position_label = customtkinter.CTkLabel(app, font=font1,text='Position:',text_color='#fff',bg_color='#161C25')
position_label.place(x=20,y=140)

position_entry = customtkinter.CTkEntry(app, font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
position_entry.place(x=110,y=140)

gender_label = customtkinter.CTkLabel(app, font=font1,text='Gender:',text_color='#fff',bg_color='#161C25')
gender_label.place(x=20,y=200)

options = ['Male', 'Female']
variable1 = StringVar()

gender_options = customtkinter.CTkComboBox(app,font=font1,text_color='#000',fg_color='#fff',dropdown_hover_color='#0C9295',button_color='#0C9295',button_hover_color='#0C9295',border_color='#0C9295',width=180,variable=variable1,values=options,state='readonly')
gender_options.set('Male')
gender_options.place(x=110,y=200)

address_label = customtkinter.CTkLabel(app, font=font1,text='Address:',text_color='#fff',bg_color='#161C25')
address_label.place(x=20,y=260)

address_entry = customtkinter.CTkEntry(app, font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
address_entry.place(x=110,y=260)

contact_label = customtkinter.CTkLabel(app, font=font1,text='Contact:',text_color='#fff',bg_color='#161C25')
contact_label.place(x=20,y=320)

contact_entry = customtkinter.CTkEntry(app, font=font1,text_color='#000',fg_color='#fff',border_color='#0C9295',border_width=2,width=180)
contact_entry.place(x=110,y=320)

add_button = customtkinter.CTkButton(app,command=insert,font=font1,text_color='#fff',text='Add Employee',fg_color='#05A312',hover_color='#00850B',bg_color='#161C25',cursor='hand2',corner_radius=15,width=260)
add_button.place(x=20,y=370)

clear_button = customtkinter.CTkButton(app,command=lambda:clear(True),font=font1,text_color='#fff',text='New Employee',fg_color='#161C25',hover_color='#00850B',bg_color='#161C25',border_color='#F15704',border_width=2,cursor='hand2',corner_radius=15,width=260)
clear_button.place(x=20,y=430)

update_button = customtkinter.CTkButton(app,command=update,font=font1,text_color='#fff',text='Update Employee',fg_color='#161C25',hover_color='#00850B',bg_color='#161C25',border_color='#F15704',border_width=2,cursor='hand2',corner_radius=15,width=260)
update_button.place(x=300,y=430)

delete_button = customtkinter.CTkButton(app,command=delete,font=font1,text_color='#fff',text='Delete Employee',fg_color='#E40404',hover_color='#AE0000',bg_color='#161C25',border_color='#E40404',border_width=2,cursor='hand2',corner_radius=15,width=260)
delete_button.place(x=580,y=430)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview',font=font2,foreground='#fff',background='#000',fieldbackground='#313837')
style.map('Treeview',background=[('selected','#1A8F2D')])

tree = ttk.Treeview(app,height=15)

tree['columns'] = ('ID', 'Name', 'Gender', 'Position', 'Address', 'Contact')

tree.column('#0', width=0, stretch=tk.NO) # Hide the default first column
tree.column('ID', anchor=tk.CENTER, width=140)
tree.column('Name', anchor=tk.CENTER, width=140)
tree.column('Gender', anchor=tk.CENTER, width=140)
tree.column('Position', anchor=tk.CENTER, width=140)
tree.column('Address', anchor=tk.CENTER, width=140)
tree.column('Contact', anchor=tk.CENTER, width=140)

tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Gender', text='Gender')
tree.heading('Position', text='Position')
tree.heading('Address', text='Address')
tree.heading('Contact', text='Contact')

tree.place(x=300,y=20)

tree.bind('<ButtonRelease>', display_data)

add_to_treeview()

app.mainloop()

