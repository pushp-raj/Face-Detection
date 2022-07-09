# Name - Pushp Raj 
# University Roll No - 2014791
# Section - c | Class Roll No. - 38
# Semester - 6

from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
# from PIL import Image, ImageTk
from cv2 import imread
from matplotlib import image 
from tkinter import messagebox
import cv2
import numpy as np
# from matplotlib import pyplot as plt


#Main Function of detecting faces

def showimage():
    num = int(t1.get())

    # for image 
    if num == 1:
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Selest Image", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png"), ("All Files", ".*")))
        # img = Image.open(fln)
        img = cv2.imread(fln)
        input_image = img.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0,0, 255), 1)
            # cv2.circle(img, (x, y), (x + w, y + h), (0,0, 255), 1)
        

        output_image=np.concatenate((input_image,img),axis=1)
        cv2.imshow('Selected Image vs Face Detected Image',output_image)
        cv2.waitKey(0)

    # for live image / video 
    elif num == 2:
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        capture = cv2.VideoCapture(0)

        while True:
            _, img = capture.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Live Camera', img)
            k = cv2.waitKey(30) & 0xff
            if k==13:
                break

        capture.release()

    else :
        messagebox.showerror('Error','Input Error !!! Enter Again')




root=Tk()
frm = Frame(root)
frm.pack(side=TOP, pady=30)



# Function responsible for marque animation

def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0):                            #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(500//fps,shift)


#Making a canvas over the root window for academic details 

canvas=Canvas(root)
canvas.place(x=0, y=500)
canvas.pack(fill=BOTH, expand=1)
text_var="This is a Simple Face Detection Software developed by Pushp Raj, Semester - 6th | Section - C | University Roll No. - 2014791 | Class Roll No. - 38 "
text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='black',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 100
height = 100
canvas['width']=width
canvas['height']=height
fps=100  


# GUI Display code 

lbl1=Label(frm, text='Choose Options - ',font=("arial",12,"bold"))
lbl1.place(x=40, y=50)
lbl1.pack(padx=40, pady=50)
lbl2=Label(frm, text='1. Image',font=("arial",12,"bold"))
lbl2.place(x=40, y=75)
lbl3=Label(frm, text='2. Live Image / Video',font=("arial",12,"bold"))
lbl3.place(x=40, y=100)
lbl4=Label(frm, text='Enter your choise',font=("arial",12,"bold"))
lbl4.place(x=40, y=125)
t1=Entry(frm, bd=3,font=("arial",12,"bold"))
t1.pack(padx=200, pady=35)
b1=Button(frm, width=10, text='Enter', bg="grey", command=showimage)
b1.place(x=40, y=160)
b2=Button(frm, width=10, text='Exit', bg="grey", command=lambda : exit())
b2.place(x=40, y=200)


#Root Window

root.title("Face Detection")
root.geometry("500x500")
root.iconbitmap('title.ico')
shift()
root.mainloop()