#This is a security system installed at the entrance of an apartment

# Import the required libraries
import tkinter as tk
import os
import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

#tkinter window
root=tk.Tk()
# Set the title of the tkinter window
root.title("Security Gate")
# Set the size of the tkinter window
root.geometry("1200x700")

s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview',rowheight=30)

#Heading label
lb=tk.Label(root,text="SECURITY GATE",font=("Arial",20))
lb.place(x=500,y=15)

#logo
logo=Image.open('logo.jpg')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.place(x=400,y=70)

#Define function face_detection()
def face_detection():
    os.system('detect.py')

#Define function display_records()
def display_records():
    #Create a new tkinter window
    new = Toplevel(root)
    new.geometry("1000x700")
    new.title("Records")

    # Add a Treeview widget
    tree = ttk.Treeview(new, column=("c1", "c2", "c3"), show='headings',height=20)

    tree.column("# 1", anchor=CENTER, width=170)
    tree.heading("# 1", text="Name")
    tree.column("# 2", anchor=CENTER, width=170)
    tree.heading("# 2", text="Time")
    tree.column("# 3", anchor=CENTER, width=170)
    tree.heading("# 3", text="Date")

    #Connect with database
    my_connect = mysql.connector.connect(host="localhost", user="root", passwd="Hookrux@912", database="records")
    my_conn = my_connect.cursor()

    #Execute query and fetch results
    my_conn.execute("Select * from security_database")
    table = my_conn.fetchall()

    # Insert the data in Treeview widget
    for row in table:
        tree.insert("", 'end', text='1', values=row)

    tree.pack()

#Define function details()
def details():
    # Create a new tkinter window
    nw = Toplevel(root)
    nw.geometry("1000x700")
    nw.title("Resident Details")

    # Add a Treeview widget
    tree = ttk.Treeview(nw,column=("c1", "c2", "c3"), show='headings',height=20)

    tree.column("# 1", anchor=CENTER, width=170)
    tree.heading("# 1", text="Flat Number")
    tree.column("# 2", anchor=CENTER, width=170)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER, width=170)
    tree.heading("# 3", text="Phone Number")

    # Connect with database
    my_connect = mysql.connector.connect(host="localhost", user="root", passwd="Hookrux@912", database="records")
    my_conn = my_connect.cursor()

    # Execute query and fetch results
    my_conn.execute("Select * from residents_details")
    table = my_conn.fetchall()

    # Insert the data in Treeview widget
    for row in table:
        tree.insert("", 'end', text='1', values=row)

    tree.pack()


#Buttons
detect_btn=tk.Button(root,text="Get yourself verified",command=lambda:face_detection(),font=("Raleway",15),bg="brown",fg="white",height=2,width=20,)
detect_btn.place(x=200,y=450)

details_btn=tk.Button(root,text="Resident Details",command=lambda:details(),font=("Raleway",15),bg="green",fg="white",height=2,width=20)
details_btn.place(x=450,y=450)

data_btn=tk.Button(root,text="Entry Records",command=lambda:display_records(),font=("Raleway",15),bg="brown",fg="white",height=2,width=20)
data_btn.place(x=700,y=450)

root.mainloop()