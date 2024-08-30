from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1137x480+222+225")


        #===================== Variable =================================
        self.var_contact=StringVar()
        self.var_checkindate=StringVar()
        self.var_checkoutdate=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


#=============================== Title ===============================================
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1137,height=50)

        #==================== Logo ============================================
        # Open and resize image
        img2 = Image.open(r"C:\Users\tiwari\Documents\HMS images\logo1.jpg")
        img2 = img2.resize((95,44), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Display image in a label
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=3, y=2, width=95, height=44)

         #=========================== Label =========================
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("Arial Unicode MS",11,"bold"),padx=2)
        LabelFrameleft.place(x=0,y=50,width=425,height=415)

         #========================= Labels & Entry ==============================
        #cust_contact
        lbl_cust_contact=Label(LabelFrameleft,text="Customer contact:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        enty_contact=ttk.Entry(LabelFrameleft,width=25,textvariable=self.var_contact,font=("Arial Unicode MS",8,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)

        #Fetch data
        btnFetchData=Button(LabelFrameleft,text="Fetch Data",command=self.Fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=300,y=4)

        #check-in-Date
        lbl_check_in_date=Label(LabelFrameleft,text="Check_in_date:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_check_in_date.grid(row=1,column=0,sticky=W)
        
        txt_check_in_date=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_checkindate,font=("Arial Unicode MS",8,"bold"))
        txt_check_in_date.grid(row=1,column=1)

        #check-out-date
        lbl_check_out_date=Label(LabelFrameleft,text="Check-out-date:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_check_out_date.grid(row=2,column=0,sticky=W)
        
        txt_check_out_date=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_checkoutdate,font=("Arial Unicode MS",8,"bold"))
        txt_check_out_date.grid(row=2,column=1)

        #Room Type
        lbl_RoomType=Label(LabelFrameleft,text="Room Type:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomType from details")
        Type=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomtype,font=("arial",8,"bold"),width=36,state="readonly")
        combo_RoomType["value"]=Type
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Availabel
        lbl_RoomAvailable=Label(LabelFrameleft,text="Room Available:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_RoomAvailable.grid(row=4,column=0,sticky=W)
        
        #txt_RoomAvailable=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_roomavailable,font=("Arial Unicode MS",8,"bold"))
        #txt_RoomAvailable.grid(row=4,column=1)
        conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomNO from details")
        rows=my_cursor.fetchall()

        combo_RoomType=ttk.Combobox(LabelFrameleft,textvariable=self.var_roomavailable,font=("arial",8,"bold"),width=36,state="readonly")
        combo_RoomType["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4,column=1)

        #Meal
        lbl_Meal=Label(LabelFrameleft,text="Meal:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_Meal.grid(row=5,column=0,sticky=W)
        
        txt_Meal=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_meal,font=("Arial Unicode MS",8,"bold"))
        txt_Meal.grid(row=5,column=1)

        #No of Days
        lbl_No_of_Days=Label(LabelFrameleft,text="No of Days:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_No_of_Days.grid(row=6,column=0,sticky=W)
        
        txt_No_of_Days=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_noofdays,font=("Arial Unicode MS",8,"bold"))
        txt_No_of_Days.grid(row=6,column=1)

        #Paid Tax
        lbl_PaidTax=Label(LabelFrameleft,text="Paid Tax:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_PaidTax.grid(row=7,column=0,sticky=W)
        
        txt_PaidTax=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_paidtax,font=("Arial Unicode MS",8,"bold"))
        txt_PaidTax.grid(row=7,column=1)

        #Sub Total
        lbl_SubTotal=Label(LabelFrameleft,text="Sub Total:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_SubTotal.grid(row=8,column=0,sticky=W)
        
        txt_SubTotal=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_actualtotal,font=("Arial Unicode MS",8,"bold"))
        txt_SubTotal.grid(row=8,column=1)

        #Total Cost
        lbl_Totalcost=Label(LabelFrameleft,text="Total Cost:",font=("Arial Unicode MS",8,"bold"),padx=2,pady=6)
        lbl_Totalcost.grid(row=9,column=0,sticky=W)
        
        txt_Totalcost=ttk.Entry(LabelFrameleft,width=34,textvariable=self.var_total,font=("Arial Unicode MS",8,"bold"))
        txt_Totalcost.grid(row=9,column=1)

        #==============Bill btn====================
        btnBill=Button(LabelFrameleft,text="Bill",command=self.total,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        #====================== Buttons ============================================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=20,y=355,width=370,height=30)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #=================Right Image Logo========================
        # Open and resize image
        img3 = Image.open(r"C:\Users\tiwari\Documents\HMS images\pic6.jpg")
        img3 = img3.resize((395,215), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Display image in a label
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=740, y=52, width=395, height=215)


        #======================== table Frame Search system ======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=250,width=700,height=215)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_SearchBy=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=18,state="readonly")
        combo_SearchBy["value"]=("Contact","Room")
        combo_SearchBy.current(0)
        combo_SearchBy.grid(row=0,column=1,padx=2)

        self.text_search=StringVar()
        textSearch=ttk.Entry(Table_Frame,textvariable=self.text_search,font=("arial",12,"bold"),width=18)
        textSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        
        #===================== Show Data Table ===========================
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=695,height=140)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table = ttk.Treeview(
        details_table,
        columns=("Contact", "checkindate", "checkoutdate", "RoomType","RoomAvailable","meal","no of days"),
        xscrollcommand=scroll_x.set,  # Corrected here
        yscrollcommand=scroll_y.set   # Corrected here
        )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("checkindate",text="Check-in-Date")
        self.room_table.heading("checkoutdate",text="Check-out-Date")
        self.room_table.heading("RoomType",text="Room Type")
        self.room_table.heading("RoomAvailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("no of days",text="No of Days")
       

        self.room_table["show"]="headings"

        self.room_table.column("Contact",width=100)
        self.room_table.column("checkindate",width=100)
        self.room_table.column("checkoutdate",width=100)
        self.room_table.column("RoomType",width=100)
        self.room_table.column("RoomAvailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("no of days",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkindate.get()=="":
            messagebox.showerror("Error","All fields are requireed.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_contact.get(),
                                                                        self.var_checkindate.get(),
                                                                        self.var_checkoutdate.get(),
                                                                        self.var_roomtype.get(),
                                                                        self.var_roomavailable.get(),
                                                                        self.var_meal.get(),
                                                                        self.var_noofdays.get()
                                                                        
                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked.",parent=self.root)        
            except Exception as es:
                messagebox.showinfo("Warning",f"Something went wrong:{str(es)}",parent=self.root)


     #========================= Fetch Data ==============================           
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
        
    #============Getcorsur==========================
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkindate.set(row[1]),
        self.var_checkoutdate.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:    
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
                my_cursor = conn.cursor()
                my_cursor.execute("""
                UPDATE room 
                SET check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noofdays=%s
                WHERE Contact=%s
                                """, (
                self.var_checkindate.get(),
                self.var_checkoutdate.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()
               ))           
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Update", "Room details have been updated successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
            finally:
                conn.close()

    #========================== Detele Btn ===========================

    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this room",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
            my_cursor = conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

#============== Reset Btn ==========================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkindate.set(""),
        self.var_checkoutdate.set(""),
        #self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

           
     
    #======================== Fetching Data ========================

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
            my_cursor = conn.cursor()
            query = "select Name from customers where Mobile=%s"
        
        # Wrap the contact number in a tuple
            value = (self.var_contact.get(),)
        
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "This number not Found", parent=self.root)
        else:
            conn.commit()
            conn.close()

            showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            showDataFrame.place(x=430, y=58, width=300, height=185)          
            
            #==============cust_Name==================
            lblName = Label(showDataFrame, text="Name:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=0)

            lbl = Label(showDataFrame, text=row[0], font=("arial", 12, "bold"))
            lbl.place(x=100, y=0)


            #==============Gender==================
            conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
            my_cursor = conn.cursor()
            query = "select Gender from customers where Mobile=%s"
            value = (self.var_contact.get(),)
        
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblGender = Label(showDataFrame, text="Gender:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=30)

            lbl2 = Label(showDataFrame, text=row[0], font=("arial", 12, "bold"))
            lbl2.place(x=100, y=30)

             #==============Email==================
            conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
            my_cursor = conn.cursor()
            query = "select Email from customers where Mobile=%s"
            value = (self.var_contact.get(),)
        
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblGender = Label(showDataFrame, text="Email:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=60)

            lbl2 = Label(showDataFrame, text=row[0], font=("arial", 10, "bold"))
            lbl2.place(x=90, y=60)
            
             #==============Nationality==================
            conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
            my_cursor = conn.cursor()
            query = "select Nationality from customers where Mobile=%s"
            value = (self.var_contact.get(),)
        
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblNationality = Label(showDataFrame, text="Nationality:", font=("arial", 12, "bold"))
            lblNationality.place(x=0, y=90)

            lbl3 = Label(showDataFrame, text=row[0], font=("arial", 12, "bold"))
            lbl3.place(x=100, y=90)
             
            #==============Address===============================

            conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
            my_cursor = conn.cursor()
            query = "select Address from customers where Mobile=%s"
            value = (self.var_contact.get(),)
        
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblAddress = Label(showDataFrame, text="Address:", font=("arial", 12, "bold"))
            lblAddress.place(x=0, y=120)

            lbl4 = Label(showDataFrame, text=row[0], font=("arial", 10, "bold"))
            lbl4.place(x=90, y=120)

 #=================== Search System ============================
    def search(self):
        try:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root@9399633853",
            database="hms"
            )
            my_cursor = conn.cursor()

        # Safely constructing the SQL query using parameterized queries
            search_column = str(self.search_var.get())
            search_value = str(self.text_search.get())
            query = f"SELECT * FROM room WHERE {search_column} LIKE %s"
            my_cursor.execute(query, (f"%{search_value}%",))
        
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("", END, values=i)

            conn.commit()  # Commit changes (if any)
        except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
                conn.close()  # Ensure connection is closed 

#=========================== Total Function ==============================

    def total(self):
        inDate = self.var_checkindate.get()
        outDate = self.var_checkoutdate.get()
    
    # Convert string dates to datetime objects
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
    
    # Calculate the number of days between check-in and check-out
        self.var_noofdays.set(abs((outDate - inDate).days))
    
    # Initialize costs based on conditions
        if self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury":
            meal_cost = 1000.0
            room_cost = 5000.0
        elif  self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury":
           
           meal_cost = 2000.0
           room_cost = 5000.0  # Add other conditions here for different meal and room types
        
        elif  self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury":
           
           meal_cost = 1500.0
           room_cost = 5000.0 
        
        elif  self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single":
           
           meal_cost = 1000.0
           room_cost = 2500.0 
       
        elif  self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single":
           
           meal_cost = 1500.0
           room_cost = 2500.0 

        elif  self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single":
           
           meal_cost = 2000.0
           room_cost = 2500.0 


        elif  self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double":
           
           meal_cost = 2000.0
           room_cost = 3500.0       
        
        elif  self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double":
           
           meal_cost = 1500.0
           room_cost = 3500.0 

        elif  self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double":
           
           meal_cost = 2000.0
           room_cost = 3500.0 
        
        elif  self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Duplex":
           
           meal_cost = 2000.0
           room_cost = 4000.0       
        
        elif  self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Duplex":
           
           meal_cost = 1500.0
           room_cost = 4000.0 

        elif  self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Duplex":
           
           meal_cost = 2000.0
           room_cost = 4000.0 
        else:
           
           meal_cost = 0.0
           room_cost = 0.0       
    # Calculate total cost
        no_of_days = float(self.var_noofdays.get())
        total_cost = (meal_cost + room_cost) * no_of_days
    
    # Calculate tax and totals
        tax = total_cost * 0.1  # 10% tax
        total_with_tax = total_cost + tax
    
    # Format the results
        self.var_paidtax.set("Rs. " + str("%.2f" % tax))
        self.var_actualtotal.set("Rs. " + str("%.2f" % total_cost))
        self.var_total.set("Rs. " + str("%.2f" % total_with_tax))

            





if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()