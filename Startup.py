from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from tkcalendar import *
import mysql.connector as mysql

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

#For Personal Details Page
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

def adsave():
    cdoorval=cdoorin.get()
    cstrtval=cstrtin.get()
    cdtval=cdtin.get()
    cpoval=cpoin.get()
    cpinval=cpinin.get()
    cstval=cstin.get()
    pdoorval=pdoorin.get()
    pstrtval=pstrtin.get()
    pdtval=pdtin.get()
    ppoval=ppoin.get()
    ppinval=ppinin.get()
    pstval=pstin.get()
    cval=cin.get()

    value1=(genno,cdoorval,cstrtval,cdtval,cpoval,cpinval,cstval,pdoorval,pstrtval,pdtval,ppoval,ppinval,pstval,cval)

    cur.execute("INSERT INTO Address_Details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",value1)
    con.commit()

def curper():
    intval=int5.get()
    if intval==1:
        pdoorin.insert(0,cdoorin.get())
        pstrtin.insert(0,cstrtin.get())
        pdtin.insert(0,cdtin.get())
        ppoin.insert(0,cpoin.get())
        ppinin.insert(0,cpinin.get())
        pstin.insert(0,cstin.get())
    if intval==0:
        pdoorin.delete(0,"end")
        pstrtin.delete(0,"end")
        pdtin.delete(0,"end")
        ppoin.delete(0,"end")
        ppinin.delete(0,"end")
        pstin.delete(0,"end")

#For Address Details page
def addPage():

    addFrame=Frame(main_frame,bg="#FFFFFF")
    addFrame.configure(width=685,height=430)
    addFrame.place(x=150,y=30)

    addtitle=Label(addFrame,text="Address Details",font="curier 17",bg="#FFFFFF")
    addtitle.place(x=180,y=10)

    addtitle1=Label(addFrame,text="Current Address :-",font="curier 15 bold",bg="#FFFFFF")
    addtitle1.place(x=5,y=50)

    cdoor=Label(addFrame,text="Door No. :",font="curier 13",bg="#FFFFFF")
    cdoor.place(x=20,y=80)
    global cdoorin
    cdoorin=Entry(addFrame,font="arial 13")
    cdoorin.place(x=110,y=80,width=60,height=25)

    cstrt=Label(addFrame,text="Street :",font="curier 13",bg="#FFFFFF")
    cstrt.place(x=180,y=80)
    global cstrtin
    cstrtin=Entry(addFrame,font="arial 13")
    cstrtin.place(x=250,y=80,width=280,height=25)

    cdt=Label(addFrame,text="District :",font="curier 13",bg="#FFFFFF")
    cdt.place(x=20,y=115)
    global cdtin
    cdtin=Entry(addFrame,font="arial 13")
    cdtin.place(x=90,y=115,width=150,height=25)

    cpo=Label(addFrame,text="(PO) :",font="curier 13",bg="#FFFFFF")
    cpo.place(x=250,y=115)
    global cpoin
    cpoin=Entry(addFrame,font="arial 13")
    cpoin.place(x=305,y=115,width=150,height=25)

    cpin=Label(addFrame,text="Pin :",font="curier 13",bg="#FFFFFF")
    cpin.place(x=20,y=150)
    global cpinin
    cpinin=Entry(addFrame,font="arial 13")
    cpinin.place(x=70,y=150,width=100,height=25) 

    cst=Label(addFrame,text="State :",font="curier 13",bg="#FFFFFF")
    cst.place(x=190,y=150)
    global cstin
    cstin=Entry(addFrame,font="arial 13")
    cstin.place(x=250,y=150,width=180,height=25) 

    addtitle2=Label(addFrame,text="Permanent Address :-",font="curier 15 bold",bg="#FFFFFF")
    addtitle2.place(x=5,y=180)

    global int5
    int5=IntVar()

    checkbox1=Checkbutton(addFrame,text="Permanent Address same as Current Address!",font="curier 11",bg="#FFFFFF")
    checkbox1.place(x=60,y=210,height=18)
    checkbox1.configure(command=lambda:curper(),variable=int5,offvalue=0,onvalue=1)

    pdoor=Label(addFrame,text="Door No. :",font="curier 13",bg="#FFFFFF")
    pdoor.place(x=20,y=235)
    global pdoorin
    pdoorin=Entry(addFrame,font="arial 13")
    pdoorin.place(x=110,y=237,width=60,height=25)

    pstrt=Label(addFrame,text="Street :",font="curier 13",bg="#FFFFFF")
    pstrt.place(x=180,y=235)
    global pstrtin
    pstrtin=Entry(addFrame,font="arial 13")
    pstrtin.place(x=250,y=237,width=280,height=25)

    pdt=Label(addFrame,text="District :",font="curier 13",bg="#FFFFFF")
    pdt.place(x=20,y=270)
    global pdtin
    pdtin=Entry(addFrame,font="arial 13")
    pdtin.place(x=90,y=270,width=150,height=25) 

    ppo=Label(addFrame,text="(PO) :",font="curier 13",bg="#FFFFFF")
    ppo.place(x=250,y=270)
    global ppoin
    ppoin=Entry(addFrame,font="arial 13")
    ppoin.place(x=305,y=270,width=150,height=25)

    ppin=Label(addFrame,text="Pin :",font="curier 13",bg="#FFFFFF")
    ppin.place(x=20,y=305)
    global ppinin
    ppinin=Entry(addFrame,font="arial 13")
    ppinin.place(x=70,y=305,width=100,height=25) 

    pst=Label(addFrame,text="State :",font="curier 13",bg="#FFFFFF")
    pst.place(x=190,y=305)
    global pstin
    pstin=Entry(addFrame,font="arial 13")
    pstin.place(x=250,y=305,width=180,height=25) 

    cno=Label(addFrame,text="Contact No. :",font="curier 13",bg="#FFFFFF")
    cno.place(x=30,y=335)
    global cin
    cin=Entry(addFrame,font="arial 13")
    cin.place(x=135,y=335,width=100,height=25)

    savebtn=Button(addFrame,text="Save And Next",font="curier 12",bg="#FFFFFF",command=adsave)
    savebtn.place(x=410,y=380)

def upload_doc():

    upFrame=Frame(main_frame,bg="#FFFFFF")
    upFrame.configure(width=685,height=430)
    upFrame.place(x=150,y=30)

    title1=Label(upFrame,text="Upload Documents",font="curier 17",bg="#FFFFFF")
    title1.place(x=150,y=10)

    photo1=Label(upFrame,text="upload Photo:",font="curier 14")
    photo1.place(x=30,y=50)
    
    ftyp=[('Jpg Files','*.jpg')]
    fname=filedialog.askopenfilename(filetypes=ftyp)
    

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

def rvPage(x):
    rvFrame=Frame(x)
    rvFrame.configure(width=700,height=450)
    rvFrame.place(x=0,y=0)

    title1=Label(rvFrame,text="Room Vacancy Details",font="courier 17 bold")
    title1.place(x=250,y=10)

    backbtn=Button(rvFrame,text="Back",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=lambda:Attendence())
    backbtn.place(x=10,y=15,height=20)

    homebtn=Button(rvFrame,text="Home",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=lambda:HomePage())
    homebtn.place(x=10,y=410)  

    exitbtn=Button(rvFrame,text="EXIT",font="Courier 13 bold",fg="#000000",bg="#C0C0C0",command=window.quit)
    exitbtn.place(x=640,y=415,width=50,height=25)

#New Entry Frame
def NewEntry():
    sideFrame1=Frame(main_frame,bg="#B0C4DE")
    sideFrame1.configure(width=150,height=450)
    sideFrame1.place(x=0,y=0)

    title=Label(main_frame,text="New Entry Form",font="curier 16",fg="#000000",bg="#FFFFFF")
    title.place(x=330,y=0)  

    title1=Button(sideFrame1,text="Personal Info",bg="#B0C4DE",font="Californian 13 bold",command=lambda:pdPage())
    title1.place(x=0,y=90,width=150,height=40)

    title2=Button(sideFrame1,text="Education",bg="#B0C4DE",font="Californian 13 bold",command=lambda:eduPage())
    title2.place(x=0,y=132,width=150,height=40)

    title3=Button(sideFrame1,text="Address details",bg="#B0C4DE",font="Californian 13 bold",command=lambda:addPage())
    title3.place(x=0,y=174,width=150,height=40)
  
    title4=Button(sideFrame1,text="Upload\nDocuments",bg="#B0C4DE",font="Californian 13 bold",command=lambda:upload_doc())
    title4.place(x=0,y=216,width=150,height=40)

    title5=Button(sideFrame1,text="Verification",bg="#B0C4DE",font="Californian 13 bold")
    title5.place(x=0,y=258,width=150,height=40)
    
    pdPage()

    backbtn=Button(sideFrame1,text="Back",font="Californian 10 bold",fg="#000000",bg="#C0C0C0")
    backbtn.place(x=20,y=410)  

    homebtn=Button(sideFrame1,text="Home",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=lambda:HomePage())
    homebtn.place(x=85,y=410)  
    
    messagebox.showwarning("Warning"," Kindly, Provide Correct details!")

def viewProfile():
    vpFrame=Frame(main_frame,bg='#FFFFFF')
    vpFrame.configure(width=700,height=450)
    vpFrame.place(x=0,y=0)

    title=Label(vpFrame,text="View Profile",font="curier 17",fg="#000000")
    title.place(x=300,y=20) 

    name=Label(vpFrame,text="Name",font="curier 14",bg="#FFFFFF")
    name.place(x=180,y=160)
    nameEntry=Entry(vpFrame,font="arial 14")
    nameEntry.place(x=330,y=160)

    dpt=Label(vpFrame,text="Deg/Dept",font="curier 14",bg="#FFFFFF")
    dpt.place(x=180,y=200)
    dptEntry=Entry(vpFrame,font="curier 14")
    dptEntry.place(x=330,y=200)

    rolno=Label(vpFrame,text="Roll No.",font="curier 14",bg="#FFFFFF")
    rolno.place(x=180,y=240)
    rolEntry=Entry(vpFrame,font="curier 14")
    rolEntry.place(x=330,y=240)

    s1=Label(vpFrame,text=":",font="curier 15",bg="#FFFFFF")
    s1.place(x=310,y=160)

    s2=Label(vpFrame,text=":",font="curier 15",bg="#FFFFFF")
    s2.place(x=310,y=200)

    s3=Label(vpFrame,text=":",font="curier 15",bg="#FFFFFF")
    s3.place(x=310,y=240)

    searchbtn=Button(vpFrame,text="Search",font="curier 13",bg="#1E90FF")
    searchbtn.place(x=320,y=285,width=80,height=30)

    backbtn=Button(vpFrame,text="Back",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=HomePage)
    backbtn.pack()
    backbtn.place(x=10,y=410)  

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

def OutPass():
    Frame4=Frame(main_frame,bg='#FFFFFF')
    Frame4.place(x=0,y=0)
    Frame4.configure(width=700,height=450)

    title=Label(Frame4,text="GatePass History ",font="curier 17",fg="#000000",bg="#FFFFFF")
    title.place(x=270,y=10)

    out1=Label(Frame4,text="See Who Checked Out ",font="curier 14")
    out1.place(x=170,y=80)

    outbtn=Button(Frame4,text="Search",font="curier 14")
    outbtn.place(x=400,y=80)

    rol=Entry(Frame4,font="arial 14")

    backButton=Button(Frame4,text="Back",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=HomePage)
    backButton.place(x=20,y=410)  
#35,44,56,59,62
def Summary():
    Frame5=Frame(main_frame,bg='#FFFFFF')
    Frame5.place(x=0,y=0)
    Frame5.configure(width=700,height=450)

    title=Label(Frame5,text="Hostel Summary",font="curier 17",fg="#000000",bg="#FFFFFF")
    title.place(x=270,y=10)

    tstu=Label(Frame5,text="Total No. of students:",font="curier 14",bg="#FFFFFF")
    tstu.place(x=50,y=60)

    tstuval=Label(Frame5,text="     ",font="curier 14",bg="#EE82EE")
    tstuval.place(x=250,y=60)

    troom=Label(Frame5,text="Total Rooms:",font="curier 14",bg="#FFFFFF")
    troom.place(x=320,y=60)

    troomval=Label(Frame5,text="      ",font="curier 14",bg="#EE82EE")
    troomval.place(x=450,y=60)

    backbtn=Button(Frame5,text="Back",font="Californian 10 bold",fg="#000000",bg="#C0C0C0",command=HomePage)
    backbtn.place(x=20,y=410)

con=mysql.connect(host='localhost',user='root',password="Swetha@143Babe",database="projectdb")
cur=con.cursor()

window=Tk()
window.geometry("700x450")
window.title("Hostel Management System")

#Main Frame
main_frame=Frame(window,bg="#FFFFFF")
main_frame.pack()
main_frame.configure(width=700,height=450)

HomePage()

window.mainloop()