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
