from tkinter import *
from PIL import *
from tkcalendar import *

root=Tk()
root.geometry("700x450")

def pdFrame():
    pdFrame=Frame(root,bg="#87cefa")
    pdFrame.pack(side=RIGHT)
    pdFrame.configure(width=685,height=420)
    pdFrame.place(x=150,y=30)

    pdtitle=Label(root,text="Personal Information",font="curier 17",bg="#87cefa")
    pdtitle.place(x=300,y=30)

    name=Label(pdFrame,text="Name :",font="curier 12",bg="#87cefa")
    name.place(x=2,y=60)
    namein=Entry(pdFrame,font="arial 13")
    namein.place(x=65,y=60,height=25,width=170)

    dob=Label(pdFrame,text="D.O.B :",font="curier 12",bg="#87cefa")
    dob.place(x=240,y=60)
    dobin=DateEntry(pdFrame,font="arial 12")
    dobin.place(x=300,y=60,height=25,width=85)

    bloodgrp=Label(pdFrame,text="Blood Group :",font="curier 12",bg="#87cefa")
    bloodgrp.place(x=390,y=60)
    bloodin=Entry(pdFrame,font="arial 13")
    bloodin.place(x=495,y=60,height=25,width=50)

    sphn=Label(pdFrame,text="Mobile No. :",font="curier 12",bg="#87cefa")
    sphn.place(x=20,y=100)
    phnin=Entry(pdFrame,font="arial 13")
    phnin.place(x=107,y=102,height=24,width=130)

    email=Label(pdFrame,text="G-Mail :",font="curier 12",bg="#87cefa")
    email.place(x=240,y=100)
    emailin=Entry(pdFrame,font="arial 13")
    emailin.place(x=300,y=100,height=24,width=240)

    height=Label(pdFrame,text="Height :",font="curier 12",bg="#87cefa")
    height.place(x=60,y=140)
    heightin=Entry(pdFrame,font="arial 13")
    heightin.place(x=125,y=140,height=25,width=60)

    wight=Label(pdFrame,text="Weight :",font="curier 12",bg="#87cefa")
    wight.place(x=200,y=140)
    weightin=Entry(pdFrame,font="arial 13")
    weightin.place(x=270,y=140,height=25,width=60)

    college=Label(pdFrame,text="College :",font="curier 12",bg="#87cefa")
    college.place(x=20,y=180)
    collegein=Entry(pdFrame,font="arial 13")
    collegein.place(x=95,y=180,height=25,width=300)

    yr=Label(pdFrame,text="Year :",font="curier 12",bg="#87cefa")
    yr.place(x=400,y=180)
    yrin=Entry(pdFrame,font="arial 13")
    yrin.place(x=450,y=180,height=25,width=60)

    """
    brn=Label(pdFrame,text="Branch :",font="curier 12",bg="#87cefa")
    brn.place(x=270,y=140)
    brnin=Entry(pdFrame,font="arial 13")
    brnin.place(x=330,y=140,height=25,width=45)
    brnval=brnin
    
    dept=Label(pdFrame,text="Department :",font="curier 12",bg="#87cefa")
    dept.place(x=374,y=140)
    deptin=Entry(pdFrame,font="arial 13")
    deptin.place(x=473,y=138,height=27,width=70)
    deptval=deptin
   
    regno=Label(pdFrame,text="Register No. :",font="curier 12",bg="#87cefa")
    regno.place(x=30,y=180)
    regin=Entry(pdFrame,font="arial 13")
    regin.place(x=130,y=180,height=25,width=150)
    regval=regin

    rolno=Label(pdFrame,text="Roll No. :",font="curier 12",bg="#87cefa")
    rolno.place(x=280,y=180)
    rolin=Entry(pdFrame,font="arial 13")
    rolin.place(x=350,y=180,height=25,width=150)
    rolval=rolin
    """

    fname=Label(pdFrame,text="Father's Name :",font="curier 12",bg="#87cefa")
    fname.place(x=10,y=220)
    fnamein=Entry(pdFrame,font="arial 13")
    fnamein.place(x=130,y=220,height=25,width=180)

    fphn=Label(pdFrame,text="Mobile No. :",font="curier 12",bg="#87cefa")
    fphn.place(x=320,y=220)
    fphnin=Entry(pdFrame,font="arial 13")
    fphnin.place(x=410,y=220,height=25,width=130)

    mname=Label(pdFrame,text="Mother's Name :",font="curier 12",bg="#87cefa")
    mname.place(x=10,y=260)
    mnamein=Entry(pdFrame,font="arial 13")
    mnamein.place(x=130,y=260,height=25,width=180)

    mphn=Label(pdFrame,text="Mobile No. :",font="curier 12",bg="#87cefa")
    mphn.place(x=320,y=260)
    mphnin=Entry(pdFrame,font="arial 13")
    mphnin.place(x=410,y=260,height=25,width=130)

    dt=Label(pdFrame,text="District :",font="curier 12",bg="#87cefa")
    dt.place(x=30,y=300)
    dtin=Entry(pdFrame,font="arial 13")
    dtin.place(x=100,y=300,height=24,width=150)

    datej=Label(pdFrame,text="Date Joined :",font="curier 12",bg="#87cefa")
    datej.place(x=290,y=300)
    datejin=DateEntry(pdFrame,font="arial 12")
    datejin.place(x=400,y=300,height=25,width=85)

    chkbox=Checkbutton(pdFrame,text="information given are correct",font="curier 12",bg="#87cefa")
    chkbox.place(x=50,y=340)

    pribox=Checkbutton(pdFrame,text="Accept Privacy and Policy",font="curier 12",bg="#87cefa")
    pribox.place(x=280,y=340)

    savebtn=Button(pdFrame,text="Save And Next",font="curier 12",bg="#87cefa")
    savebtn.place(x=410,y=380)

def eduFrame():

    eduFrame=Frame(root,bg="#EE82EE")
    eduFrame.pack(side=RIGHT)
    eduFrame.configure(width=685,height=420)
    eduFrame.place(x=150,y=30)

    edutitle=Label(eduFrame,text="Educational Details",font="curier 17",bg="#EE82EE")
    edutitle.place(x=160,y=20)

    college=Label(eduFrame,text="College Name :",font="curier 13",bg="#EE82EE")
    college.place(x=10,y=70)
    collegein=Entry(eduFrame,font="arial 13")
    collegein.place(x=130,y=70,width=300,height=25)

    colcode=Label(eduFrame,text="College Code :",font="curier 13",bg="#EE82EE")
    colcode.place(x=10,y=110)
    colin=Entry(eduFrame,font="courier 13")
    colin.place(x=130,y=110,width=60,height=25)

    deg=Label(eduFrame,text="Degree :",font="curier 13",bg="#EE82EE")
    deg.place(x=50,y=147)
    degin=Entry(eduFrame,font="arial 13")
    degin.place(x=120,y=145,width=50,height=25)

    dept=Label(eduFrame,text="Department :",font="curier 13",bg="#EE82EE")
    dept.place(x=190,y=147)
    deptin=Entry(eduFrame,font="arial 13")
    deptin.place(x=295,y=145,width=60,height=25)

    yr=Label(eduFrame,text="Year :",font="curier 13",bg="#EE82EE")
    yr.place(x=370,y=147)
    yrin=Entry(eduFrame,font="arial 13")
    yrin.place(x=430,y=145,width=70,height=25)

    regno=Label(eduFrame,text="Register No. :",font="curier 13",bg="#EE82EE")
    regno.place(x=10,y=182)
    regin=Entry(eduFrame,font="arial 13")
    regin.place(x=120,y=182,width=150,height=25)

    rolno=Label(eduFrame,text="Roll No. :",font="curier 13",bg="#EE82EE")
    rolno.place(x=280,y=182)
    rolin=Entry(eduFrame,font="arial 13")
    rolin.place(x=355,y=181,width=120,height=25)

    passout=Label(eduFrame,text="Year of Passing :",font="curier 13",bg="#EE82EE")
    passout.place(x=10,y=220)
    passoutin=Entry(eduFrame,font="curier 13")
    passoutin.place(x=150,y=220,width=60,height=25)
    
    batch=Label(eduFrame,text="Batch :",font="curier 13",bg="#EE82EE")
    batch.place(x=230,y=220)
    batchin=Entry(eduFrame,font="arial 13")
    batchin.place(x=290,y=220,width=100,height=25)

    admission=Label(eduFrame,text="Admission Type :",font="curier 13",bg="#EE82EE")
    admission.place(x=10,y=260)
    typein1=Checkbutton(eduFrame,text="Govt.Quota",font="arial 13",bg="#EE82EE")
    typein1.place(x=150,y=258)
    typein2=Checkbutton(eduFrame,text="Management Quota",font="arial 13",bg="#EE82EE")
    typein2.place(x=270,y=258)

    st=Label(eduFrame,text="If Government Quota,",font="curier 13",bg="#EE82EE")
    st.place(x=20,y=295)    

    cno=Label(eduFrame,text="TNEA Application No. :",font="curier 13",bg="#EE82EE")
    cno.place(x=50,y=325)
    cnoin=Entry(eduFrame,font="arial 13")
    cnoin.place(x=230,y=325,width=150,height=25)

    savebtn=Button(eduFrame,text="Save And Next",font="curier 13",bg="#87cefa")
    savebtn.place(x=410,y=370)

def addFrame():
    addFrame=Frame(root,bg="#F0E68C")
    addFrame.pack(side=RIGHT)
    addFrame.configure(width=685,height=430)
    addFrame.place(x=150,y=30)

    addtitle=Label(addFrame,text="Address Details",font="curier 17",bg="#F0E68C")
    addtitle.place(x=180,y=10)

    addtitle1=Label(addFrame,text="Current Address :-",font="curier 15 bold",bg="#F0E68C")
    addtitle1.place(x=5,y=50)

    door=Label(addFrame,text="Door No. :",font="curier 13",bg="#F0E68C")
    door.place(x=20,y=80)
    doorin=Entry(addFrame,font="arial 13")
    doorin.place(x=110,y=80,width=60,height=25)

    strt=Label(addFrame,text="Street :",font="curier 13",bg="#F0E68C")
    strt.place(x=180,y=80)
    strtin=Entry(addFrame,font="arial 13")
    strtin.place(x=250,y=80,width=280,height=25)

    dt=Label(addFrame,text="District :",font="curier 13",bg="#F0E68C")
    dt.place(x=20,y=115)
    dtin=Entry(addFrame,font="arial 13")
    dtin.place(x=90,y=115,width=150,height=25) 

    po=Label(addFrame,text="(PO) :",font="curier 13",bg="#F0E68C")
    po.place(x=250,y=115)
    poin=Entry(addFrame,font="arial 13")
    poin.place(x=305,y=115,width=150,height=25)

    pin=Label(addFrame,text="Pin :",font="curier 13",bg="#F0E68C")
    pin.place(x=20,y=150)
    pinin=Entry(addFrame,font="arial 13")
    pinin.place(x=70,y=150,width=100,height=25) 

    st=Label(addFrame,text="State :",font="curier 13",bg="#F0E68C")
    st.place(x=190,y=150)
    stin=Entry(addFrame,font="arial 13")
    stin.place(x=250,y=150,width=180,height=25) 

    addtitle2=Label(addFrame,text="Permanent Address :-",font="curier 15 bold",bg="#F0E68C")
    addtitle2.place(x=5,y=180)

    checkbox1=Checkbutton(addFrame,text="Permanent Address same as Current Address!",font="curier 11",bg="#F0E68C")
    checkbox1.place(x=60,y=210,height=18)

    door=Label(addFrame,text="Door No. :",font="curier 13",bg="#F0E68C")
    door.place(x=20,y=235)
    doorin=Entry(addFrame,font="arial 13")
    doorin.place(x=110,y=235,width=60,height=25)

    strt=Label(addFrame,text="Street :",font="curier 13",bg="#F0E68C")
    strt.place(x=180,y=235)
    strtin=Entry(addFrame,font="arial 13")
    strtin.place(x=250,y=235,width=280,height=25)

    dt=Label(addFrame,text="District :",font="curier 13",bg="#F0E68C")
    dt.place(x=20,y=270)
    dtin=Entry(addFrame,font="arial 13")
    dtin.place(x=90,y=270,width=150,height=25) 

    po=Label(addFrame,text="(PO) :",font="curier 13",bg="#F0E68C")
    po.place(x=250,y=270)
    poin=Entry(addFrame,font="arial 13")
    poin.place(x=305,y=270,width=150,height=25)

    pin=Label(addFrame,text="Pin :",font="curier 13",bg="#F0E68C")
    pin.place(x=20,y=305)
    pinin=Entry(addFrame,font="arial 13")
    pinin.place(x=70,y=305,width=100,height=25) 

    st=Label(addFrame,text="State :",font="curier 13",bg="#F0E68C")
    st.place(x=190,y=305)
    stin=Entry(addFrame,font="arial 13")
    stin.place(x=250,y=305,width=180,height=25) 

    savebtn=Button(addFrame,text="Save And Next",font="curier 12",bg="#87cefa")
    savebtn.place(x=410,y=380)

sideframe1=Frame(root,bg="#B0C4DE")
sideframe1.pack(side=LEFT)
sideframe1.configure(width=150,height=450)
sideframe1.place(x=0,y=0)

title=Label(root,text="New Entry Form",font="curier 16",fg="#000000")
title.place(x=330,y=0)  

title1=Button(sideframe1,text="Personal Info",bg="#B0C4DE",font="Californian 13 bold",command=lambda:pdFrame())
title1.place(x=0,y=90,width=150,height=40)
title2=Button(sideframe1,text="Education",bg="#B0C4DE",font="Californian 13 bold",command=lambda:eduFrame())
title2.place(x=0,y=132,width=150,height=40)
title3=Button(sideframe1,text="Address details",bg="#B0C4DE",font="Californian 13 bold",command=lambda:addFrame())
title3.place(x=0,y=174,width=150,height=40)
title4=Button(sideframe1,text="Upload\nDocuments",bg="#B0C4DE",font="Californian 13 bold")
title4.place(x=0,y=216,width=150,height=40)
title5=Button(sideframe1,text="Verification",bg="#B0C4DE",font="Californian 13 bold")
title5.place(x=0,y=258,width=150,height=40)

backbtn=Button(root,text="Back",font="Californian 10 bold",fg="#000000",bg="#C0C0C0")
backbtn.pack()
backbtn.place(x=20,y=410)  

homebtn=Button(root,text="Home",font="Californian 10 bold",fg="#000000",bg="#C0C0C0")
homebtn.pack()
homebtn.place(x=85,y=410)  

root.mainloop()