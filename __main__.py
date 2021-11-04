"""
Invokes django-admin when the django module is run as a script.

Example: python -m django check
"""

import webbrowser
import tkinter as tk
from django.core import management
from tkinter import Button, Image, PhotoImage, Tk


import webbrowser
# importing all files from tkinter module
# from tkinter import *

# creating root
window = tk.Tk()
# setting GUI title
window.title("https://www.etenders.gov.za/")
# setting GUI geometry
window.geometry("660x660")


# function to open linkedin in browser
def home():
    webbrowser.open("home")
# function to open facebook in browser
def about_us():
    webbrowser.open("About Us")
# function to open twitter in browser
def register():
    webbrowser.open("Register")
# function to open youtube in browser
def apply():
    webbrowser.open("Apply")
# function to open whatsapp web in browser
def updateApplication():
    webbrowser.open("Update Application")
# function to open instagram in browser
def submitApplication():
    webbrowser.open("Submit Application")
# function to open gmail in browser
def cancelApplication():
    webbrowser.open("Cancel Application")
    
def tenderStatus():
    webbrowser.open("Tender Status")

def awards():
    webbrowser.open("Awards")
    



bg = tk.PhotoImage(file = "CoatOfArm.png") 
label1 = tk.Label(window, image = bg)
label1.place(x = 200, y = 200)


background = tk.PhotoImage(file = "AfricanFlag.png")
label = tk.Label(text = "Government Public Procurement Submition Portal",
                    font = ("Arial Black", 28),
                    fg = "Black", bg = "#F4A460")
            
label2 = tk.Label(window, text = "Welcome e-Tender Submission Portal")
label.pack()
label2.bind(label2)

button1 = Button(window, text = "Home", command = home, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)
button3 = Button(window, text = "Apply",command = apply, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)
button4 = Button(window, text = "Register",command = register, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)
button5 = Button(window, text = "Update Application",command = updateApplication, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)
button6 = Button(window, text = "Submit Application",command = submitApplication, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)
button7 = Button(window, text = "Cancel Application",command = cancelApplication, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)
button8 = Button(window, text = "Tender Status",command = tenderStatus, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)
button9 = Button(window, text = "Awards",command = awards, font = ("Ariel",8), width = 12, bg = "#FFD700").pack(side = tk.LEFT)

window.mainloop()



    
        
        # subject = Button(window, text = "Government Central Public Procurement Submition Portal")
        # subject.pack()
        
    

    
# if __name__ == "__main__":
   
    
    
            








































































# window = tk.Tk()
# entry = tk.Entry()
# greeting = tk.Label(text = "Hello Tkinter", fg = "Pink", bg = "Blue", width = 20, height = 6)
# greeting.pack()
# entry.pack()
# name = entry.get()
# entry.delete(1)


# button = Button(text = "Python Rocks!", foreground = "Grey", background = "Brown", width = 10, height = 5)
# # button.grid(row = 250, column =300 )


# window.mainloop()


# if __name__ == "__main__":
#     management.execute_from_command_line()
