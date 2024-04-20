from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk 
import random
import mysql.connector
from tkinter import messagebox

from mysql.connector.errors import DatabaseError


class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #================================================variables========================================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


        #=================================================title===========================================================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #============================logo===================================================================
        img2=Image.open(r"F:\\python 8th sem\\mylibrary\\mylibrary\\hotel_images\\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        #=============================lableFrame==========================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #==============================labels and entry====================================================
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #================================customer name============================================
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        

        #=================================mother name==============================================
        lbl_cust_mname=Label(labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_mname.grid(row=2,column=0,sticky=W)
        
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)


        #================================gender combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        #================================postcode=============================
        lblpostcode=Label(labelframeleft,text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        
        txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
        txtpostcode.grid(row=4,column=1)

        #================================mobile number==========================

        lblmobile=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)
        
        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        txtmobile.grid(row=5,column=1)

        #==================================Email================================
        lblemail=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)
        
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        txtemail.grid(row=6,column=1)

        #==================================nationality=======================
        lblnationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("Indian","American","Britist")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        

        #==================================idproof type combobox===============
        lblidproof=Label(labelframeleft,text="Id Proof Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)
        
        combo_idtype=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_idtype["value"]=("AdharCard","DrivingLicence","Passport")
        combo_idtype.current(0)
        combo_idtype.grid(row=8,column=1)

        #===================================id number===========================
        lblnumber=Label(labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblnumber.grid(row=9,column=0,sticky=W)
        
        txtnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtnumber.grid(row=9,column=1)

        #===================================address==============================
        lbladdress=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)
        
        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        txtaddress.grid(row=10,column=1)


        #====================================Buttons======================
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


        #==============================table frame=============================
        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details Ans Search System",font=("times new roman",12,"bold"),padx=2)
        tabelframe.place(x=435,y=50,width=860,height=490)

        lblsearch=Label(tabelframe,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_search=ttk.Combobox(tabelframe,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","Ref")
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
        deatils_frame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(deatils_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(deatils_frame,orient=VERTICAL)


        self.cust_Details_Table=ttk.Treeview(deatils_frame,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("ref",text="Refer No")
        self.cust_Details_Table.heading("name",text="Name")
        self.cust_Details_Table.heading("mother",text="Mother Name")
        self.cust_Details_Table.heading("gender",text="Gender")
        self.cust_Details_Table.heading("post",text="Postcode")
        self.cust_Details_Table.heading("mobile",text="Mobile")
        self.cust_Details_Table.heading("email",text="Email")
        self.cust_Details_Table.heading("nationality",text="Nationality")
        self.cust_Details_Table.heading("idproof",text="Id Proof")
        self.cust_Details_Table.heading("idnumber",text="Id Number")
        self.cust_Details_Table.heading("address",text="Address")

        self.cust_Details_Table["show"]="headings"
        self.cust_Details_Table.column("ref",width=100)
        self.cust_Details_Table.column("name",width=100)
        self.cust_Details_Table.column("mother",width=100)
        self.cust_Details_Table.column("gender",width=100)
        self.cust_Details_Table.column("post",width=100)
        self.cust_Details_Table.column("mobile",width=100)
        self.cust_Details_Table.column("email",width=100)
        self.cust_Details_Table.column("nationality",width=100)
        self.cust_Details_Table.column("idproof",width=100)
        self.cust_Details_Table.column("idnumber",width=100)
        self.cust_Details_Table.column("address",width=100)
        
        self.cust_Details_Table.pack(fill=BOTH,expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Attention","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                   self.var_ref.get(),
                                                                                                   self.var_cust_name.get(),
                                                                                                   self.var_mother.get(),
                                                                                                   self.var_gender.get(),
                                                                                                   self.var_post.get(),
                                                                                                   self.var_mobile.get(),
                                                                                                   self.var_email.get()
                                                                                                   ,self.var_nationality.get(),
                                                                                                   self.var_id_proof.get(),
                                                                                                   self.var_id_number.get(),
                                                                                                   self.var_address.get()
                                                                                                ))

                messagebox.showinfo("Success","customer has been added",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()            
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    
    def update(self):
        if self.var_mobile.get()=="0":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                    ))  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)      



    def Delete(self):
        Delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if Delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        #self.var_ref.set(row("")),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(row("")),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(row("")),
        #self.var_id_proof.set(row("")),
        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="109876543210",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.serch_var.get())+" LIKE '%"+str(self.txt_serch.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        


if __name__ =="__main__":
            root=Tk()
            obj=cust_win(root)
            root.mainloop()