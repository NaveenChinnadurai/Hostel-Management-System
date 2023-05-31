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