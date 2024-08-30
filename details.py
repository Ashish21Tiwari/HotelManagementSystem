from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1137x480+222+225")




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
        LabelFrameleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("Arial Unicode MS",11,"bold"),padx=2)
        LabelFrameleft.place(x=5,y=50,width=450,height=300)


        #========================= Labels & Entry ==============================
        #Floor
        lbl_Floor=Label(LabelFrameleft,text="Floor",font=("Arial Unicode MS",9,"bold"),padx=2,pady=6)
        lbl_Floor.grid(row=0,column=0,sticky=W)

        self.var_Floor=StringVar()
        
        enty_Floor=ttk.Entry(LabelFrameleft,textvariable=self.var_Floor,width=25,font=("Arial Unicode MS",8,"bold"))
        enty_Floor.grid(row=0,column=1,sticky=W)

        #Room NO
        lbl_RoomNo=Label(LabelFrameleft,text="RoomNo",font=("Arial Unicode MS",9,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()
        
        enty_RoomNo=ttk.Entry(LabelFrameleft,textvariable=self.var_RoomNo,width=25,font=("Arial Unicode MS",8,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        #RoomType
        lbl_RoomType=Label(LabelFrameleft,text="RoomType",font=("Arial Unicode MS",9,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        
        enty_RoomType=ttk.Entry(LabelFrameleft,width=25,textvariable=self.var_RoomType,font=("Arial Unicode MS",8,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)

        
        #====================== Buttons ============================================
        btn_frame=Frame(LabelFrameleft,bd=2,relief=RIDGE)
        btn_frame.place(x=20,y=205,width=370,height=30)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)


        #======================== table Frame Search system ======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"))
        Table_Frame.place(x=500,y=50,width=620,height=300)


        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.details_table = ttk.Treeview(
        Table_Frame,
        columns=("Floor","RoomNo","RoomType"),
        xscrollcommand=scroll_x.set,  # Corrected here
        yscrollcommand=scroll_y.set   # Corrected here
        )

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("Floor",text="Floor")
        self.details_table.heading("RoomNo",text="RoomNo")
        self.details_table.heading("RoomType",text="RoomType")
        
        self.details_table["show"]="headings"

        self.details_table.column("Floor",width=100)
        self.details_table.column("RoomNo",width=100)
        self.details_table.column("RoomType",width=100)
        
        self.details_table.pack(fill=BOTH,expand=1)

        self.details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
#========================== Add Data ===============================
    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are requireed.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into details values(%s,%s,%s)",(
                                                                        self.var_Floor.get(),
                                                                        self.var_RoomNo.get(),
                                                                        self.var_RoomType.get()
                                                                        
                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully.",parent=self.root)        
            except Exception as es:
                messagebox.showinfo("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #========================= Fetch Data ==============================           
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root@9399633853",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
            self.details_table.delete(*self.details_table.get_children())
            for i in rows:
                self.details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============Getcorsur==========================
    def get_cursor(self,event=""):
        cursor_row=self.details_table.focus()
        content=self.details_table.item(cursor_row)
        row=content["values"]

        self.var_Floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2])


#========================== Update Table ============================
    def update(self):
        if self.var_Floor.get() == "":
            messagebox.showerror("Error", "Please enter the floor number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
                my_cursor = conn.cursor()
            # Corrected SQL query
                my_cursor.execute("""
                UPDATE details 
                SET RoomNo=%s, RoomType=%s
                WHERE Floor=%s
                               """, (
                 self.var_RoomNo.get(),
                 self.var_RoomType.get(),
                 self.var_Floor.get()
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
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

    #============== Reset Btn ==========================
    def reset(self):
        self.var_Floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set(""),
                   

                    

if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()