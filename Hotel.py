from tkinter import *
from PIL import Image, ImageTk  # type: ignore # pip install pillow
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

 

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #============================ image ==================================
        # Open and resize image
        img1 = Image.open(r"C:\Users\tiwari\Documents\HMS images\pic1.jpg")
        img1 = img1.resize((1550, 170), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Display image in a label
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=170)

        #==================== Logo ============================================
        # Open and resize image
        img2 = Image.open(r"C:\Users\tiwari\Documents\HMS images\logo1.jpg")
        img2 = img2.resize((220, 170), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Display image in a label
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=220, height=170)

        #=============================== Title ===============================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
        
        #================================ Main Fram ===============================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #================================ Menu ====================================================
        lbl_title=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=220)

        #=============================== Button Menu ==============================================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=220,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        Room_btn=Button(btn_frame,text="ROOM",width=22,command=self.roombooking,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        Room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=22,command=self.details_room,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        Logout_btn=Button(btn_frame,text="LOGOUT",command=self.Logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        Logout_btn.grid(row=4,column=0,pady=1)

        #========================== Right Side Image ======================================
        img3 = Image.open(r"C:\Users\tiwari\Documents\HMS images\pic4.jpg")
        img3 = img3.resize((1310, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Display image in a label
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=220,y=0, width=1310, height=590)

        #========================= Down Side Image =======================================
        img4 = Image.open(r"C:\Users\tiwari\Documents\HMS images\pic3.jpg")
        img4 = img4.resize((222, 190), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Display image in a label
        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0,y=225, width=222, height=190)

        img5 = Image.open(r"C:\Users\tiwari\Documents\HMS images\pic2.jpg")
        img5 = img5.resize((222, 180), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        # Display image in a label
        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0,y=360, width=222, height=180)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window) 

    def Logout(self):
        self.root.destroy()    



if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()

