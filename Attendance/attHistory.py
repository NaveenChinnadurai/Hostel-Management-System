from tkinter import *
from tkcalendar import *

from AttendancePage import Attendence
from Home import HomePage
from Startup import window
def ahPage(x):
    ahFrame=Frame(x)
    ahFrame.configure(width=700,height=450)
    ahFrame.place(x=0,y=0)

    title1=Label(ahFrame,text="Attendence History",font="curier 17 bold")
    title1.place(x=190,y=50)

    selectTxt=Label(ahFrame,text="Select Date:",font="curier 15")
    selectTxt.place(x=250,y=150) 
    selectdate=DateEntry(ahFrame,font="arial 14")
    selectdate.place(x=370,y=152,width=100,height=25)   

    searchbtn1=Button(ahFrame,text="View Attendence",font="curier 12")
    searchbtn1.place(x=300,y=190,height=25,width=130)

    sattend=Label(ahFrame,text="View Attendence Details of Specific Student",font="curier 14")
    sattend.place(x=190,y=250)

    rolin=Entry(ahFrame,font="arial 13")
    rolin.place(x=280,y=280)
    rolin.insert(0,"Enter Roll No.")

    searchbtn2=Button(ahFrame,text="View",font="curier 12")
    searchbtn2.place(x=350,y=310,height=25)

    backbtn=Button(ahFrame,text="Back",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=lambda:Attendence())
    backbtn.place(x=10,y=15,height=20)

    homebtn=Button(ahFrame,text="Home",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=lambda:HomePage())
    homebtn.place(x=10,y=410)  

    exitbtn=Button(ahFrame,text="EXIT",font="Courier 13 bold",fg="#000000",bg="#C0C0C0",width=5,height=1,command=window.quit)
    exitbtn.place(x=640,y=415,width=50,height=25)
