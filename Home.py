from tkinter import *

from Newentry import NewEntry
from vProfilePage import viewProfile
from AttendancePage import Attendence
from OutPassPage import OutPass
from SummaryPage import Summary

from Startup import main_frame,window

def HomePage():
    
    homeFrame=Frame(main_frame,bg="#FFFFFF")
    homeFrame.configure(width=700,height=450)
    homeFrame.place(x=0,y=0)

    t1=Label(homeFrame,text="Hostel Management System",font="ar 20 bold",fg="#FF0000",bg="#FFFFFF")
    t1.place(x=160,y=40) 

    button1=Button(homeFrame,text="New Entry",font="16",fg="#000000",bg="#C0C0C0",width=17,command=lambda:NewEntry())
    button1.place(x=250,y=120)

    button2=Button(homeFrame,text="View Profile",font="16",fg="#000000",bg="#C0C0C0",width=17,command=lambda:viewProfile())
    button2.place(x=250,y=170)

    button3=Button(homeFrame,text="Attendence Register",font="16",fg="#000000",bg="#C0C0C0",width=17,command=lambda:Attendence())
    button3.place(x=250,y=220)

    button4=Button(homeFrame,text="GatePass Register",font="16",fg="#000000",bg="#C0C0C0",width=17,command=lambda:OutPass())
    button4.place(x=250,y=270)

    button5=Button(homeFrame,text="Hostel Details",font="16",fg="#000000",bg="#C0C0C0",width=17,command=lambda:Summary())
    button5.place(x=250,y=320)

    button6=Button(homeFrame,text="EXIT",font="Courier 13 bold",fg="#000000",bg="#C0C0C0",width=5,height=1,command=window.quit)
    button6.place(x=640,y=415,width=50,height=25)

    button7=Button(homeFrame,text="Administrator Login",font="Californian 10 bold",fg="#000000",bg="#C0C0C0")
    button7.place(x=20,y=410)
