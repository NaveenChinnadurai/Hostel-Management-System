from tkinter import *
from tkinter import Frame
import mysql.connector as mysql

from Home import HomePage

window=Tk()
window.geometry("700x450")
window.title("Hostel Management System")

#Main Frame
main_frame=Frame(window,bg="#FFFFFF")
main_frame.pack()
main_frame.configure(width=700,height=450)

#Database Connectivity
con=mysql.connect(host='localhost',user='root',password="Swetha@143Babe",database="projectdb")
cur=con.cursor()

HomePage() 

window.mainloop()