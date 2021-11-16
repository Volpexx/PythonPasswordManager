#Import the required Libraries
from tkinter import *
import os, sys
from tkinter import ttk
from tkinter import simpledialog
import tkinter

#variables
mastersetpressed = 0
masterpass = {}

#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of Tkinter frame
win.geometry("400x400")

#define commands
def open_login():
   login = simpledialog.askstring("Password", "Please Enter Your Password") 
   with open('login.txt', 'r', encoding='u4f-8') as mPassword:
      mPasswordMatch = (mPassword.read())
      print(mPasswordMatch)
      if str(login) == mPasswordMatch:
         main = Tk()


      
#Create a button in the main Window to open the password and login pages
Label(win, text=" Welcome to Anthony's Password Manager", font=('Helvetica 14 bold')).pack(pady=20)
ttk.Button(win, text= "Log In", command= open_login).pack()
ttk.Button(win,text= "Close", command=exit).pack()


win.mainloop()
