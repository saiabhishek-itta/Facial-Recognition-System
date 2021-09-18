import tkinter as tk
from tkinter import Tk, ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time

def adminpanel():
    if(tkpassword.get()=="" or tkusername.get()=="" ):
        tklblerror.config(text="Enter Credentials!")
        print("Admin Credentials not entered to login")
    elif(tkpassword.get()=="admin" and tkusername.get()=="admin"):
        admin=tk.Tk()
        admin.geometry("1080x620")
        admin.resizable(True,False)
        admin.title("ADMIN PANEL")
        admin.configure(background='#262523')
        window.destroy()
        admin.mainloop()
    else:
        tklblerror.config(text="ID or Password not found for Admin")
        print("Admin login failed")

def facultypanel():
    if(tkpassword.get()=="" or tkusername.get()=="" ):
        tklblerror.config(text="Enter Credentials!")
        print("Faculty Credentials not entered to login")
    elif(tkpassword.get()=="faculty" and tkusername.get()=="faculty"):
        faculty=tk.Tk()
        faculty.mainloop()
    else:
        tklblerror.config(text="ID or Password not found for Faculty")
        print("Faculty login failed")
 

########################################################################################################################################
#window---> mainscreen


def clearusername():
    tkusername.delete(first=0,last=10)
def clearpassword():
    tkpassword.delete(first=0,last=18)


window = tk.Tk()
window.geometry("1080x620")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#262523')


tklblusername = tk.Label(window, text="Enter Employee ID :", width=20, fg="black", height=1, font=('times', 15, ' bold '))
tklblusername.place(x=20, y=210)

tklblpassword = tk.Label(window, text="Enter Password    :", width=20, fg="black",  height=1, font=('times', 15, ' bold '))
tklblpassword.place(x=20, y=310)

tkusername = tk.Entry(window, width=20, bg="white", fg="red", font=('times', 25, ' bold '))
tkusername.place(x=300, y=210)

tkpassword = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 25, ' bold '))
tkpassword.place(x=300, y=310)

tkclearusernamebtn = tk.Button(window, text="Clear", command=clearusername  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
tkclearusernamebtn.place(x=700, y=215)

tkclearpasswordbtn = tk.Button(window, text="Clear", command=clearpassword  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
tkclearpasswordbtn.place(x=700, y=315)


tkfacultyloginbtn = tk.Button(window, text="Faculty", command=facultypanel  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
tkfacultyloginbtn.place(x=500, y=415)

tkadminloginbtn = tk.Button(window, text="Admin", command=adminpanel  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
tkadminloginbtn.place(x=350, y=415)

tklblerror = tk.Label(window, text="",bg="#262523", width=80, fg="red",  height=1, font=('times', 15, ' bold '))
tklblerror.place(x=5, y=495)

#window.configure(menu=menubar)
window.mainloop()

