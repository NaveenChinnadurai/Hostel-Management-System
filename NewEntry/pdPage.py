from tkinter import *
from tkcalendar import *

from Startup import main_frame,con,cur
from eduPage import eduPage

def stringslice(x):
    str1=""
    for i in x:
        if i=="/":
            continue
        else:
            str1=str1+i
    return str1

def generate(x):
    nameval=namein.get()
    dobval=dobin.get()
    str1=stringslice(dobval)
    global genno
    genno=nameval+str1
    genin=Label(x,text=genno, font="arial 12")
    genin.place(x=300,y=90,height=25,width=100)
    
def pdPage():

    pdFrame=Frame(main_frame,bg="#FFFFFF")
    pdFrame.configure(width=685,height=420)
    pdFrame.place(x=150,y=30)

    pdtitle=Label(pdFrame,text="Personal Details",font="curier 17",bg="#FFFFFF")
    pdtitle.place(x=170,y=10)

    name=Label(pdFrame,text="Name :",font="curier 12",bg="#FFFFFF")
    name.place(x=10,y=60)
    global namein
    namein=Entry(pdFrame,font="arial 13")
    namein.place(x=75,y=60,height=25,width=170)    

    dob=Label(pdFrame,text="D.O.B :",font="curier 12",bg="#FFFFFF")
    dob.place(x=310,y=60)
    global dobin
    dobin=DateEntry(pdFrame,font="arial 12")
    dobin.place(x=380,y=60,height=25,width=110)

    genbtn=Button(pdFrame,text="Generate ID",font="curier 10",bg="#FFFFFF",command=lambda:generate(pdFrame))
    genbtn.place(x=200,y=90,height=20,width=80)
    genin=Label(pdFrame,text="Generate PIN", font="arial 10")
    genin.place(x=300,y=90,height=25,width=100)

    sphn=Label(pdFrame,text="Mobile No. :",font="curier 12",bg="#FFFFFF")
    sphn.place(x=20,y=120)
    global phnin
    phnin=Entry(pdFrame,font="arial 13")
    phnin.place(x=107,y=122,height=24,width=130)

    email=Label(pdFrame,text="G-Mail :",font="curier 12",bg="#FFFFFF")
    email.place(x=240,y=120)
    global emailin
    emailin=Entry(pdFrame,font="arial 13")
    emailin.place(x=300,y=120,height=24,width=240)

    height=Label(pdFrame,text="Height :",font="curier 12",bg="#FFFFFF")
    height.place(x=50,y=160)
    global heightin
    heightin=Entry(pdFrame,font="arial 13")
    heightin.place(x=120,y=160,height=25,width=50)

    wight=Label(pdFrame,text="Weight :",font="curier 12",bg="#FFFFFF")
    wight.place(x=180,y=160)
    global weightin
    weightin=Entry(pdFrame,font="arial 13")
    weightin.place(x=250,y=160,height=25,width=50)

    bloodgrp=Label(pdFrame,text="Blood Group :",font="curier 12",bg="#FFFFFF")
    bloodgrp.place(x=310,y=160)
    global bloodmenu
    bloodmenu=StringVar()
    bloodmenu.set("Select")
    bloodin=OptionMenu(pdFrame,bloodmenu,"A+","A-","B+","B-","O+","O-","AB+","AB-")
    bloodin.place(x=420,y=160,height=25,width=70)

    college=Label(pdFrame,text="College :",font="curier 12",bg="#FFFFFF")
    college.place(x=5,y=200)
    global collegein
    collegein=Entry(pdFrame,font="arial 13")
    collegein.place(x=75,y=200,height=25,width=280)

    degdept=Label(pdFrame,text="Deg/Dept :",font="curier 12",bg="#FFFFFF")
    degdept.place(x=360,y=200)
    global degin
    degin=Entry(pdFrame,font="arial 13")
    degin.place(x=445,y=200,height=25,width=100)

    fname=Label(pdFrame,text="Father's Name :",font="curier 12",bg="#FFFFFF")
    fname.place(x=10,y=240)
    global fnamein
    fnamein=Entry(pdFrame,font="arial 13")
    fnamein.place(x=130,y=240,height=25,width=180)

    fphn=Label(pdFrame,text="Mobile No. :",font="curier 12",bg="#FFFFFF")
    fphn.place(x=320,y=240)
    global fphnin
    fphnin=Entry(pdFrame,font="arial 13")
    fphnin.place(x=410,y=240,height=25,width=130)

    mname=Label(pdFrame,text="Mother's Name :",font="curier 12",bg="#FFFFFF")
    mname.place(x=10,y=280)
    global mnamein
    mnamein=Entry(pdFrame,font="arial 13")
    mnamein.place(x=130,y=280,height=25,width=180)

    mphn=Label(pdFrame,text="Mobile No. :",font="curier 12",bg="#FFFFFF")
    mphn.place(x=320,y=280)
    global mphnin
    mphnin=Entry(pdFrame,font="arial 13")
    mphnin.place(x=410,y=280,height=25,width=130)

    dt=Label(pdFrame,text="District :",font="curier 12",bg="#FFFFFF")
    dt.place(x=30,y=320)
    global dtin
    dtin=Entry(pdFrame,font="arial 13")
    dtin.place(x=100,y=320,height=24,width=150)

    datej=Label(pdFrame,text="Date Joined :",font="curier 12",bg="#FFFFFF")
    datej.place(x=290,y=320)
    global datejin
    datejin=DateEntry(pdFrame,font="arial 12")
    datejin.place(x=400,y=320,height=25,width=100)

    global int1
    int1=IntVar()
    global int2
    int2=IntVar()

    chkbox1=Checkbutton(pdFrame,text="Above Details Are \nCorrect in my knowledge",font="curier 10",bg="#FFFFFF",onvalue=1,offvalue=0,variable=int1)
    chkbox1.configure(justify=LEFT)
    chkbox1.place(x=80,y=350)

    chkbox2=Checkbutton(pdFrame,text="Accept Rules and\nRegulations",font="curier 10",bg="#FFFFFF",onvalue=1,offvalue=0,variable=int2)
    chkbox2.place(x=280,y=350)

    savebtn=Button(pdFrame,text="Save And Next",font="curier 12",bg="#FFFFFF",command=pdsave)
    savebtn.place(x=410,y=380)
    savebtn.configure(state=DISABLED)

    chkbox1.configure(command=lambda:check(savebtn))
    chkbox2.configure(command=lambda:check(savebtn))

def check(s):
    s1=int1.get()
    s2=int2.get()
    if s1==1:
        if s2==1:
            s.configure(state=NORMAL)
        else:
            s.configure(state=DISABLED)
    else:
        s.configure(state=DISABLED)

def pdsave():
    eduPage()
    nameval=namein.get()
    dobval=dobin.get()
    bloodval=bloodmenu.get()
    phnval=phnin.get()
    emailval=emailin.get()
    heightval=heightin.get()
    weightval=weightin.get()
    collegeval=collegein.get()
    degval=degin.get()
    fnameval=fnamein.get()
    fphnval=fphnin.get()
    mnameval=mnamein.get()
    mphnval=mphnin.get()
    dtval=dtin.get()
    datejnval=datejin.get()

    value1=(nameval,dobval,genno,emailval,phnval,bloodval,heightval,weightval,dtval)
    value2=(fnameval,fphnval,mnameval,mphnval,dtval)

    cur.execute("INSERT IGNORE INTO PersonalInfo VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",value1)
    cur.execute("INSERT IGNORE INTO Parent_Details VALUES(%s,%s,%s,%s,%s)",value2)

    con.commit()