from tkinter import *

from Attendance.attHistory import ahPage
from Startup import main_frame
from Attendance.roomVacancyPage import rvPage
from Home import HomePage
from Startup import window

def Attendence():
    atFrame=Frame(main_frame)
    atFrame.configure(width=700,height=450)
    atFrame.place(x=0,y=0)

    title=Label(atFrame,text="Attendence Register",font="curier 18",fg="#000000")
    title.place(x=270,y=10)

    dailyattendence=Button(atFrame,text="Today's Attendence Entry",font="curier 14")
    dailyattendence.place(x=255,y=150)

    history=Button(atFrame,text="Attendence History",font="curier 14",command=lambda:ahPage(atFrame))
    history.place(x=280,y=200)

    vacant=Button(atFrame,text="Room Vaccancy",font="curier 14",command=lambda:rvPage(atFrame))
    vacant.place(x=290,y=250)

    homebtn=Button(atFrame,text="Home",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=HomePage)
    homebtn.place(x=20,y=410)

    exitbtn=Button(atFrame,text="EXIT",font="Courier 13 bold",fg="#000000",bg="#C0C0C0",width=5,height=1,command=window.quit)
    exitbtn.place(x=640,y=415,width=50,height=25)
