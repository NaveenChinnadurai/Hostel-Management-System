from tkinter import *

from AddressPage import addPage
from Startup import main_frame,con,cur
from pdPage import genno
#For educational Details Page

def eduPage():

    eduFrame=Frame(main_frame,bg="#FFFFFF")
    eduFrame.configure(width=685,height=420)
    eduFrame.place(x=150,y=30)

    edutitle=Label(eduFrame,text="Educational Details",font="curier 17",bg="#FFFFFF")
    edutitle.place(x=160,y=10)

    college=Label(eduFrame,text="College Name :",font="curier 13",bg="#FFFFFF")
    college.place(x=10,y=60)
    global collegein
    collegein=Entry(eduFrame,font="arial 13")
    collegein.place(x=130,y=60,width=300,height=25)

    colcode=Label(eduFrame,text="College Code :",font="curier 13",bg="#FFFFFF")
    colcode.place(x=10,y=100)
    global colin
    colin=Entry(eduFrame,font="courier 13")
    colin.place(x=130,y=100,width=60,height=25)

    deg=Label(eduFrame,text="Degree :",font="curier 13",bg="#FFFFFF")
    deg.place(x=50,y=137)
    global degmenu
    degmenu=StringVar()
    degmenu.set("")
    degin=OptionMenu(eduFrame,degmenu,"B.E","B.Tech","B.Pharm","D.Pharm","M.E")
    degin.place(x=125,y=135,width=50,height=25)

    dept=Label(eduFrame,text="Department :",font="curier 13",bg="#FFFFFF")
    dept.place(x=190,y=137)
    global deptmenu
    deptmenu=StringVar()
    deptmenu.set("")
    deptin=OptionMenu(eduFrame,deptmenu,"CSE","ECE","EEE","Mech","Civil","IT","AI & DS","ME",)
    deptin.place(x=295,y=135,width=60,height=25)

    yr=Label(eduFrame,text="Year :",font="curier 13",bg="#FFFFFF")
    yr.place(x=370,y=137)
    global yrmenu
    yrmenu=StringVar()
    yrmenu.set("")
    yrin=OptionMenu(eduFrame,yrmenu,"I","II","III","IV")
    yrin.place(x=430,y=135,width=70,height=25)

    regno=Label(eduFrame,text="Register No. :",font="curier 13",bg="#FFFFFF")
    regno.place(x=10,y=172)
    global regin
    regin=Entry(eduFrame,font="arial 13")
    regin.place(x=120,y=172,width=150,height=25)

    rolno=Label(eduFrame,text="Roll No. :",font="curier 13",bg="#FFFFFF")
    rolno.place(x=280,y=172)
    global rolin
    rolin=Entry(eduFrame,font="arial 13")
    rolin.place(x=355,y=171,width=120,height=25)

    passout=Label(eduFrame,text="Year of Passing :",font="curier 13",bg="#FFFFFF")
    passout.place(x=10,y=210)    
    global passoutin
    passoutin=Entry(eduFrame,font="curier 13")
    passoutin.place(x=150,y=210,width=60,height=25)
    
    batch=Label(eduFrame,text="Batch :",font="curier 13",bg="#FFFFFF")
    batch.place(x=230,y=210)
    global batchin
    batchin=Entry(eduFrame,font="arial 13")
    batchin.place(x=290,y=210,width=100,height=25)

    global int3
    int3=IntVar()
    global int4
    int4=IntVar()

    admission=Label(eduFrame,text="Admission Type :",font="curier 13",bg="#FFFFFF")
    admission.place(x=10,y=250)
    typein1=Checkbutton(eduFrame,text="Govt.Quota",font="arial 13",bg="#FFFFFF",offvalue=0,onvalue=1,variable=int3)
    typein1.place(x=150,y=248)
    typein2=Checkbutton(eduFrame,text="Management Quota",font="arial 13",bg="#FFFFFF",offvalue=0,onvalue=1,variable=int4)
    typein2.place(x=270,y=248)

    typein1.configure(command=lambda:checkbtn(typein2,st,cno,cnoin))
    typein2.configure(command=lambda:checkbtn(typein1,st,cno,cnoin))

    st=Label(eduFrame,text="If Government Quota,",font="curier 13",bg="#FFFFFF")
    st.place(x=20,y=285)

    cno=Label(eduFrame,text="TNEA Application No. :",font="curier 13",bg="#FFFFFF")
    cno.place(x=50,y=315)
    global cnoin
    cnoin=Entry(eduFrame,font="arial 13")
    cnoin.place(x=230,y=315,width=150,height=25)

    savebtn=Button(eduFrame,text="Save And Next",font="curier 13",bg="#FFFFFF",command=edusave)
    savebtn.place(x=410,y=360)

def edusave():
    addPage()
    collegeval=collegein.get()
    colval=colin.get()
    degval=degmenu.get()
    deptval=deptmenu.get()
    yrval=yrmenu.get()
    regval=regin.get()
    rolval=rolin.get()
    passoutval=passoutin.get()
    batchval=batchin.get()
    cnoval=cnoin.get()
    
    if admtyp=="Management Quota":
        cnoval="-"
    value1=(genno,collegeval,colval,degval,deptval,yrval,regval,rolval,passoutval,batchval,admtyp,cnoval)

    cur.execute("INSERT IGNORE INTO Educational_Details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",value1)

    con.commit()

def checkbtn(x,a,b,c):
    s1=int3.get()
    s2=int4.get()
    global admtyp
    admtyp=""
    if s1==1 or s2==1:
        x.configure(state=DISABLED)
    else:
        x.configure(state=NORMAL)
    if s1==1:
        admtyp="Govt. Quota"
        a.configure(state=NORMAL)
        b.configure(state=NORMAL)
        c.configure(state=NORMAL)
    if s2==1:
        admtyp="Management Quota"
        a.configure(state=DISABLED)
        b.configure(state=DISABLED)
        c.configure(state=DISABLED)