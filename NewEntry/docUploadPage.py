from tkinter import *
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