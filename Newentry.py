from tkinter import *
from tkinter import messagebox


from Startup import main_frame
from NewEntry.pdPage import pdPage
from NewEntry.eduPage import eduPage
from NewEntry.addPage import addPage
from NewEntry.docUploadPage import upload_doc

from Home import HomePage

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
