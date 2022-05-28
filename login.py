#This is the login page to ensure the safety of the security gate

# Import the required libraries
import tkinter as tk
import os
from PIL import Image,ImageTk

#tkinter window
gi=tk.Tk()
# Set the title of the tkinter window
gi.title("Login Page")
# Set the size of the tkinter window
gi.geometry("1200x700")

image = Image.open("login.jpg")

# Resize the image using resize() method
resize_image = image.resize((270, 340))

img = ImageTk.PhotoImage(resize_image)

panel = tk.Label(gi, image = img)
panel.place(x=750,y=100)


#Define function security_gate()
def security_gate():
    User=Username.get()
    Pass=password.get()
    if(User=="sejalgangwar" and Pass=="Hookrux@912"):
        gi.destroy()
        os.system('app.py')
    else:
        err=tk.Label(gi,text="Incorrect Username or Password!!",font=("Arial",18))
        err.place(x=400,y=500)

#Heading label
lb=tk.Label(gi,text="LOGIN PAGE",font=("Arial",25))
lb.place(x=500,y=20)

#username label and text entry box
lblfrstrow = tk.Label(gi, text="USERNAME",font=("Cambria",15) )
lblfrstrow.place(x=360, y=150)

Username = tk.Entry(gi, width=35,font=("Cambria",15))
Username.place(x=500, y=150, width=200,height=40)

#password label and password entry box
lblsecrow = tk.Label(gi, text="PASSWORD",font=("Cambria",15))
lblsecrow.place(x=360, y=250)

password = tk.Entry(gi, width=35,font=("Cambria",15),show="*")
password.place(x=500, y=250, width=200,height=40)

#Login button
loginbtn = tk.Button(gi,text="Login",font="Raleway",bg="green",fg="white",height=2,width=20, command=lambda:security_gate())
loginbtn.place(x=500, y=400)

gi.mainloop()