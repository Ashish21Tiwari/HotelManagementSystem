from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from Hotel import HotelManagementSystem


def login():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\tiwari\Documents\HMS images\pic2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=100,width=340,height=440)

        img1 = Image.open(r"C:\Users\tiwari\Documents\HMS images\logo3.png")
        img1 = img1.resize((100,100), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        # Display image in a label
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=620, y=105, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=102)

        #lable
        username=lal=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=185,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=220)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

  #============== Icon Image ==============================
        img2 = Image.open(r"C:\Users\tiwari\Documents\HMS images\logo3.png")
        img2 = img2.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        # Display image in a label
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=540, y=258, width=25, height=25)

        img3 = Image.open(r"C:\Users\tiwari\Documents\HMS images\logo3.png")
        img3 = img3.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        # Display image in a label
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=540, y=323, width=25, height=25)

        #============ Login Btn ============
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #Registerbtn
        registerbtn=Button(frame,text="New User Resister",command=self.rigister_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="Black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=165)
        
        #forgetpassbtn
        forgetpassbtn=Button(frame,text="Forget Password",command=self.forget_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="Black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=388,width=160)
    
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "Assu" and self.txtpass.get() == "ram":
            messagebox.showinfo("Success", "Welcome to Hotel Royal.")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
                my_cursor = conn.cursor()

            # Fetch username and password from the database
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))

                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username & password")
                else:
                # Check if the user has admin access
                    open_main = messagebox.askyesno("Access Verification", "Access only for admin. Proceed?")
                
                    if open_main:  # Proceed only if 'Yes' is selected
                        self.new_window = Toplevel(self.root)
                        self.obj = HotelManagementSystem(self.new_window)
                
                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            conn.close()  # Ensure the connection is closed in case of an error



    #=========================== reset password =====================

    # def reset_password(self):
    #     try:
    #         # Check if the security question combobox still exists
    #         if self.combo_security_Q.winfo_exists():
    #             if self.combo_security_Q.get() == "Select":
    #                 messagebox.showerror("Error", "Select security question")
    #             elif self.txt_security.get() == "":
    #                 messagebox.showerror("Error", "Please enter the answer")
    #             elif self.txt_newpass.get() == "":
    #                 messagebox.showerror("Error", "Please enter the new password")
    #             else:
    #                 try:
    #                     conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
    #                     query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
    #                     value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get().strip())
    #                     my_cursor = conn.cursor()
                    
    #                     print("Executing Query with:", value)  # Debugging: Show the values being passed
                    
    #                     my_cursor.execute(query, value)  
    #                     row = my_cursor.fetchone()

    #                     if row is None:
    #                         print("No matching data found")  # Debugging: No match found in database
    #                         messagebox.showerror("Error", "Please enter the correct answer")
    #                     else:
    #                         print("Match found:", row)  # Debugging: Show the matching row data
    #                         update_query = "UPDATE register SET password=%s WHERE email=%s"
    #                         update_value = (self.txt_newpass.get(), self.txtuser.get())
    #                         my_cursor.execute(update_query, update_value)

    #                         conn.commit()
    #                         messagebox.showinfo("Success", "Your password has been reset successfully")
    #                     conn.close()

    #                 except mysql.connector.Error as err:
    #                     messagebox.showerror("Database Error", f"Error occurred: {str(err)}")
    #         else:
    #             messagebox.showerror("Error", "Security question window has been closed. Please reopen and try again.")
    
    #     except AttributeError:
    #         messagebox.showerror("Error", "Security question window is not available.")


    def reset_password(self):
        try:
            email = self.txtuser.get().strip().lower()
            security_question = self.combo_security_Q.get().strip().lower()
            security_answer = self.txt_security.get().strip().lower()
        
            if security_question == "select":
                messagebox.showerror("Error", "Select security question")
            elif security_answer == "":
                messagebox.showerror("Error", "Please enter the answer")
            elif self.txt_newpass.get() == "":
                messagebox.showerror("Error", "Please enter the new password")
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
                my_cursor = conn.cursor()
            
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (email, security_question, security_answer)
                print("Executing Query with:", value)  # Debugging: Show the values being passed
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
            
                if row is None:
                    print("No matching data found")  # Debugging: No match found in database
                    messagebox.showerror("Error", "Please enter the correct answer")
                else:
                    print("Match found:", row)  # Debugging: Show the matching row data
                    update_query = "UPDATE register SET password=%s WHERE email=%s"
                    update_value = (self.txt_newpass.get(), email)
                    my_cursor.execute(update_query, update_value)
                
                    conn.commit()
                    messagebox.showinfo("Success", "Your password has been reset successfully")
                conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error occurred: {str(err)}")


    
# ================= Forget Password ==========================

    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.txtuser.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please enter a valid username")
                else:
                    conn.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("340x450+500+100")

                    frame = Frame(self.root2, bg="green")
                    frame.place(x=0, y=0, width=500, height=450)

                    l = Label(self.root2, text="Forget Password", font=("times new roman", 15, "bold"), bg="Red",     fg="Yellow")
                    l.place(x=0, y=10, relwidth=1)

                    security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), fg="white", bg="black")
                    security_Q.place(x=50, y=80, width=250)

                    self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 13, "bold"),     state="readonly")
                    self.combo_security_Q["values"] = ("Select", "Your best friend's name", "Your mother's name", "Your nickname")
                    self.combo_security_Q.place(x=50, y=135, width=250)
                    self.combo_security_Q.current(0)

                    security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"),    bg="black", fg="white")
                    security_A.place(x=50, y=200, width=250)

                    self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                    self.txt_security.place(x=50, y=240, width=250)

                    newpass = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
                    newpass.place(x=50, y=280, width=250)

                    self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                    self.txt_newpass.place(x=50, y=320, width=250)

                    btn = Button(self.root2, text="Reset", command=self.reset_password, font=("times new roman", 15, "bold"), bg="red", fg="black")
                    btn.place(x=135, y=400)
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error occurred: {str(err)}")




#=========== Register Function ============================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTER")
        self.root.geometry("1500x800+0+0")

     #================= Variable ===================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #============= Bg image ===================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\tiwari\Documents\HMS images\pic2.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\tiwari\Documents\HMS images\pic9.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=420, height=480)

        #=============== Main Frame===================
        frame=Frame(self.root,bg="white")
        frame.place(x=470,y=100,width=750,height=480)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        
        #================== Lable Entry================

        #........................row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",13,"bold"))
        lname_entry.place(x=370,y=130,width=250)

        #........................row2
        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        self.txt.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #........................row3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your best friend name","Your mother name","Your nick name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",13))
        self.txt_security.place(x=370,y=270,width=250)

        #............................row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",13))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Cinfirm Password",font=("times new roman",15,"bold"),bg="white", fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",13,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        #============chech btn ========================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree The terms and conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)


        #=============== buttun ========================

        img = Image.open(r"C:\Users\tiwari\Documents\HMS images\logo4.jpg")
        img = img.resize((250,45), Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=50,y=420,width=200)

        img1 = Image.open(r"C:\Users\tiwari\Documents\HMS images\logo5.jpg")
        img1 = img1.resize((250,45), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
        b1.place(x=380,y=420,width=200)


        #=========== Funtion Declaration ===============================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root@9399633853", database="hms")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                   my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration successful", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)






if __name__ == "__main__":
    
    #login()
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()        
