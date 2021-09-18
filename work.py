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

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='File Not Found', message='Cascade File Not Found!!!')
        window.destroy()

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.','ID','NAME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns)
            serial = 1
        csvFile1.close()
    Id = (adminpanel.txt.get())
    name = (adminpanel.txt2.get())
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('Taking Images', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Taken for ID : " + Id
        row = [serial, Id, name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        adminpanel.message.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            adminpanel.message.configure(text=res)

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
        adminpanel.txt = tk.Entry(admin,width=32 ,fg="black",font=('times', 15, ' bold '))
        adminpanel.txt.place(x=30, y=88)
        adminpanel.txt2 = tk.Entry(admin,width=32 ,fg="black",font=('times', 15, ' bold ')  )
        adminpanel.txt2.place(x=30, y=173)
        tknewregistrationbtn = tk.Button(admin, text="Take Images",command=TakeImages,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
        tknewregistrationbtn.place(x=700, y=315)
        adminpanel.message = tk.Label(admin, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
        adminpanel.message.place(x=7, y=450)
        admin.mainloop()
    else:
        tklblerror.config(text="ID or Password not found for Admin")
        print("Admin login failed")







#########################################################################################################################################
def facultypanel():
    if(tkpassword.get()=="" or tkusername.get()=="" ):
        tklblerror.config(text="Enter Credentials!")
        print("Faculty Credentials not entered to login")
    elif(tkpassword.get()=="faculty" and tkusername.get()=="faculty"):
        admin=tk.Tk()
        admin.geometry("1080x620")
        admin.resizable(True,False)
        admin.title("FACULTY PANEL")
        admin.configure(background='#262523')
        window.destroy()
        admin.mainloop()
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

