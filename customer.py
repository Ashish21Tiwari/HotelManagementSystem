from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1137x480+222+225")

        #============================== variable ==========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationaliry=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()

        #=============================== Title ===============================================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
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
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customers Details",font=("times new roman",12,"bold"),padx=2)
        LabelFrameleft.place(x=0,y=50,width=425,height=420)

        #========================= Labels & Entry ==============================
        #cust_ref
        lbl_cust_ref=Label(LabelFrameleft,text="Customer Ref",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        enty_ref=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_ref,font=("times new roman",10,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

        #cust_name
        lbl_cust_name=Label(LabelFrameleft,text="Customer Name:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        
        textcust_name=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_cust_name,font=("times new roman",10,"bold"))
        textcust_name.grid(row=1,column=1)

        #mother name
        lbl_mname=Label(LabelFrameleft,text="Mother Name:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_mname.grid(row=2,column=0,sticky=W)
        
        textmname=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_mother,font=("times new roman",10,"bold"))
        textmname.grid(row=2,column=1)

        #Gender combobox
        lbl_Gender=Label(LabelFrameleft,text="Gender:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_Gender.grid(row=3,column=0,sticky=W)
        
        combo_Gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_gender,font=("arial",10,"bold"),width=32,state="readonly")
        combo_Gender["value"]=("Male","Female","Other")
        combo_Gender.current(0)
        combo_Gender.grid(row=3,column=1)


        
        #postcode
        lbl_Postcode=Label(LabelFrameleft,text="Postcode:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_Postcode.grid(row=4,column=0,sticky=W)
        
        textPostcode=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_post,font=("times new roman",10,"bold"))
        textPostcode.grid(row=4,column=1)

        #mobile number
        lbl_Mnumber=Label(LabelFrameleft,text="Mobile Number:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_Mnumber.grid(row=5,column=0,sticky=W)
        
        textMnumber=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_mobile,font=("times new roman",10,"bold"))
        textMnumber.grid(row=5,column=1)

        # email
        lbl_email=Label(LabelFrameleft,text="Email:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_email.grid(row=6,column=0,sticky=W)
        
        textemail=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_email,font=("times new roman",10,"bold"))
        textemail.grid(row=6,column=1)

        # Nationality
        lbl_nationality=Label(LabelFrameleft,text="Nationality:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=7,column=0,sticky=W)
        
        
        combo_nationality=ttk.Combobox(LabelFrameleft,textvariable=self.var_nationaliry,font=("arial",10,"bold"),width=32,state="readonly")
        combo_nationality["value"]=("Indean","American","Japnies","Fransisy","Cineez","Bhootan","UAE","Others")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)


        # Idproof Combobox
        lbl_Idcbox=Label(LabelFrameleft,text="Id Proof Type:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_Idcbox.grid(row=8,column=0,sticky=W)
        
        
        combo_Idproof=ttk.Combobox(LabelFrameleft,textvariable=self.var_id_proof,font=("arial",10,"bold"),width=32,state="readonly")
        combo_Idproof["value"]=("Adharcard","Pancard","VoterId card","Mobile NO.","Passport","Driving licence")
        combo_Idproof.current(0)
        combo_Idproof.grid(row=8,column=1)


        # Id number
        lbl_Idnumber=Label(LabelFrameleft,text="Id Number:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_Idnumber.grid(row=9,column=0,sticky=W)
        
        textIdnumber=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_id_number,font=("times new roman",10,"bold"))
        textIdnumber.grid(row=9,column=1)

        # address
        lbl_address=Label(LabelFrameleft,text="Address:",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_address.grid(row=10,column=0,sticky=W)
        
        textaddress=ttk.Entry(LabelFrameleft,width=35,textvariable=self.var_address,font=("times new roman",10,"bold"))
        textaddress.grid(row=10,column=1)


        #====================== Button ============================================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=20,y=350,width=370,height=30)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #======================== table Frame Search system ======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=420)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_SearchBy=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=18,state="readonly")
        combo_SearchBy["value"]=("Mobile","Ref","Nationality")
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
        details_table.place(x=0,y=50,width=695,height=300)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_Details_Table = ttk.Treeview(
        details_table,
        columns=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "IdProof", "idnumber", "address"),
        xscrollcommand=scroll_x.set,  # Corrected here
        yscrollcommand=scroll_y.set   # Corrected here
        )

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
        self.cust_Details_Table.heading("IdProof",text="Id Proof")
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
        self.cust_Details_Table.column("IdProof",width=100)
        self.cust_Details_Table.column("idnumber",width=100)
        self.cust_Details_Table.column("address",width=100)

        self.cust_Details_Table.pack(fill=BOTH,expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    
    
    
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mobile.get()=="":
            messagebox.showerror("Error","All fields are requireed.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        self.var_ref.get(),
                                                                        self.var_cust_name.get(),
                                                                        self.var_mother.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_post.get(),
                                                                        self.var_mobile.get(),
                                                                        self.var_email.get(),
                                                                        self.var_nationaliry.get(),
                                                                        self.var_id_proof.get(),
                                                                        self.var_id_number.get(),
                                                                        self.var_address.get()
                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added.",parent=self.root)        
            except Exception as es:
                messagebox.showinfo("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customers")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
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
        self.var_nationaliry.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]) 

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:    
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853",     database="hms")
                my_cursor = conn.cursor()
                my_cursor.execute("""
                UPDATE customers 
                SET Name=%s, Mother=%s, Gender=%s, Post=%s, Mobile=%s, Email=%s, Nationality=%s, `Id Proof`=%s, `Id Number`=%s, Address=%s 
                WHERE Ref=%s
                                        """, (
                                                self.var_cust_name.get(),
                                                self.var_mother.get(),
                                                self.var_gender.get(),
                                                self.var_post.get(),
                                                self.var_mobile.get(),
                                                self.var_email.get(),
                                                self.var_nationaliry.get(),
                                                self.var_id_proof.get(),
                                                self.var_id_number.get(),
                                                self.var_address.get(),
                                                self.var_ref.get()   
                                           ))           
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Update", "Customer details have been updated successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
            finally:
               conn.close()

    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
        if mdelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853",     database="hms")
            my_cursor = conn.cursor()
            query="delete from customers where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""), 
        #self.var_nationaliry.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("") 

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

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
            query = f"SELECT * FROM customers WHERE {search_column} LIKE %s"
            my_cursor.execute(query, (f"%{search_value}%",))
        
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
                for i in rows:
                    self.cust_Details_Table.insert("", END, values=i)

            conn.commit()  # Commit changes (if any)
        except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
                conn.close()  # Ensure connection is closed  
        
            

           
                              



if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()       