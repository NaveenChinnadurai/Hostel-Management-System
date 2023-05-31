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
