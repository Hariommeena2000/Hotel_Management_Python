from tkinter import*
#from PIL import Image
from tkinter import ttk 
import random
import mysql.connector
from tkinter import messagebox

from mysql.connector.errors import DatabaseError

class reportdp:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_ref=StringVar()
        x="This project is Developed By 'Hariom Meena','Pinky Mahawar' \
          and 'Mohan Lal Prajapat' Students Of 8th sem Of \
           "
        self.var_ref.set(str(x))

        lbl_title=Label(self.root,text="About Developer",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=6,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=70)
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Hariom Meena",font=("times new roman",25,"bold"),padx=2)
        labelframeleft.place(x=5,y=70,width=1295,height=470)

        entry_report=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=120,font=("arial",13,"bold"))
        entry_report.grid(row=0,column=1)





if __name__== "__main__":
    root=Tk()
    obj=reportdp(root)
    root.mainloop()