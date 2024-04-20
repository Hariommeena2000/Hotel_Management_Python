import builtins
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk 
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #============================================variable==============================================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        

        #=================================================title===========================================================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #============================logo===================================================================
        img2=Image.open(r"F:\\python 8th sem\\mylibrary\\mylibrary\\hotel_images\\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        #=============================lableFrame==========================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #==============================labels and entry====================================================
        
        #=========================================Customer contact========================================
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #=======================================fetch data button======================================
        btnfetch=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnfetch.place(x=347,y=4)

        #==========================================Check in date=======================================
        check_in_date=Label(labelframeleft,text="Check In Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)
        #==============================Check out date====================================================
        check_out_date=Label(labelframeleft,text="Check Out Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        
        txtcheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txtcheck_out_date.grid(row=2,column=1)
        #==============================Room type====================================================
        room_type=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        room_type.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        
        combo_room_type=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_room_type["value"]=ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)

        #==============================Available room====================================================
        RoomAvailable=Label(labelframeleft,text="Available Room:",font=("arial",12,"bold"),padx=2,pady=6)
        RoomAvailable.grid(row=4,column=0,sticky=W)
        
        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4,column=1)

        #==============================Meal====================================================
        Meal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        Meal.grid(row=5,column=0,sticky=W)
        
        #txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        #txtMeal.grid(row=5,column=1)
        combo_meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        combo_meal["value"]=("BreakFast","Lunch","Dinner")
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)

        #=============================No Of Days====================================================
        NoOfDays=Label(labelframeleft,text="No Of Days",font=("arial",12,"bold"),padx=2,pady=6)
        NoOfDays.grid(row=6,column=0,sticky=W)
        
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        #=================================Paid Tax==================================================
        PaidTax=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        PaidTax.grid(row=7,column=0,sticky=W)
        txtPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txtPaidTax.grid(row=7,column=1)

        #====================================sub Total============================================
        SubTotal=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        SubTotal.grid(row=8,column=0,sticky=W)
        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txtSubTotal.grid(row=8,column=1)

        #====================================sub Total============================================
        TotalCost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        TotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txtTotalCost.grid(row=9,column=1)

        #=======================================Bill button=============================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=10,column=1,padx=1,sticky=W)


        #===================================buttons=====================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #==============================Right side image=======================================
        img3=Image.open(r"F:\\python 8th sem\\mylibrary\\mylibrary\\hotel_images\\room2.jpg")
        img3=img3.resize((520,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=760,y=55,width=520,height=300)


        #==============================table frame=============================
        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details Ans Search System",font=("times new roman",12,"bold"),padx=2)
        tabelframe.place(x=435,y=280,width=860,height=260)

        lblsearch=Label(tabelframe,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_search=ttk.Combobox(tabelframe,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","roomavailable")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_serch=StringVar()
        txtsearch=ttk.Entry(tabelframe,textvariable=self.txt_serch,width=24,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnseach=Button(tabelframe,text="Search",command=self.search,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnseach.grid(row=0,column=3,padx=1)

        btnshowall=Button(tabelframe,text="Show All",command=self.fetch_data,font=("arial",13,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)

        #=================================show data table==============================
        deatils_frame=Frame(tabelframe,bd=2,relief=RIDGE)
        deatils_frame.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(deatils_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(deatils_frame,orient=VERTICAL)


        self.room_table=ttk.Treeview(deatils_frame,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="No Of Days")
               
     
       
        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)                   
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    #============================================add data===========================================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Attention","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
                                                                                ))

                messagebox.showinfo("Success","Room Booked",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()            
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    #=======================================fetch data=========================================
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from room")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    #===============================get cursor==========================================================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    #============================================update data==============================================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                             self.var_checkin.get(),
                                                                                                                                             self.var_checkout.get(),
                                                                                                                                             self.var_roomtype.get(),
                                                                                                                                             self.var_roomavailable.get(),
                                                                                                                                             self.var_meal.get(),
                                                                                                                                             self.var_noofdays.get(),
                                                                                                                                             self.var_contact.get()
                                                                                                                                                                    ))  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root) 

    #=============================================Delete data=======================================
    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this Room Details",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()     


    #===========================================reset=================================================
    def reset(self):
            self.var_contact.set("")
            self.var_checkin.set("")
            self.var_checkout.set("")
            self.var_roomtype.set("")
            self.var_roomavailable.set("")
            self.var_meal.set("")
            self.var_noofdays.set("")
            self.var_paidtax.set("")
            self.var_actualtotal.set("")
            self.var_total.set("")

    #============================================All data fetch=========================================
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
            my_cursor=conn.cursor(buffered=True)
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                #============================gender============================================
                conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
                my_cursor=conn.cursor(buffered=True)
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=30)

                #============================Email============================================
                conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
                my_cursor=conn.cursor(buffered=True)
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=60)

                #==================================Nationality======================================
                conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
                my_cursor=conn.cursor(buffered=True)
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=90)

                #============================Address============================================
                conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
                my_cursor=conn.cursor(buffered=True)
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=120)
    
    #======================================search data==============================================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_serch.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #=======================================total bill=================================================
    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")       
        self.var_noofdays.set(abs(outdate-indate).days)

        if(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            q1=float(200)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(400)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(400)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(400)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))   
            ST="Rs."+str("%.2f"%((q5)))        
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)




if __name__ =="__main__":
            root=Tk()
            obj=RoomBooking(root)
            root.mainloop()