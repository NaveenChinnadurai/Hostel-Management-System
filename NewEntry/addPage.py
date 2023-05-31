from tkinter import *


from Startup import main_frame,con,cur
from pdPage import genno
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

