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

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }

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

######################################################################################################################################################

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
        print(ID)
    except:
        #mess._show(title='No New Images Found', message='Please Take Images to proceed with profile saving!')
        adminpanel.message.configure(text='Please take images first!!!')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profile Saved Successfully"
    adminpanel.message1.configure(text=res)
    adminpanel.message.configure(text='Total Registrations till now  : ' + str(ID[0]))



def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.','Student ID','Student NAME']
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
        tksavebtn = tk.Button(admin, text="Save Profile",command=TrainImages,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
        tksavebtn.place(x=700, y=415)
        adminpanel.message = tk.Label(admin, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
        adminpanel.message.place(x=7, y=450)
        adminpanel.message1 = tk.Label(admin, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('times', 16, ' bold '))
        adminpanel.message1.place(x=7, y=550)
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
        facultypanel.tv= ttk.Treeview(admin,height =13,columns = ('name','date','time'))
        facultypanel.tv.column('#0',width=82)
        facultypanel.tv.column('name',width=130)
        facultypanel.tv.column('date',width=133)
        facultypanel.tv.column('time',width=133)
        facultypanel.tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
        facultypanel.tv.heading('#0',text ='ID')
        facultypanel.tv.heading('name',text ='NAME')
        facultypanel.tv.heading('date',text ='DATE')
        facultypanel.tv.heading('time',text ='TIME')
        tknewregistrationbtn = tk.Button(admin, text="Take Attendence",command=TrackImages,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
        tknewregistrationbtn.place(x=700, y=315)
        window.destroy()
        admin.mainloop()
    else:
        tklblerror.config(text="ID or Password not found for Faculty")
        print("Faculty login failed")

def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in facultypanel.tv.get_children():
        facultypanel.tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml")
    else:
        mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv")
    else:
        mess._show(title='Details Missing', message='Students details are missing, please check!')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Taking Attendance', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if exists:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    facultypanel.tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()
 

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

