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
