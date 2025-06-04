from tkinter import ttk, Tk, Frame, Label, Button, Entry, filedialog, Toplevel
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime, timedelta
import sqlite3
import shutil
import os
# PDF generation
from reportlab.lib.pagesizes import A7,landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics

conn = sqlite3.connect(r"C:\Users\HP\Desktop\gg\spaday_04.db")
cursor = conn.cursor()

#--------------- หน้า log in --------------------
window = Tk()
window.title("Tkinter")
window.configure(bg="#ecb1b1")
window.geometry("1920x1080") 

img = Image.open('07ab5de1-6c63-4daf-b1b8-6bfecf0e1cec.jpg')
photo = ImageTk.PhotoImage(img)
Label(image=photo).pack()

# หน้า About US
def aboutus():
    global Aboutwindow
    Aboutwindow = Toplevel()
    Aboutwindow.title("About Us")
    Aboutwindow.configure(bg="#ecb1b1")
    Aboutwindow.geometry("1920x1080")  # อันเดิมคือ 1950x1080

    imgabout = Image.open('aboutus.jpg')
    photo = ImageTk.PhotoImage(imgabout)
    label = Label(Aboutwindow, image=photo)
    label.image = photo  # เก็บการอ้างอิงถึงรูปภาพ
    label.pack()  # เพิ่มคำสั่ง pack เพื่อแสดง Label

#ปุ่ม about
Button_about = customtkinter.CTkButton(master=window,text="About Us",command=aboutus,font=("Georgia", 16),
    text_color="#000000",hover=True,hover_color="#949494",height=50,width=150,
    corner_radius=30,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
Button_about.place(x=1110, y=680)

# ฟังก์ชั่น login
def login():
    username = Entry_username.get()
    password = Entry_password.get()
    correct_credentials = {
        "staff": "1234",
        "admin": "12345678"
    }
    # ตรวจสอบว่าชื่อผู้ใช้มีอยู่ใน dictionary และรหัสผ่านตรงกัน
    if username in correct_credentials and password == correct_credentials[username]:
        messagebox.showinfo("Success", "Login successful!")
        window.withdraw()  # ซ่อนหน้าต่างล็อกอิน
        if username == "staff":
            open_main()  # เปิดหน้าต่างเมนูหลักสำหรับพนักงาน
        elif username == "admin":
            open_admin()  # เปิดหน้าต่างอื่นสำหรับแอดมิน
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# ปุ่ม log in
Button_id1 = customtkinter.CTkButton(master=window,text="Log In",command=login,font=("Georgia", 16),
    text_color="#000000",hover=True,hover_color="#949494",height=50,width=150,
    corner_radius=30,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
Button_id1.place(x=920, y=680)

#ช่องกรอก user
Entry_username = customtkinter.CTkEntry(master=window,placeholder_text="username",placeholder_text_color="#454545",
    font=("Georgia", 16),text_color="#000000",height=60,width=400,
    border_width=1,corner_radius=25,border_color="#f2d8d7",
    bg_color="#f2d8d7",fg_color="#ffffff",)
Entry_username.place(x=890, y=480)

def focus_password(event=None):
    Entry_password.focus()  # ย้ายโฟกัสไปที่ช่องรหัสผ่าน

Entry_username.bind("<Return>", focus_password)

# ช่องกรอกรหัส
Entry_password = customtkinter.CTkEntry(master=window,placeholder_text="password",placeholder_text_color="#454545",
    font=("Georgia", 16),text_color="#000000",height=60,width=400,border_width=1,corner_radius=25,
    border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",show="•"  )
Entry_password.place(x=890, y=580)

def on_enter(event=None):
    login()
    Entry_username.delete(0, 'end')
    Entry_password.delete(0, 'end')

Entry_password.bind("<Return>", on_enter)

def logout(master):
    master.withdraw()
    window.deiconify()
        
# ------------------ หน้าหลัก staff menu --------------------------
def open_main():
    global staff_main_menu
    global master, source
    staff_main_menu = Toplevel(window)
    staff_main_menu.title("Main Menu")
    staff_main_menu.configure(bg="#f2d8d7")
    staff_main_menu.geometry("1950x1080")

    img1 = Image.open('main.jpg')
    photo1 = ImageTk.PhotoImage(img1)
    label_image = Label(staff_main_menu, image=photo1)
    label_image.photo = photo1  # เก็บอ้างอิง
    label_image.place(x=-15, y=0)

    master=staff_main_menu

    # ปุ่ม service
    Button_id4 = customtkinter.CTkButton(master=master,command=service,
            text="service",font=("Georgia", 25),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=250,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id4.place(x=25, y=250)
    
    # ปุ่ม member
    Button_id4 = customtkinter.CTkButton(master=master,command=member,
            text="membership",font=("Georgia", 25),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=250,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id4.place(x=25, y=320)
    
    # ปุ่ม booking
    Button_id5 = customtkinter.CTkButton(master=master,command=booking,
            text="booking",font=("Georgia", 25),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=250,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id5.place(x=25, y=390)

    # ปุ่ม receipt
    Button_id4 = customtkinter.CTkButton(master=master,command=show_receipt,
            text="receipt",font=("Georgia", 25),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=250,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id4.place(x=25, y=460)

    # ปุ่ม logout
    Button_id6 = customtkinter.CTkButton(master=master,command=lambda: logout(master),
            text="log out",font=("Georgia", 20),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=100,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id6.place(x=100, y=630)


# ------------------ หน้าหลัก admin menu --------------------------
def open_admin():
    global admin_main_menu
    global master , source
    admin_main_menu = Toplevel(window)
    admin_main_menu.title("Your Spa")
    admin_main_menu.configure(bg="#f2d8d7")
    admin_main_menu.geometry("1950x1080")

    img1 = Image.open('admin.jpg')
    photo1 = ImageTk.PhotoImage(img1)
    label_image = Label(admin_main_menu, image=photo1)
    label_image.photo = photo1  # เก็บอ้างอิง
    label_image.place(x=-15, y=0)

    master=admin_main_menu

    # ปุ่ม service
    Button_id2 = customtkinter.CTkButton(master=master,command=service,
        text="service",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=250,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id2.place(x=25, y=190)

    # ปุ่ม staff
    Button_id3 = customtkinter.CTkButton(master=master,command=staff,
        text="staff",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=250,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id3.place(x=25,y=260)

     # ปุ่ม member
    Button_id4 = customtkinter.CTkButton(master=master,command=member,
            text="membership",font=("Georgia", 25),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=250,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id4.place(x=25, y=330)  

    # ปุ่ม booking
    Button_id5 = customtkinter.CTkButton(master=master,command=booking,
        text="booking",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=250,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id5.place(x=25, y=400)

    # ปุ่ม receipt
    Button_id4 = customtkinter.CTkButton(master=master,command=show_receipt,
            text="receipt",font=("Georgia", 25),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=250,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id4.place(x=25, y=470)

    # ปุ่ม report
    Button_id5 = customtkinter.CTkButton(master=master,command=show_report,
            text="report",font=("Georgia", 25),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=250,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id5.place(x=25, y=540)

    # ปุ่ม logout
    Button_id6 = customtkinter.CTkButton(master=master,command=lambda: logout(master),
            text="log out",font=("Georgia", 20),text_color="#000000",
            hover=True,hover_color="#949494",height=50,width=100,
            border_width=2,corner_radius=20,border_color="#f2d8d7",
            bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_id6.place(x=100, y=620)


#------------------- หน้าหลักของ service ----------------------
def service():
    global servicewindow
    
    servicewindow = Toplevel()
    servicewindow.title("Service Menu")
    servicewindow.geometry("1950x1080")
    servicewindow.configure(bg="#f2d8d7")
    
    img2 = Image.open('service.jpg')
    photo2 = ImageTk.PhotoImage(img2)
    label_image = Label(servicewindow, image=photo2)
    label_image.photo = photo2  # เก็บอ้างอิง
    label_image.place(x=-15, y=0)

    Label(servicewindow, text="service", font=("Georgia", 20), bg="#f2d8d7", fg="#000000").place(x=35, y=160)

# ปุ่มเพิ่มข้อมูล service
    Button_add = customtkinter.CTkButton(master=servicewindow,command=add,
        text="add",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_add.place(x=25, y=205)

# ปุ่มอัปเดตข้อมูล service
    Button_update = customtkinter.CTkButton(master=servicewindow,command=update,
        text="update",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50, width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_update.place(x=25, y=265)

# ปุ่มลบข้อมูล service
    Button_delete = customtkinter.CTkButton(master=servicewindow,command=delete,
        text="delete",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_delete.place(x=25, y=325)

# ปุ่ม show รูป service
    Button_delete = customtkinter.CTkButton(master=servicewindow,command=show_service,
        text="service",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_delete.place(x=25, y=385)

# ปุ่ม show รูป staff
    Button_delete = customtkinter.CTkButton(master=servicewindow,command=show_staff,
        text="staff",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_delete.place(x=25, y=445)

# ปุ่มย้อนกลับไปหน้าเมนู
    Button_gomenu = customtkinter.CTkButton(master=servicewindow,command=lambda: servicewindow_go_menu(master),
        text="back",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=80,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_gomenu.place(x=25, y=700)


#ฟังชั่นย้อนกลับไปหน้าเมนูหลัก
def servicewindow_go_menu(master):
    servicewindow.withdraw()
    master.deiconify()
        
def showservice():
    global windowshow_service
    # สร้างหน้าต่างใหม่
    windowshow_service =Toplevel()
    windowshow_service.title("Add New Service")
    windowshow_service.geometry("1950x1080")
    windowshow_service.configure(bg="#f2d8d7")  # กำหนดสีพื้นหลังของหน้าต่างหลัก
    imgshowservice = Image.open('serviceshow.jpg')
    photo = ImageTk.PhotoImage(imgshowservice)
    label = Label(windowshow_service, image=photo)
    label.image = photo  # เก็บการอ้างอิงถึงรูปภาพ
    label.pack()  # เพิ่มคำสั่ง pack เพื่อแสดง Label


#หน้า add service
def add():
    global windowadd
    
    servicewindow.withdraw()
    
    windowadd = Toplevel()
    windowadd.title("Add New Service")
    windowadd.geometry("1950x1080")
    windowadd.configure(bg="#f2d8d7")

    img6 = Image.open('showservice.jpg')
    photo6 = ImageTk.PhotoImage(img6)
    label_image = Label(windowadd, image=photo6)
    label_image.photo = photo6 
    label_image.place(x=-15, y=0)

    # สร้างตารางชื่อ servicetable
    columns = ("ID", "Service Name", "Price", "Duration")
    servicetable = ttk.Treeview(windowadd, columns=columns, show='headings',height=15)
    column_widths = {
        "ID": 40,
        "Service Name": 200,
        "Price": 80,
        "Duration": 80 }
    for col in columns:
        servicetable.heading(col, text=col)
        servicetable.column(col, width=column_widths[col])

    servicetable.place(x=1110, y=100)

    # ดึงข้อมูลจาก sql ตาราง ourservices
    cursor.execute("SELECT * FROM ourservices")
    rows = cursor.fetchall()

    # เพิ่มข้อมูลลงใน servicetable
    for row in rows:
        servicetable.insert("", "end", values=row)

    # ฟังก์ชันรีเฟรชข้อมูลใน servicetable
    def refresh_service_table_add():
        for row in servicetable.get_children():
            servicetable.delete(row)

        cursor.execute("SELECT * FROM ourservices")
        rows = cursor.fetchall()

        for row in rows:
            servicetable.insert("", "end", values=row)

    # ช่องกรอกชื่อบริการ
    Entry_servicename = customtkinter.CTkEntry(master=windowadd,
        placeholder_text="new service name",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_servicename.place(x=1170, y=470)

    # ช่องกรอกราคา
    Entry_price = customtkinter.CTkEntry(master=windowadd,
        placeholder_text="price (baht)",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_price.place(x=1170, y=540)

    # ช่องกรอกระยะเวลา
    Entry_duration = customtkinter.CTkEntry(master=windowadd,
        placeholder_text="duration (min)",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_duration.place(x=1170, y=610)

    # ฟังก์ชันเมื่อกดปุ่ม "Confirm"
    def on_confirm(event=None):
        # รับค่าจากช่องกรอก
        servicename = Entry_servicename.get()
        try:
            price = Entry_price.get()
            duration = Entry_duration.get()
        except ValueError:
            return

        # เรียกใช้ฟังก์ชัน add_service()
        add_service(servicename, price, duration)
        # เรียกใช้ฟังก์ชัน refresh service table
        refresh_service_table_add()

        # เคลียร์ข้อมูลในช่องกรอกเพื่อให้กรอกข้อมูลใหม่ได้
        Entry_servicename.delete(0, 'end')
        Entry_price.delete(0, 'end')
        Entry_duration.delete(0, 'end')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องต่อไป
    Entry_servicename.bind("<Return>", focus_next_widget)
    Entry_price.bind("<Return>", focus_next_widget)
    Entry_duration.bind("<Return>", on_confirm)  # กด Enter ในช่องระยะเวลาเพื่อยืนยันข้อมูล

    Button_ok = customtkinter.CTkButton(master=windowadd,command=on_confirm,  
        text="confirm",font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_ok.place(x=1190, y=680)

    Button_back = customtkinter.CTkButton(master=windowadd,command=go_back1,  
        text="back to menu",font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_back.place(x=1320, y=680)

def go_back1():
    windowadd.withdraw()
    servicewindow.deiconify()

def add_service(servicename, price, duration):
    cursor.execute('INSERT INTO ourservices (name, price, duration) VALUES (?, ?, ?)', (servicename, price, duration))
    conn.commit()

#หน้า delete service
def delete():
    global windowdelete
    
    # ปิดหน้าต่างบริการ
    servicewindow.withdraw()
    
    # สร้างหน้าต่างใหม่สำหรับเพิ่มบริการ
    windowdelete = Toplevel()
    windowdelete.title("Delete Existing Service")
    windowdelete.geometry("1950x1080")
    windowdelete.configure(bg="#f2d8d7")

    img6 = Image.open('showservice.jpg')
    photo6 = ImageTk.PhotoImage(img6)
    label_image = Label(windowdelete, image=photo6)
    label_image.photo = photo6 
    label_image.place(x=-15, y=0)

    #ตาราง ourservices จาก sql
    columns = ("ID", "Service Name", "Price", "Duration")
    servicetable = ttk.Treeview(windowdelete, columns=columns, show='headings', height=20)  # กำหนดให้แสดง 20 แถว
    column_widths = {
        "ID": 40,
        "Service Name": 200,
        "Price": 80,
        "Duration": 80 }
    for col in columns:
        servicetable.heading(col, text=col)
        servicetable.column(col, width=column_widths[col])
    servicetable.place(x=1110, y=100)
    # ดึงข้อมูลจาก sql ตาราง ourservices
    cursor.execute("SELECT * FROM ourservices")
    rows = cursor.fetchall()
    # เพิ่มข้อมูลลงใน servicetable
    for row in rows:
        servicetable.insert("", "end", values=row)

    # ฟังก์ชันรีเฟรชตาราง service
    def refresh_service_table_delete():
        for row in servicetable.get_children():
            servicetable.delete(row)

        cursor.execute("SELECT * FROM ourservices")
        rows = cursor.fetchall()

        for row in rows:
            servicetable.insert("", "end", values=row)

    Entry_delete = customtkinter.CTkEntry(master=windowdelete,
        placeholder_text="service id",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1, corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_delete.place(x=1170, y=550)
    
    def on_confirm(event=None):
        try:
            delete = int(Entry_delete.get())
        except ValueError:
            return
        delete_service(delete)
        refresh_service_table_delete()
        Entry_delete.delete(0, 'end')
        
    Entry_delete.bind("<Return>", on_confirm)  # กด Enter ในช่องระยะเวลาเพื่อยืนยันข้อมูล

    Button_ok = customtkinter.CTkButton(master=windowdelete,text="confirm",command=on_confirm, 
        font=("Georgia", 14),text_color="#000000", hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_ok.place(x=1190, y=620)

    Button_back = customtkinter.CTkButton(master=windowdelete,text="back to menu",command=go_back2, 
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_back.place(x=1320, y=620)

def go_back2():
    windowdelete.withdraw()
    servicewindow.deiconify()
   
def delete_service(delete):
    cursor.execute(''' DELETE FROM ourservices WHERE service_id = ? ''', (delete,))
    conn.commit()

#หน้าอัปเดต service
def update():
    global windowupdate

    servicewindow.withdraw()

    windowupdate = Toplevel()
    windowupdate.title("Edit Existing Service")
    windowupdate.geometry("1950x1080")
    windowupdate.configure(bg="#f2d8d7")

    img6 = Image.open('showservice.jpg')
    photo6 = ImageTk.PhotoImage(img6)
    label_image = Label(windowupdate, image=photo6)
    label_image.photo = photo6 
    label_image.place(x=-15, y=0)

    # สร้างตารางชื่อ servicetable
    columns = ("ID", "Service Name", "Price", "Duration")
    servicetable = ttk.Treeview(windowupdate, columns=columns, show='headings' , height = 14 )
    columns_width = {
        "ID": 40,
        "Service Name": 200,
        "Price": 80,
        "Duration": 80 }
    for col in columns:
        servicetable.heading(col, text=col)
        servicetable.column(col, width=columns_width[col])
        servicetable.place(x=1110, y=60)
    # ดึงข้อมูลจาก sql ตาราง ourservices
    cursor.execute("SELECT * FROM ourservices")
    rows = cursor.fetchall()
    # เพิ่มข้อมูลลงใน servicetable
    for row in rows:
        servicetable.insert("", "end", values=row)

    def refresh_service_table_update():
        for row in servicetable.get_children():
            servicetable.delete(row)

        cursor.execute("SELECT * FROM ourservices")
        rows = cursor.fetchall()

        for row in rows:
            servicetable.insert("", "end", values=row)

    # ช่องกรอก service id 
    Entry_service_id = customtkinter.CTkEntry(master=windowupdate,placeholder_text="service id",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_service_id.place(x=1170, y=390)

    # ช่องกรอกชื่อบริการที่จะเปลี่ยน
    Entry_service_name = customtkinter.CTkEntry(master=windowupdate,placeholder_text="new service name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_service_name.place(x=1170, y=460)

    # ช่องกรอกราคาที่จะเปลี่ยน
    Entry_service_price = customtkinter.CTkEntry(master=windowupdate,placeholder_text="new price",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_service_price.place(x=1170, y=530)

    # ช่องกรอกระยะเวลา
    Entry_service_duration = customtkinter.CTkEntry(master=windowupdate,placeholder_text="new duration (min)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_service_duration.place(x=1170, y=600)

    # ฟังก์ชันเมื่อกดปุ่ม "Confirm"
    def on_confirm_update(event=None):
        service_id = Entry_service_id.get()
        name = Entry_service_name.get()
        price = Entry_service_price.get()
        duration = Entry_service_duration.get()

        update_service(service_id, name, price, duration)
        refresh_service_table_update()

        Entry_service_id.delete(0, 'end')
        Entry_service_name.delete(0, 'end')
        Entry_service_price.delete(0, 'end')
        Entry_service_duration.delete(0, 'end')

    Button_confirm_update = customtkinter.CTkButton(master=windowupdate,text="confirm",command=on_confirm_update, 
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_confirm_update.place(x=1190, y=680)

    def focus_next_widget(event):
            event.widget.tk_focusNext().focus()
            return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องถัดไป
    Entry_service_id.bind("<Return>", focus_next_widget)
    Entry_service_name.bind("<Return>", focus_next_widget)
    Entry_service_price.bind("<Return>", focus_next_widget)
    Entry_service_duration.bind("<Return>", on_confirm_update)  # กด Enter ในช่องระยะเวลาเพื่อยืนยันข้อมูล

    Button_back = customtkinter.CTkButton(master=windowupdate,text="back to menu",
        command=go_back3,font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_back.place(x=1320, y=680)

def go_back3():
    windowupdate.withdraw()
    servicewindow.deiconify()

def update_service(service_id, name, price, duration):
    if name:
        cursor.execute('''
        UPDATE ourservices
        SET name = ?
        WHERE service_id = ?
        ''', (name, service_id))
    if price:
        cursor.execute('''
        UPDATE ourservices
        SET price = ?
        WHERE service_id = ?
        ''', (price, service_id))
    if duration:
        cursor.execute('''
        UPDATE ourservices
        SET duration = ?
        WHERE service_id = ?
        ''', (duration, service_id))
    conn.commit()


#------------------------ หน้าต่าง staff -------------------------
def staff():
    global staffwindow
    staffwindow = Toplevel()
    staffwindow.title("Staff Menu")
    staffwindow.geometry("1950x1080")
    staffwindow.configure(bg="#f2d8d7")
    img3 = Image.open('staff.jpg')
    photo3 = ImageTk.PhotoImage(img3)
    label_image = Label(staffwindow, image=photo3)
    label_image.photo = photo3  # เก็บอ้างอิง
    label_image.place(x=-15, y=0)

    Label(staffwindow, text="staff", font=("Georgia", 20), bg="#f2d8d7", fg="#000000").place(x=35, y=160)
    #ปุ่ม add staff
    Button_add = customtkinter.CTkButton(master=staffwindow,text="add",command=addstaff,
        font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",
        height=50,width=120,border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_add.place(x=25, y=205)
    #ปุ่ม update staff
    Button_staffupdate = customtkinter.CTkButton(master=staffwindow,text="update",command=update_staff,
        font=("Georgia", 25),text_color="#000000", hover=True,hover_color="#949494",
        height=50,width=120,border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_staffupdate.place(x=25, y=265)

    #ปุ่ม ลบ staff
    Button_staffdelete = customtkinter.CTkButton(master=staffwindow,text="delete",command=delete_staff,
        font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",
        height=50,width=120,border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_staffdelete.place(x=25, y=325)

    #ปุ่มย้อนกลับ
    Button_staffwindow_go_menu = customtkinter.CTkButton(master=staffwindow,text="back",command=lambda: staffwindow_go_menu(master),
        font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",
        height=50,width=80,border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_staffwindow_go_menu.place(x=25, y=700)

def staffwindow_go_menu(master):
    staffwindow.withdraw()
    master.deiconify()


#หน้าเพิ่มstaff
def addstaff():
    global windowadd_staff

    # ปิดหน้าต่างบริการ
    staffwindow.withdraw()

    # สร้างหน้าต่างใหม่สำหรับเพิ่มพนักงาน
    windowadd_staff = Toplevel()
    windowadd_staff.title("Add New Staff Information")
    windowadd_staff.geometry("1950x1080")
    windowadd_staff.configure(bg="#f2d8d7")

    title_label = ttk.Label(windowadd_staff, text="Add New Staff Information", font=("Georgia", 16))
    title_label.place(x=540, y=40)
    columns = ("staff_id", "first_name", "last_name", "id_card", "email", "birthdate", "phone", "position")
    stafftable = ttk.Treeview(windowadd_staff, columns=columns, show='headings',height=30)
    for col in columns:
        stafftable.heading(col, text=col)
        stafftable.column(col, width=100)
        stafftable.place(x=540, y=80)

    # ดึงข้อมูลจาก sql ตาราง staff
    cursor.execute("SELECT * FROM staff")
    rows = cursor.fetchall()

    # เพิ่มข้อมูลลงใน stafftable
    for row in rows:
        stafftable.insert("", "end", values=row)
    
    def refresh_staff_table_add():
        for row in stafftable.get_children():
            stafftable.delete(row)
    
        cursor.execute("SELECT * FROM staff")
        rows = cursor.fetchall()
    
        for row in rows:
            stafftable.insert("", "end", values=row)

    # ช่องกรอกข้อมูลพนักงานต่างๆ
    Entry_firstname = customtkinter.CTkEntry(master=windowadd_staff,placeholder_text="name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_firstname.place(x=100, y=100)

    Entry_lastname = customtkinter.CTkEntry(master=windowadd_staff,placeholder_text="last name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_lastname.place(x=100, y=170)

    Entry_idcard = customtkinter.CTkEntry(master=windowadd_staff,placeholder_text="id card",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_idcard.place(x=100, y=240)

    Entry_email = customtkinter.CTkEntry(master=windowadd_staff,placeholder_text="email",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_email.place(x=100, y=310)

    Entry_birthdate = customtkinter.CTkEntry(
        master=windowadd_staff,placeholder_text="birthdate(YY-MM-DD)",placeholder_text_color="#454545",font=("Georgia", 14),
        text_color="#000000",height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",
    )
    Entry_birthdate.place(x=100, y=380)

    Entry_phone = customtkinter.CTkEntry(
        master=windowadd_staff,placeholder_text="phone",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",
    )
    Entry_phone.place(x=100, y=450)

    Entry_position = customtkinter.CTkEntry(
        master=windowadd_staff,placeholder_text="position",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",
    )
    Entry_position.place(x=100, y=520)

    def on_confirm(event=None):
        # รับค่าจากช่องกรอก
        first_name = Entry_firstname.get()
        last_name = Entry_lastname.get()
        id_card = Entry_idcard.get()
        email = Entry_email.get()
        birthdate = Entry_birthdate.get()
        phone = Entry_phone.get()
        position = Entry_position.get()

        staffadd(first_name, last_name, id_card, email, birthdate, phone, position)
        refresh_staff_table_add()

        # เคลียร์ข้อมูลในช่องกรอกเพื่อให้สามารถกรอกข้อมูลใหม่ได้
        Entry_firstname.delete(0, 'end')
        Entry_lastname.delete(0, 'end')
        Entry_idcard.delete(0, 'end')
        Entry_email.delete(0, 'end')
        Entry_birthdate.delete(0, 'end')
        Entry_phone.delete(0, 'end')
        Entry_position.delete(0, 'end')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องถัดไป
    Entry_firstname.bind("<Return>", focus_next_widget)
    Entry_lastname.bind("<Return>", focus_next_widget)
    Entry_idcard.bind("<Return>", focus_next_widget)
    Entry_email.bind("<Return>", focus_next_widget)
    Entry_birthdate.bind("<Return>", focus_next_widget)
    Entry_phone.bind("<Return>", focus_next_widget)
    Entry_position.bind("<Return>", on_confirm)  # กด Enter ในช่อง position เพื่อยืนยันข้อมูล


    # ปุ่มยืนยัน
    Button_addstaff_ok = customtkinter.CTkButton(master=windowadd_staff,text="confirm",command=on_confirm,
        font=("Georgia", 14),  text_color="#000000",hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_addstaff_ok.place(x=120, y=600)

    Button_addstaff_go_back = customtkinter.CTkButton(master=windowadd_staff,text="back to menu",command=go_back4, 
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",height=40,
        width=120,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_addstaff_go_back.place(x=250, y=600)

def go_back4():
    windowadd_staff.withdraw()
    staffwindow.deiconify()

def staffadd(first_name, last_name, id_card, email, birthdate, phone, position):
    cursor.execute('''
    INSERT INTO staff (first_name, last_name, id_card, email, birthdate, phone, position) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (first_name, last_name, id_card, email, birthdate, phone, position))
    conn.commit()

#หน้าอัปเดต staff
def update_staff():
    global updatestaffwindow
    # ปิดหน้าต่างบริการ
    staffwindow.withdraw()
    
    # สร้างหน้าต่างใหม่สำหรับแก้ไขข้อมูลพนักงาน
    updatestaffwindow = Toplevel()
    updatestaffwindow.title("Update Existing Staff Information")
    updatestaffwindow.geometry("1950x1080")
    updatestaffwindow.configure(bg="#f2d8d7")

    title_label = ttk.Label(updatestaffwindow, text="Edit Staff Information", font=("Georgia", 16))
    title_label.place(x=540, y=40)
    columns = ("staff_id", "first_name", "last_name", "id_card", "email", "birthdate", "phone", "position")
    stafftable = ttk.Treeview(updatestaffwindow, columns=columns, show='headings',height=30)
    for col in columns:
        stafftable.heading(col, text=col)
        stafftable.column(col, width=100)
        stafftable.place(x=540, y=70)
    cursor.execute("SELECT * FROM staff")
    rows = cursor.fetchall()
    for row in rows:
        stafftable.insert("", "end", values=row)

    def refresh_staff_table_update():
        for row in stafftable.get_children():
            stafftable.delete(row)
        cursor.execute("SELECT * FROM staff")
        rows = cursor.fetchall()
        for row in rows:
            stafftable.insert("", "end", values=row)

    # ช่องกรอกข้อมูลพนักงานต่างๆ
    Entry_staff_id = customtkinter.CTkEntry(master=updatestaffwindow,placeholder_text="staff id",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_staff_id.place(x=100, y=80)

    Entry_firstname = customtkinter.CTkEntry(master=updatestaffwindow,
        placeholder_text="name",placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_firstname.place(x=100, y=150)

    Entry_lastname = customtkinter.CTkEntry(master=updatestaffwindow,placeholder_text="last name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_lastname.place(x=100, y=220)

    Entry_idcard = customtkinter.CTkEntry(master=updatestaffwindow,placeholder_text="id card",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_idcard.place(x=100, y=290)

    Entry_email = customtkinter.CTkEntry(master=updatestaffwindow,placeholder_text="email",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_email.place(x=100, y=360)

    Entry_birthdate = customtkinter.CTkEntry(master=updatestaffwindow,placeholder_text="birthdate (YY-MM-DD)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,
        width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_birthdate.place(x=100, y=430)

    Entry_phone = customtkinter.CTkEntry(master=updatestaffwindow,placeholder_text="phone",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,border_width=1,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_phone.place(x=100, y=500)

    Entry_position = customtkinter.CTkEntry(master=updatestaffwindow,placeholder_text="position",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,border_width=1,
        corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff", )
    Entry_position.place(x=100, y=570)

    def on_confirm_updatestaff(event=None):
        # รับค่าจากช่องกรอก
        staff_id = Entry_staff_id.get()
        first_name = Entry_firstname.get()
        last_name = Entry_lastname.get()
        id_card = Entry_idcard.get()
        email = Entry_email.get()
        birthdate = Entry_birthdate.get()
        phone = Entry_phone.get()
        position = Entry_position.get()

        # เรียกใช้ฟังก์ชัน add_service()
        staffupdate(staff_id,first_name, last_name, id_card, email, birthdate, phone, position)
        refresh_staff_table_update()

        # เคลียร์ข้อมูลในช่องกรอกเพื่อให้สามารถกรอกข้อมูลใหม่ได้
        Entry_staff_id.delete(0, 'end')
        Entry_firstname.delete(0, 'end')
        Entry_lastname.delete(0, 'end')
        Entry_idcard.delete(0, 'end')
        Entry_email.delete(0, 'end')
        Entry_birthdate.delete(0, 'end')
        Entry_phone.delete(0, 'end')
        Entry_position.delete(0, 'end')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องถัดไป
    Entry_staff_id.bind("<Return>", focus_next_widget)
    Entry_firstname.bind("<Return>", focus_next_widget)
    Entry_lastname.bind("<Return>", focus_next_widget)
    Entry_idcard.bind("<Return>", focus_next_widget)
    Entry_email.bind("<Return>", focus_next_widget)
    Entry_birthdate.bind("<Return>", focus_next_widget)
    Entry_phone.bind("<Return>", focus_next_widget)
    Entry_position.bind("<Return>", on_confirm_updatestaff)  # กด Enter ในช่อง position เพื่อยืนยันข้อมูล

    # ปุ่มยืนยัน
    Button_udstaffok = customtkinter.CTkButton(master=updatestaffwindow,text="confirm",command=on_confirm_updatestaff,  
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_udstaffok.place(x=120, y=650)

    Button_udstaff_back = customtkinter.CTkButton(master=updatestaffwindow,text="back to menu",command=go_back5, 
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_udstaff_back.place(x=250, y=650)

def go_back5():
    updatestaffwindow.withdraw()
    staffwindow.deiconify()

def staffupdate(staff_id,first_name, last_name, id_card, email, birthdate, phone, position):
    if first_name:
        cursor.execute('''
        UPDATE staff
        SET first_name = ?
        WHERE staff_id = ?
        ''', (first_name, staff_id))
    if last_name:
        cursor.execute('''
        UPDATE staff
        SET last_name = ?
        WHERE staff_id = ?
        ''', (last_name, staff_id))
    if id_card:
        cursor.execute('''
        UPDATE staff
        SET id_card = ?
        WHERE staff_id = ?
        ''', (id_card, staff_id))
    if email:
        cursor.execute('''
        UPDATE staff
        SET email = ?
        WHERE staff_id = ?
        ''', (email, staff_id))
    if birthdate:
        cursor.execute('''
        UPDATE staff
        SET birthdate = ?
        WHERE staff_id = ?
        ''', (birthdate, staff_id))
    if phone:
        cursor.execute('''
        UPDATE staff
        SET phone = ?
        WHERE staff_id = ?
        ''', (phone, staff_id))
    if position:
        cursor.execute('''
        UPDATE staff
        SET position = ?
        WHERE staff_id = ?
        ''', (position, staff_id))

    conn.commit()

#หน้าลบ staff
def delete_staff():
    global delete_staffwindow

    staffwindow.withdraw()
    
    delete_staffwindow = Toplevel()
    delete_staffwindow.title("Delete Existing Staff")
    delete_staffwindow.geometry("1950x1080")
    delete_staffwindow.configure(bg="#f2d8d7")

    title_label = ttk.Label(delete_staffwindow, text="Enter Staff ID to Delete Staff Information", font=("Georgia", 16))
    title_label.place(x=560, y=40)
    columns = ("staff_id", "first_name", "last_name", "id_card", "email", "birthdate", "phone", "position")
    stafftable = ttk.Treeview(delete_staffwindow, columns=columns, show='headings',height=24)
    for col in columns:
        stafftable.heading(col, text=col)
        stafftable.column(col, width=100)
        stafftable.place(x=340, y=80)
    cursor.execute("SELECT * FROM staff")
    rows = cursor.fetchall()
    for row in rows:
        stafftable.insert("", "end", values=row)


    def refresh_staff_table_delete():
        for row in stafftable.get_children():
            stafftable.delete(row)
        cursor.execute("SELECT * FROM staff")
        rows = cursor.fetchall()
        for row in rows:
            stafftable.insert("", "end", values=row)
    

    Entry_delete_staff = customtkinter.CTkEntry(master=delete_staffwindow,placeholder_text="staff id",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_delete_staff.place(x=600, y=620)
    
    def on_confirm_delete_staff(event=None):
        # รับค่าจากช่องกรอก
        try:
            staff_id_to_delete = int(Entry_delete_staff.get())
        except ValueError:
            return
        
        delete_staff_(staff_id_to_delete)
        refresh_staff_table_delete()

        Entry_delete_staff.delete(0, 'end')
        
    Entry_delete_staff.bind("<Return>", on_confirm_delete_staff)  # กด Enter ในช่องระยะเวลาเพื่อยืนยันข้อมูล

    Button_confirm_delete_staff = customtkinter.CTkButton(master=delete_staffwindow,
        text="confirm",command=on_confirm_delete_staff,font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=120,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_confirm_delete_staff.place(x=620, y=700)

    Button_back = customtkinter.CTkButton(master=delete_staffwindow,text="back to menu",command=go_back6,  
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_back.place(x=750, y=700)

def go_back6():
    delete_staffwindow.withdraw()
    staffwindow.deiconify()
   
def delete_staff_(staff_id_to_delete):
    cursor.execute('''DELETE FROM staff WHERE staff_id = ?''', (staff_id_to_delete,))
    conn.commit()

#หน้าโชว์ staff
def refresh_ui(windowshow_staff):
    # """รีเฟรชหน้าจอ"""
    for widget in windowshow_staff.winfo_children():
        widget.destroy()
    show_employees(windowshow_staff)

def add_employee(name, role, image_path, windowshow_staff):
    # """เพิ่มพนักงานใหม่"""
    try:
        cursor.execute("INSERT INTO picture (name, role, image_path) VALUES (?, ?, ?)", (name, role, image_path))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error adding employee: {e}")

def delete_employee(emp_id, windowshow_staff):
    # """ลบพนักงานออกจากฐานข้อมูล"""
    try:
        cursor.execute("SELECT image_path FROM picture WHERE id = ?", (emp_id,))
        image_path = cursor.fetchone()
        if image_path and os.path.exists(image_path[0]):
            os.remove(image_path[0])
        cursor.execute("DELETE FROM picture WHERE id = ?", (emp_id,))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error deleting employee: {e}")

def browse_image(entry_image_path):
    # """เลือกไฟล์รูปภาพ"""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;*.jpeg")])
    if file_path:
        new_path = f"images/{os.path.basename(file_path)}"
        os.makedirs("images", exist_ok=True)
        shutil.copy(file_path, new_path)
        entry_image_path.delete(0, "end")
        entry_image_path.insert(0, new_path)

def update_employee(emp_id, name, role, image_path, windowshow_staff):
    # """แก้ไขข้อมูลพนักงาน"""
    try:
        cursor.execute("UPDATE picture SET name = ?, role = ?, image_path = ? WHERE id = ?", (name, role, image_path, emp_id))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error updating employee: {e}")

def edit_employee(emp_id, current_name, current_role, current_image_path, windowshow_staff):
    # """เปิดหน้าต่างใหม่เพื่อแก้ไขข้อมูลพนักงาน"""
    edit_window = Toplevel(windowshow_staff)
    edit_window.title("แก้ไขข้อมูลพนักงาน")

    entry_name = Entry(edit_window)
    entry_name.grid(row=0, column=1, padx=20, pady=20)
    entry_name.insert(0, current_name)

    entry_role = Entry(edit_window)
    entry_role.grid(row=1, column=1, padx=20, pady=20)
    entry_role.insert(0, current_role)

    entry_image_path = Entry(edit_window)
    entry_image_path.grid(row=2, column=1, padx=20, pady=20)
    entry_image_path.insert(0, current_image_path)

    Button(edit_window, text="เลือกไฟล์", command=lambda: browse_image(entry_image_path)).grid(row=2, column=2, padx=10, pady=10)
    Button(edit_window, text="บันทึก", command=lambda: update_employee(emp_id, entry_name.get(), entry_role.get(), entry_image_path.get(), windowshow_staff)).grid(row=3, column=1, padx=10, pady=10)

    edit_window.mainloop()

def show_employees(windowshow_staff):
    # """แสดงข้อมูลพนักงาน"""
    frame = Frame(windowshow_staff, bg="#f2d8d7")
    frame.pack(fill="both", expand=True)

    try:
        cursor.execute("SELECT id, name, role, image_path FROM picture ORDER BY id DESC")
        employees = cursor.fetchall()
    except Exception as e:
        print(f"Error fetching employees: {e}")
        return


    entry_name = Entry(frame)
    entry_name = customtkinter.CTkEntry(master=windowshow_staff,
                                   placeholder_text_color="#454545",
                                   font=("Georgia", 14),
                                   text_color="#000000",
                                   height=40,
                                   width=200,
                                   border_width=1,
                                   corner_radius=20,
                                   border_color="#f2d8d7",
                                   bg_color="#f2d8d7",
                                   fg_color="#ffffff")
    entry_name.place(x=20,y=20,)
    entry_name.insert(0, "name")

    entry_role = Entry(frame)
    entry_role = customtkinter.CTkEntry(master=windowshow_staff,
                                   placeholder_text_color="#454545",
                                   font=("Georgia", 14),
                                   text_color="#000000",
                                   height=40,
                                   width=200,
                                   border_width=1,
                                   corner_radius=20,
                                   border_color="#f2d8d7",
                                   bg_color="#f2d8d7",
                                   fg_color="#ffffff")
    entry_role.place(x=300,y=20)
    entry_role.insert(0, "position")

    entry_image_path = Entry(frame)
    entry_image_path = customtkinter.CTkEntry(master=windowshow_staff,
                                   placeholder_text_color="#454545",
                                   font=("Georgia", 14),
                                   text_color="#000000",
                                   height=40,
                                   width=200,
                                   border_width=1,
                                   corner_radius=20,
                                   border_color="#f2d8d7",
                                   bg_color="#f2d8d7",
                                   fg_color="#ffffff")
    entry_image_path.place(x=580,y=20)

    Button(frame, text="เลือกไฟล์", command=lambda: browse_image(entry_image_path)).grid(row=1, column=24, padx=10, pady=20)
    
    Button(frame, text="เพิ่ม", command=lambda: add_employee(entry_name.get(), entry_role.get(), entry_image_path.get(), windowshow_staff)).grid(row=1, column=30, padx=10, pady=20)

    for index, (emp_id, name, role, image_path) in enumerate(employees, start=2):
        emp_frame = Frame(frame, bg="#f2d8d7")
        emp_frame.grid(row=index, column=0, columnspan=10, pady=50, padx=50, sticky="w")

        try:
            img = Image.open(image_path)
            img = img.resize((400, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            Label(emp_frame, image=img, bg="#f2d8d7").grid(row=0, column=8, rowspan=5, padx=10)
            emp_frame.image = img
        except Exception as e:
            Label(emp_frame, text="Image not found", bg="white").grid(row=0, column=8, rowspan=2, padx=5)
            print(f"Error loading image: {e}")

        Label(emp_frame, text=f"ชื่อ: {name}\nตำแหน่ง: {role}", bg="white").grid(row=0, column=16, padx=5, sticky="w")
        Button(emp_frame, text="ลบ", command=lambda emp_id=emp_id: delete_employee(emp_id, windowshow_staff), bg="red", fg="white").grid(row=0, column=22, padx=5)
        Button(emp_frame, text="แก้ไข", command=lambda emp_id=emp_id, name=name, role=role, image_path=image_path: edit_employee(emp_id, name, role, image_path, windowshow_staff), bg="yellow").grid(row=0, column=24, padx=5)

def showstaff():
    # """ฟังก์ชันเรียกหน้าต่างแสดงข้อมูลพนักงาน"""
    windowshow_staff = Toplevel()
    windowshow_staff.title("แสดงข้อมูลพนักงาน")
    windowshow_staff.configure(bg="#f2d8d7")
    windowshow_staff.geometry("1950x1080")
    show_employees(windowshow_staff)

   

# ------------------------- หน้าต่าง membership --------------------------
def member():
    global memberwindow
    memberwindow = Toplevel()

    memberwindow.title("Membership Menu")
    memberwindow.geometry("1950x1080")
    memberwindow.configure(bg="#f2d8d7")

    img4 = Image.open('member.jpg')
    photo4 = ImageTk.PhotoImage(img4)
    label_image = Label(memberwindow, image=photo4)
    label_image.photo = photo4  # เก็บอ้างอิง
    label_image.place(x=-15, y=0)

    Label(memberwindow, text="member", font=("Georgia", 20), bg="#f2d8d7", fg="#000000").place(x=35, y=160)

#ปุ่มเพิ่มmember
    Button_addmember = customtkinter.CTkButton(master=memberwindow,text="add",command=add_member,
        font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_addmember.place(x=25, y=205)
#ปุ่มอัปเดต
    Button_updatemember = customtkinter.CTkButton(master=memberwindow,text="update",command=update_member,
        font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_updatemember.place(x=25, y=265)
#ปุ่มลบเมมเบอร์
    Button_deletemember = customtkinter.CTkButton(master=memberwindow,text="delete",command=delete_member,
        font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_deletemember.place(x=25, y=325)
#ปุ่มย้อนกลับไปหน้าหลัก
    Button_gomenu = customtkinter.CTkButton(master=memberwindow,text="back",command=lambda:go_back7(master),
        font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",height=50,width=80,
        border_width=2,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_gomenu.place(x=25, y=700)

def go_back7(master):
    memberwindow.withdraw()
    master.deiconify()

#หน้าเพิ่มข้อมูลของสมาชิก
def add_member():
    global addmemberwindow
    # ปิดหน้าต่างบริการ
    memberwindow.withdraw()
    
    # สร้างหน้าต่างใหม่สำหรับลงทะเบียนสมาชิกใหม่
    addmemberwindow = Toplevel()
    addmemberwindow.title("Add New Member")
    addmemberwindow.geometry("1950x1080")
    addmemberwindow.configure(bg="#f2d8d7")

    title_label = ttk.Label(addmemberwindow, text="Membership Information", font=("Georgia", 16))
    title_label.place(x=540, y=20)
    columns = ("membership_id","discount_rate", "first_name", "last_name", "phone" , "email", "birthdate" ,"join_date", "expiry_date")
    membertable = ttk.Treeview(addmemberwindow, columns=columns, show='headings',height=32)
    columns_width = {
        "membership_id": 50,
        "discount_rate": 80,
        "first_name": 120,
        "last_name": 120,
        "phone": 80,
        "email": 160,
        "birthdate": 80,
        "join_date":80,
        "expiry_date": 80 }
    for col in columns:
        membertable.heading(col, text=col)
        membertable.column(col, width=columns_width[col])
        membertable.place(x=540, y=50)
    cursor.execute("SELECT * FROM memberships")
    rows = cursor.fetchall()
    for row in rows:
        membertable.insert("", "end", values=row)

    def refresh_member_table_add():
        for row in membertable.get_children():
            membertable.delete(row)
        cursor.execute("SELECT * FROM memberships")
        rows = cursor.fetchall()
        for row in rows:
            membertable.insert("", "end", values=row)
    
    Label(addmemberwindow, text="Welcome New Member", font=("Georgia", 20), bg="#f2d8d7", fg="#000000").place(x=100, y=50)

    # ช่องกรอกข้อมูลสมาชิกต่างๆ
    Entry_firstname = customtkinter.CTkEntry(master=addmemberwindow,placeholder_text="first name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_firstname.place(x=100, y=120)

    Entry_lastname = customtkinter.CTkEntry(master=addmemberwindow,placeholder_text="last name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_lastname.place(x=100, y=190)

    Entry_phone = customtkinter.CTkEntry(master=addmemberwindow,placeholder_text="phone",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_phone.place(x=100, y=260)

    Entry_email = customtkinter.CTkEntry(master=addmemberwindow,placeholder_text="email",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_email.place(x=100, y=330)

    Entry_birthdate = customtkinter.CTkEntry(master=addmemberwindow,placeholder_text="birthdate (YY-MM-DD)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_birthdate.place(x=100, y=400)

    
    Entry_join_date = customtkinter.CTkEntry(master=addmemberwindow,placeholder_text="join date (YY-MM-DD)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_join_date.place(x=100, y=470)

    Entry_expiry_date = customtkinter.CTkEntry(master=addmemberwindow,placeholder_text="expiry date (YY-MM-DD)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_expiry_date.place(x=100, y=540)

    def on_confirm(event=None):
        # รับค่าจากช่องกรอก
        memberdiscountrate = 10.0
        memberfirst_name = Entry_firstname.get()
        memberlast_name = Entry_lastname.get()
        memberphone = Entry_phone.get()
        memberemail = Entry_email.get()
        memberbirthdate =Entry_birthdate.get()
        memberjoindate= Entry_join_date.get()
        memberexpirydate=Entry_expiry_date.get()

        memberadd(memberdiscountrate,memberfirst_name ,memberlast_name , memberphone, memberemail,memberbirthdate,memberjoindate,memberexpirydate)
        refresh_member_table_add()

        # เคลียร์ข้อมูลในช่องกรอกเพื่อให้สามารถกรอกข้อมูลใหม่ได้
        Entry_firstname.delete(0, 'end')
        Entry_lastname.delete(0, 'end')
        Entry_phone.delete(0, 'end')
        Entry_email.delete(0, 'end')
        Entry_birthdate.delete(0, 'end')
        Entry_join_date.delete(0, 'end')
        Entry_expiry_date.delete(0, 'end')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องถัดไป
    Entry_firstname.bind("<Return>", focus_next_widget)
    Entry_lastname.bind("<Return>", focus_next_widget)
    Entry_phone.bind("<Return>", focus_next_widget)
    Entry_email.bind("<Return>", focus_next_widget)
    Entry_birthdate.bind("<Return>", focus_next_widget)
    Entry_join_date.bind("<Return>", focus_next_widget)
    Entry_expiry_date.bind("<Return>", on_confirm)  # กด Enter ในช่อง position เพื่อยืนยันข้อมูล

# ปุ่มยืนยัน
    Button_add_member_ok = customtkinter.CTkButton(master=addmemberwindow,text="confirm",command=on_confirm,
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_add_member_ok.place(x=110, y=620)

    Button_back = customtkinter.CTkButton(master=addmemberwindow,text="back to menu",command=go_back8,  
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_back.place(x=250, y=620)

def go_back8():
    addmemberwindow.withdraw()
    memberwindow.deiconify()

def memberadd(memberdiscountrate,memberfirstname ,memberlastname,memberphone,memberemail,  memberbirthdate, memberjoindate,memberexpirydate):
    cursor.execute('''INSERT INTO memberships (discount_rate, first_name, last_name, phone, email, birthdate, join_date, expiry_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (memberdiscountrate, memberfirstname, memberlastname, memberphone, memberemail, memberbirthdate, memberjoindate, memberexpirydate))
    conn.commit()

def update_member():
    global update_memberwindow
    # ปิดหน้าต่างบริการ
    memberwindow.withdraw()
    
    # สร้างหน้าต่างใหม่สำหรับแก้ไขข้อมูลพนักงาน
    update_memberwindow = Toplevel()
    update_memberwindow.title("Update Existing Member Information")
    update_memberwindow.geometry("1950x1080")
    update_memberwindow.configure(bg="#f2d8d7")

    title_label = ttk.Label(update_memberwindow, text="Membership Information", font=("Georgia", 16))
    title_label.place(x=540, y=20)
    columns = ("membership_id","discount_rate", "first_name", "last_name", "phone" , "email", "birthdate" ,"join_date", "expiry_date")
    membertable = ttk.Treeview(update_memberwindow, columns=columns, show='headings',height=33)
    columns_width = {
        "membership_id": 50,
        "discount_rate": 80,
        "first_name": 120,
        "last_name": 120,
        "phone": 80,
        "email": 160,
        "birthdate": 80,
        "join_date":80,
        "expiry_date": 80 }
    for col in columns:
        membertable.heading(col, text=col)
        membertable.column(col, width=columns_width[col])
        membertable.place(x=540, y=50)

    cursor.execute("SELECT * FROM memberships")
    rows = cursor.fetchall()

    for row in rows:
        membertable.insert("", "end", values=row)

    def refresh_member_table_update():
        for row in membertable.get_children():
            membertable.delete(row)

        cursor.execute("SELECT * FROM memberships")
        rows = cursor.fetchall()

        for row in rows:
            membertable.insert("", "end", values=row)

    # ช่องกรอก member id เพื่อแก้ไขข้อมูลของ member
    Entry_member_id = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="member id",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_member_id.place(x=100, y=50)

    Entry_discout_rate = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="discout rate",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_discout_rate.place(x=100, y=120)

    Entry_firstname = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="first name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_firstname.place(x=100, y=190)

    Entry_lastname = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="last name",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_lastname.place(x=100, y=260)

    Entry_phone = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="phone",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_phone.place(x=100, y=330)

    Entry_email = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="email",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_email.place(x=100, y=400)

    Entry_birthdate = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="birthdate (YY-MM-DD)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_birthdate.place(x=100, y=470)

    Entry_join_date = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="join date (YY-MM-DD)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_join_date.place(x=100, y=540)

    Entry_expiry_date = customtkinter.CTkEntry(master=update_memberwindow,placeholder_text="expiry date (YY-MM-DD)",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_expiry_date.place(x=100, y=610)

    def on_confirm_update_member(event=None):
        # รับค่าจากช่องกรอก
        member_id = Entry_member_id.get()
        memberdiscountrate = Entry_discout_rate.get()
        memberfirst_name = Entry_firstname.get()
        memberlast_name = Entry_lastname.get()
        memberphone = Entry_phone.get()
        memberemail = Entry_email.get()
        memberbirthdate =Entry_birthdate.get()
        memberjoindate= Entry_join_date.get()
        memberexpirydate=Entry_expiry_date.get()

        memberupdate(member_id,memberdiscountrate,memberfirst_name ,memberlast_name , memberphone, memberemail,memberbirthdate,memberjoindate,memberexpirydate)
        refresh_member_table_update()

        # เคลียร์ข้อมูลในช่องกรอกเพื่อให้สามารถกรอกข้อมูลใหม่ได้
        Entry_member_id.delete(0, 'end')
        Entry_discout_rate.delete(0, 'end')
        Entry_firstname.delete(0, 'end')
        Entry_lastname.delete(0, 'end')
        Entry_phone.delete(0, 'end')
        Entry_email.delete(0, 'end')
        Entry_birthdate.delete(0, 'end')
        Entry_join_date.delete(0, 'end')
        Entry_expiry_date.delete(0, 'end')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องถัดไป
    Entry_member_id.bind("<Return>", focus_next_widget)
    Entry_discout_rate.bind("<Return>", focus_next_widget)
    Entry_firstname.bind("<Return>", focus_next_widget)
    Entry_lastname.bind("<Return>", focus_next_widget)
    Entry_phone.bind("<Return>", focus_next_widget)
    Entry_email.bind("<Return>", focus_next_widget)
    Entry_birthdate.bind("<Return>", focus_next_widget)
    Entry_join_date.bind("<Return>", focus_next_widget)
    Entry_expiry_date.bind("<Return>", on_confirm_update_member) 

# ปุ่มยืนยัน
    Button_update_member_ok = customtkinter.CTkButton(master=update_memberwindow,text="confirm",
        command=on_confirm_update_member, font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=120,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_update_member_ok.place(x=110, y=690)

    Button_back = customtkinter.CTkButton(master=update_memberwindow,text="back to menu",command=go_back9,  
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_back.place(x=250, y=690)

def go_back9():
    update_memberwindow.withdraw()
    memberwindow.deiconify()

def memberupdate(member_id,memberdiscountrate,memberfirst_name ,memberlast_name , memberphone, memberemail,memberbirthdate,memberjoindate,memberexpirydate):
    if memberdiscountrate:
        cursor.execute('''
        UPDATE memberships
        SET discount_rate = ?
        WHERE membership_id = ?
        ''', (memberdiscountrate, member_id))
    if memberfirst_name:
        cursor.execute('''
        UPDATE memberships
        SET first_name = ?
        WHERE membership_id = ?
        ''', (memberfirst_name, member_id))
    if memberlast_name:
        cursor.execute('''
        UPDATE memberships
        SET last_name = ?
        WHERE membership_id = ?
        ''', (memberlast_name, member_id))
    if memberphone:
        cursor.execute('''
        UPDATE memberships
        SET phone = ?
        WHERE membership_id = ?
        ''', (memberphone, member_id))
    if memberemail:
        cursor.execute('''
        UPDATE memberships
        SET email = ?
        WHERE membership_id = ?
        ''', (memberemail, member_id))
    if memberbirthdate:
        cursor.execute('''
        UPDATE memberships
        SET birthdate = ?
        WHERE membership_id = ?
        ''', (memberbirthdate, member_id))
    if memberjoindate:
        cursor.execute('''
        UPDATE memberships
        SET join_date = ?
        WHERE membership_id = ?
        ''', (memberjoindate, member_id))
    if memberexpirydate:
        cursor.execute('''
        UPDATE memberships
        SET expiry_date = ?
        WHERE membership_id = ?
        ''', (memberexpirydate, member_id))

    conn.commit()

def delete_member():
    global delete_memberwindow
    
    memberwindow.withdraw()
    
    delete_memberwindow = Toplevel()
    delete_memberwindow.title("Delete Existing Member")
    delete_memberwindow.geometry("1950x1080")
    delete_memberwindow.configure(bg="#f2d8d7")

    title_label = ttk.Label(delete_memberwindow, text="Enter Member ID to Delete Membership Information", font=("Georgia", 16))
    title_label.place(x=540, y=45)
    columns = ("membership_id","discount_rate", "first_name", "last_name", "phone" , "email", "birthdate","join_date", "expiry_date")
    membertable = ttk.Treeview(delete_memberwindow, columns=columns, show='headings',height=24)
    columns_width = {
        "membership_id": 50,
        "discount_rate": 80,
        "first_name": 120,
        "last_name": 120,
        "phone": 80,
        "email": 160,
        "birthdate": 80,
        "join_date":80,
        "expiry_date": 80 }
    for col in columns:
        membertable.heading(col, text=col)
        membertable.column(col, width=columns_width[col])
        membertable.place(x=350, y=90)

    cursor.execute("SELECT * FROM memberships")
    rows = cursor.fetchall()

    for row in rows:
        membertable.insert("", "end", values=row)

    def refresh_member_table_delete():
        for row in membertable.get_children():
            membertable.delete(row)

        cursor.execute("SELECT * FROM memberships")
        rows = cursor.fetchall()

        for row in rows:
            membertable.insert("", "end", values=row)

    Entry_delete_member = customtkinter.CTkEntry(master=delete_memberwindow,placeholder_text="member id",
        placeholder_text_color="#454545",font=("Georgia", 14),text_color="#000000",
        height=50,width=300,border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_delete_member.place(x=650, y=620)
    
    def on_confirm_delete_member(event=None):
        try:
            memberid_to_delete = int(Entry_delete_member.get())
        except ValueError:
            return
        
        delete_member_(memberid_to_delete)
        refresh_member_table_delete()

        Entry_delete_member.delete(0, 'end')
        
    Entry_delete_member.bind("<Return>", on_confirm_delete_member)  # กด Enter ในช่องระยะเวลาเพื่อยืนยันข้อมูล

    Button_confirm_delete_member = customtkinter.CTkButton(master=delete_memberwindow,text="confirm",
        command=on_confirm_delete_member, font=("Georgia", 14),
        text_color="#000000",hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,
        border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_confirm_delete_member.place(x=670, y=700)

    Button_deletemember_back = customtkinter.CTkButton(master=delete_memberwindow,
        text="back to menu",command=go_back15,  # เรียกใช้ฟังก์ชันเมื่อคลิกปุ่ม
        font=("Georgia", 14),text_color="#000000",hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_deletemember_back.place(x=810, y=700)

def go_back15():
    delete_memberwindow.withdraw()
    memberwindow.deiconify()
   
def delete_member_(memberid_to_delete):
    cursor.execute('''DELETE FROM memberships WHERE membership_id = ? ''', (memberid_to_delete,))
    conn.commit()

#----------------------- หน้าต่าง booking -----------------------------
def booking():
    global bookingwindow
    bookingwindow = Toplevel()
    bookingwindow.title("Booking Menu")
    bookingwindow.geometry("1950x1080")
    bookingwindow.configure(bg="#f2d8d7")

    img5 = Image.open('booking.jpg')
    photo5 = ImageTk.PhotoImage(img5)
    label_image = Label(bookingwindow, image=photo5)
    label_image.photo = photo5  # เก็บอ้างอิง
    label_image.place(x=-15, y=0)

    Label(bookingwindow, text="booking", font=("Georgia", 20), bg="#f2d8d7", fg="#000000").place(x=35, y=160)

    Button_addbooking = customtkinter.CTkButton(master=bookingwindow,
        command=add_booking,text="add",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_addbooking.place(x=25, y=205)

    Button_updatebooking = customtkinter.CTkButton(master=bookingwindow,
        command=update_booking,text="update",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_updatebooking.place(x=25, y=265)

    Button_deletebooking = customtkinter.CTkButton(master=bookingwindow,
        command=delete_booking,text="delete",font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=120,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_deletebooking.place(x=25, y=325)

    Button_booking_gomenu = customtkinter.CTkButton(master=bookingwindow,
        text="back",command=lambda:go_back11(master),font=("Georgia", 25),text_color="#000000",
        hover=True,hover_color="#949494",height=50,width=80,
        border_width=2,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_booking_gomenu.place(x=25, y=700)

def go_back11(master):
    bookingwindow.withdraw()
    master.deiconify()

def add_booking():
    global add_bookingwindow
    
    bookingwindow.withdraw()
    
    add_bookingwindow = Toplevel()
    add_bookingwindow.title("Add New booking")
    add_bookingwindow.geometry("1950x1080")
    add_bookingwindow.configure(bg="#f2d8d7")

    # ตารางแสดงข้อมูลรายการ service
    title_label = ttk.Label(add_bookingwindow, text="Service Information", font=("Georgia", 16))
    title_label.place(x=100, y=20)
    columns = ("ID", "Service Name", "Price", "Duration")
    servicetable = ttk.Treeview(add_bookingwindow, columns=columns, show='headings', height=12)
    column_widths = {
        "ID": 50,
        "Service Name": 180,
        "Price": 100,
        "Duration": 80}
    for col in columns:
        servicetable.heading(col, text=col)
        servicetable.column(col, width=column_widths[col])
    servicetable.place(x=100, y=50)
    # ดึงข้อมูลจาก sql ตาราง ourservices
    cursor.execute("SELECT * FROM ourservices")
    rows = cursor.fetchall()
    # เพิ่มข้อมูลลงใน servicetable
    for row in rows:
        servicetable.insert("", "end", values=row)

    # ตารางแสดงข้อมูลรายชื่อ staff
    title_label = ttk.Label(add_bookingwindow, text="Staff Information", font=("Georgia", 16))
    title_label.place(x=600, y=20)
    columns = ("staff_id", "first_name", "last_name", "id_card", "email", "birthdate", "phone", "position")
    stafftable = ttk.Treeview(add_bookingwindow, columns=columns, show='headings', height=34)
    column_widths = {
        "staff_id": 60,
        "first_name": 100,
        "last_name": 100,
        "id_card": 120,
        "email": 160,
        "birthdate": 100,
        "phone": 120,
        "position": 100}
    for col in columns:
        stafftable.heading(col, text=col)
        stafftable.column(col, width=column_widths[col])
    stafftable.place(x=600, y=50)
    cursor.execute("SELECT * FROM staff")
    rows = cursor.fetchall()
    for row in rows:
        stafftable.insert("", "end", values=row)

    # ช่องกรอกข้อมูลการจองต่างๆ
    Entry_service_id = customtkinter.CTkEntry(master=add_bookingwindow,
        placeholder_text="service id",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_service_id.place(x=150, y=350)

    Entry_bookingdate = customtkinter.CTkEntry(master=add_bookingwindow,
        placeholder_text="booking date (YY-MM-DD)",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_bookingdate.place(x=150, y=420)

    Entry_starttime = customtkinter.CTkEntry(master=add_bookingwindow,
        placeholder_text="start time (hh:mm AM/PM)",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_starttime.place(x=150, y=490)

    Entry_staffname = customtkinter.CTkEntry(master=add_bookingwindow,
        placeholder_text="staff name",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_staffname.place(x=150, y=560)

    Entry_customerphone = customtkinter.CTkEntry(master=add_bookingwindow,
        placeholder_text="phone",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_customerphone.place(x=150, y=630)
    

    def on_confirm_add_booking(event=None):
        service_id= Entry_service_id.get()
        bkdate = Entry_bookingdate.get()
        starttime = Entry_starttime.get()
        staffname = Entry_staffname.get()
        customerphone = Entry_customerphone.get()

        add_booking_(service_id,bkdate,starttime,staffname,customerphone,)

        # เคลียร์ข้อมูลในช่องกรอกเพื่อให้สามารถกรอกข้อมูลใหม่ได้
        Entry_service_id.delete(0, 'end')
        Entry_bookingdate.delete(0, 'end')
        Entry_starttime.delete(0, 'end')
        Entry_staffname.delete(0, 'end')
        Entry_customerphone.delete(0, 'end')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องถัดไป
    Entry_service_id.bind("<Return>", focus_next_widget)
    Entry_bookingdate.bind("<Return>", focus_next_widget)
    Entry_starttime.bind("<Return>", focus_next_widget)
    Entry_staffname.bind("<Return>", focus_next_widget)
    Entry_customerphone.bind("<Return>", on_confirm_add_booking)

    Button_add_booking_ok = customtkinter.CTkButton(master=add_bookingwindow,
        text="confirm",command=on_confirm_add_booking,  # เรียกใช้ฟังก์ชันเมื่อคลิกปุ่ม
        font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Button_add_booking_ok.place(x=170, y=710)

    Button_addbooking_gomenu = customtkinter.CTkButton(master=add_bookingwindow,
        text="back to menu",command=go_back12,
        font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",
        height=40,width=120,corner_radius=20,
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Button_addbooking_gomenu.place(x=300, y=710)

def go_back12():
    add_bookingwindow.withdraw()
    bookingwindow.deiconify()

def calculate_end_time(starttime, duration):
    start_dt = datetime.strptime(starttime, "%I:%M %p")
    end_dt = start_dt + timedelta(minutes=duration)
    return end_dt.strftime("%I:%M %p")
 
def add_booking_(service_id, bkdate, starttime, staffname, customerphone):
    # ค้นหา membership_id และ discount_rate จากเบอร์โทรศัพท์
    cursor.execute('''SELECT membership_id, discount_rate FROM memberships WHERE phone = ? ''', (customerphone,))
    membership = cursor.fetchone()

    if membership:
        membership_id, discount_rate = membership
    else:
        membership_id, discount_rate = None, 0.0

    cursor.execute('''SELECT price, duration, name FROM ourservices WHERE service_id = ? ''', (service_id,))
    service = cursor.fetchone()

    if service:
        price, duration, service_name = service
        discounted = price * (discount_rate / 100)
        discounted_price = price * (1 - discount_rate / 100)
    else:
        return

    cursor.execute('''SELECT staff_id FROM staff WHERE first_name = ? ''', (staffname,))
    staff = cursor.fetchone()

    if staff:
        staff_id = staff[0]
    else:
        return

    endtime = calculate_end_time(starttime, duration)

    cursor.execute('''INSERT INTO bookings (membership_id, service_id, service_name, staff_id, staff_name, booking_date, start_time, end_time, customer_phone, price, discounted, total_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (membership_id, service_id, service_name, staff_id, staffname, bkdate, starttime, endtime, customerphone, price, discounted, discounted_price))
    conn.commit()

def update_booking ():
    global update_bookingwindow
    
    bookingwindow.withdraw()
    
    update_bookingwindow = Toplevel()
    update_bookingwindow.title("Edit Existing Booking")
    update_bookingwindow.geometry("1950x1080")
    update_bookingwindow.configure(bg="#f2d8d7")

    # ตารางแสดงข้อมูลรายการ booking ที่มีอยู่
    title_label = ttk.Label(update_bookingwindow, text="Booking History", font=("Georgia", 16))
    title_label.place(x=450, y=20)
    # กำหนดคอลัมน์สำหรับตาราง
    columns = ("booking_id", "membership_id", "service_id", "service_name", "staff_id", "staff_name", "booking_date", "start_time", "end_time", "customer_phone", "price", "discounted", "total_price")
    bookingtable = ttk.Treeview(update_bookingwindow, columns=columns, show='headings', height=18)
    # กำหนดขนาดคอลัมน์
    column_widths = {
        "booking_id": 75,
        "membership_id": 90,
        "service_id": 70,
        "service_name": 120,
        "staff_id": 65,
        "staff_name": 70,
        "booking_date": 80,
        "start_time": 70,
        "end_time": 70,
        "customer_phone": 100,
        "price": 60,
        "discounted": 70,
        "total_price": 75
    }

    for col in columns:
        bookingtable.heading(col, text=col)
        bookingtable.column(col, width=column_widths[col])

    bookingtable.place(x=450, y=50)

    # ดึงข้อมูลจาก sql ตาราง bookings
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    for row in rows:
        bookingtable.insert("", "end", values=row)

    def refresh_booking_table_update(): 
        for row in bookingtable.get_children(): bookingtable.delete(row) 
        cursor.execute("SELECT * FROM bookings") 
        rows = cursor.fetchall() 
        for row in rows: bookingtable.insert("", "end", values=row)

    # ตารางแสดงข้อมูลรายการ service
    columns = ("ID", "Service Name", "Price", "Duration")
    servicetable = ttk.Treeview(update_bookingwindow, columns=columns, show='headings', height=8)
    column_widths = {
        "ID": 30,
        "Service Name": 180,
        "Price": 50,
        "Duration": 55}
    for col in columns:
        servicetable.heading(col, text=col)
        servicetable.column(col, width=column_widths[col])
    servicetable.place(x=50, y=550)
    # ดึงข้อมูลจาก sql ตาราง ourservices
    cursor.execute("SELECT * FROM ourservices")
    rows = cursor.fetchall()
    # เพิ่มข้อมูลลงใน servicetable
    for row in rows:
        servicetable.insert("", "end", values=row)


    # ตารางแสดงข้อมูลรายชื่อ staff
    columns = ("staff_id", "first_name", "last_name", "id_card", "email", "birthdate", "phone", "position")
    stafftable = ttk.Treeview(update_bookingwindow, columns=columns, show='headings', height=13)
    column_widths = {
        "staff_id": 90,
        "first_name": 130,
        "last_name": 130,
        "id_card": 130,
        "email": 165,
        "birthdate": 120,
        "phone": 120,
        "position": 130 }
    for col in columns:
        stafftable.heading(col, text=col)
        stafftable.column(col, width=column_widths[col])
    stafftable.place(x=450, y=450)
    cursor.execute("SELECT * FROM staff")
    rows = cursor.fetchall()
    for row in rows:
        stafftable.insert("", "end", values=row)


    # ช่องกรอกข้อมูลการจองต่างๆเพื่อแก้ไข
    Entry_booking_id = customtkinter.CTkEntry(master=update_bookingwindow,
        placeholder_text="booking id",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_booking_id.place(x=60, y=50)

    Entry_service_id = customtkinter.CTkEntry(master=update_bookingwindow,
        placeholder_text="service id",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_service_id.place(x=60, y=120)

    Entry_bookingdate = customtkinter.CTkEntry(master=update_bookingwindow,
        placeholder_text="booking date (YY-MM-DD)",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_bookingdate.place(x=60, y=190)

    Entry_starttime = customtkinter.CTkEntry(master=update_bookingwindow,
        placeholder_text="start time (hh:mm AM/PM)",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_starttime.place(x=60, y=260)

    Entry_staffname = customtkinter.CTkEntry(master=update_bookingwindow,
        placeholder_text="staff name",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_staffname.place(x=60, y=330)

    Entry_customerphone = customtkinter.CTkEntry(master=update_bookingwindow,
        placeholder_text="phone",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",
        height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Entry_customerphone.place(x=60, y=400)

    def on_confirm_update_booking(event=None):
        booking_id_update = Entry_booking_id.get()
        service_id_update = Entry_service_id.get()
        booking_date_update = Entry_bookingdate.get()
        start_time_update = Entry_starttime.get()
        staff_name_update = Entry_staffname.get()
        customer_phone_update = Entry_customerphone.get()

        # ตรวจสอบว่ามี booking_id เพื่ออัปเดตข้อมูล
        if not booking_id_update:
            print("Please enter a valid Booking ID.")
            return

        # ตรวจสอบข้อมูลของสมาชิกเพื่อใช้ส่วนลด
        membership_id, discount_rate = None, 0.0
        if customer_phone_update:
            cursor.execute('''SELECT membership_id, discount_rate FROM memberships WHERE phone = ? ''', (customer_phone_update,))
            membership = cursor.fetchone()
            if membership:
                membership_id, discount_rate = membership

        # ตรวจสอบข้อมูลบริการเพื่อตั้งราคาและระยะเวลา
        service = None
        price, discounted, discounted_price, duration = None, None, None, None
        if service_id_update:
            cursor.execute('''SELECT price, duration FROM ourservices WHERE service_id = ? ''', (service_id_update,))
            service = cursor.fetchone()
            if service:
                price, duration = service
                discounted = price * (discount_rate / 100)
                discounted_price = price * (1 - discount_rate / 100)

        # ตรวจสอบข้อมูลพนักงานเพื่อดึง staff_id และ staff_name
        staff_id = None
        if staff_name_update:
            cursor.execute('''SELECT staff_id FROM staff WHERE first_name = ? ''', (staff_name_update,))
            staff = cursor.fetchone()
            if staff:
                staff_id = staff[0]

        # คำนวณ end_time หากมี start_time และ duration
        end_time_update = None
        if start_time_update and duration:
            end_time_update = calculate_end_time(start_time_update, duration)

        # เรียกใช้ฟังก์ชัน update_booking_ เพื่ออัปเดตเฉพาะฟิลด์ที่มีข้อมูล
        update_booking_(booking_id_update, service_id_update, membership_id, booking_date_update, start_time_update, end_time_update, staff_id, customer_phone_update, discount_rate)
        
        # เรียกใช้ฟังก์ชัน refresh_booking เพื่ออัปเดตตาราง booking
        refresh_booking_table_update()

        # เคลียร์ข้อมูลในช่องกรอกเพื่อให้สามารถกรอกข้อมูลใหม่ได้
        Entry_booking_id.delete(0, 'end')
        Entry_service_id.delete(0, 'end')
        Entry_bookingdate.delete(0, 'end')
        Entry_starttime.delete(0, 'end')
        Entry_staffname.delete(0, 'end')
        Entry_customerphone.delete(0, 'end')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"  # หยุดการทำงานเพิ่มเติมหลังจากเปลี่ยนโฟกัส

    # ผูกปุ่ม Enter กับช่องกรอกแต่ละช่องเพื่อเปลี่ยนโฟกัสไปยังช่องถัดไป
    Entry_booking_id.bind("<Return>", focus_next_widget)
    Entry_service_id.bind("<Return>", focus_next_widget)
    Entry_bookingdate.bind("<Return>", focus_next_widget)
    Entry_starttime.bind("<Return>", focus_next_widget)
    Entry_staffname.bind("<Return>", focus_next_widget)
    Entry_customerphone.bind("<Return>", on_confirm_update_booking)

    Button_update_booking_ok = customtkinter.CTkButton(master=update_bookingwindow,
        text="confirm",command=on_confirm_update_booking, 
        font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",
        height=40,width=120,
        corner_radius=20,
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Button_update_booking_ok.place(x=80, y=480)

    Button_update_booking_gomenu = customtkinter.CTkButton(master=update_bookingwindow,
        text="back to menu", command=go_back13,
        font=("Georgia", 14), text_color="#000000",
        hover=True,hover_color="#949494",
        height=40,width=120,
        corner_radius=20,
        bg_color="#f2d8d7",
        fg_color="#ffffff",)
    Button_update_booking_gomenu.place(x=220, y=480)
   
def go_back13():
    update_bookingwindow.withdraw()
    bookingwindow.deiconify()

def calculate_end_time(starttime, duration):
    start_dt = datetime.strptime(starttime, "%I:%M %p")
    end_dt = start_dt + timedelta(minutes=duration)
    return end_dt.strftime("%I:%M %p")


def update_booking_(booking_id_update, service_id_update, membership_id, booking_date_update, start_time_update, end_time_update, staff_id, customer_phone_update, discount_rate):
    # Update membership_id if provided
    if membership_id:
        cursor.execute('''UPDATE bookings SET membership_id = ? WHERE booking_id = ?''', (membership_id, booking_id_update))

    # Update service_id and times if provided
    if service_id_update:
        cursor.execute('''UPDATE bookings SET service_id = ? WHERE booking_id = ?''', (service_id_update, booking_id_update))
        
        # Recalculate price and discounted price
        cursor.execute('''SELECT price, duration FROM ourservices WHERE service_id = ?''', (service_id_update,))
        service = cursor.fetchone()
        if service:
            price, duration = service
            discounted = price * (discount_rate / 100)
            discounted_price = price * (1 - discount_rate / 100)
            cursor.execute('''UPDATE bookings SET price = ?, discounted = ?, total_price = ? WHERE booking_id = ?''', (price, discounted, discounted_price, booking_id_update))
            
            # Update start_time and end_time if provided
            if start_time_update:
                end_time_update = calculate_end_time(start_time_update, duration)
                cursor.execute('''UPDATE bookings SET start_time = ?, end_time = ? WHERE booking_id = ?''', (start_time_update, end_time_update, booking_id_update))

    # Update staff_id if provided
    if staff_id:
        cursor.execute('''UPDATE bookings SET staff_id = ? WHERE booking_id = ?''', (staff_id, booking_id_update))

    # Update booking_date if provided
    if booking_date_update:
        cursor.execute('''UPDATE bookings SET booking_date = ? WHERE booking_id = ?''', (booking_date_update, booking_id_update))

    # Update customer_phone if provided
    if customer_phone_update:
        cursor.execute('''UPDATE bookings SET customer_phone = ? WHERE booking_id = ?''', (customer_phone_update, booking_id_update))

    conn.commit()



def delete_booking():

    global delete_bookingwindow
    
    bookingwindow.withdraw()
    
    delete_bookingwindow = Toplevel()
    delete_bookingwindow.title("Delete Existing Booking")
    delete_bookingwindow.geometry("1950x1080")
    delete_bookingwindow.configure(bg="#f2d8d7")

    # ตารางแสดงข้อมูลรายการ booking ที่มีอยู่
    title_label = ttk.Label(delete_bookingwindow, text="Enter Booking ID to Delete Booking History", font=("Georgia", 16))
    title_label.place(x=550, y=45)
    columns = ("booking_id", "membership_id", "service_id", "service_name", "staff_id", "staff_name", "booking_date", "start_time", "end_time", "customer_phone", "price", "discounted", "total_price")
    bookingtable = ttk.Treeview(delete_bookingwindow, columns=columns, show='headings', height=22)
    # กำหนดขนาดคอลัมน์
    column_widths = {
        "booking_id": 80,
        "membership_id": 90,
        "service_id": 120,
        "service_name": 200,
        "staff_id": 80,
        "staff_name": 120,
        "booking_date": 100,
        "start_time": 100,
        "end_time": 100,
        "customer_phone": 120,
        "price": 100,
        "discounted": 100,
        "total_price": 120 }
    for col in columns:
        bookingtable.heading(col, text=col)
        bookingtable.column(col, width=column_widths[col])
        bookingtable.place(x=50, y=100)
    # ดึงข้อมูลจาก sql ตาราง bookings
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    for row in rows:
        bookingtable.insert("", "end",  values=row)

    def refresh_booking_table_delete(): 
        for row in bookingtable.get_children(): bookingtable.delete(row) 
        cursor.execute("SELECT * FROM bookings") 
        rows = cursor.fetchall() 
        for row in rows: bookingtable.insert("", "end", values=row)
    
    Entry_delete_booking = customtkinter.CTkEntry(
        master=delete_bookingwindow,
        placeholder_text="booking id",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=300,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",
    )
    Entry_delete_booking.place(x=620, y=590)
    
    def on_confirm_delete_booking(event=None):
        try:
            bookingid_to_delete = int(Entry_delete_booking.get())
        except ValueError:
            return
        
        delete_booking_(bookingid_to_delete)
        refresh_booking_table_delete()

        Entry_delete_booking.delete(0, 'end')
        
    Entry_delete_booking.bind("<Return>", on_confirm_delete_booking)  # กด Enter ในช่องระยะเวลาเพื่อยืนยันข้อมูล

    Button_confirm_delete_booking = customtkinter.CTkButton(
        master=delete_bookingwindow,
        text="confirm",
        command=on_confirm_delete_booking,  # เรียกใช้ฟังก์ชันเมื่อคลิกปุ่ม
        font=("Georgia", 14),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=40,
        width=120,
        corner_radius=20,
        bg_color="#f2d8d7",
        fg_color="#ffffff",
    )
    Button_confirm_delete_booking.place(x=640, y=660)

    Button_deletebooking_back = customtkinter.CTkButton(
        master=delete_bookingwindow,
        text="back to menu",
        command=go_back14,  # เรียกใช้ฟังก์ชันเมื่อคลิกปุ่ม
        font=("Georgia", 14),
        text_color="#000000",
        hover=True,
        hover_color="#949494",
        height=40,
        width=120,
        corner_radius=20,
        bg_color="#f2d8d7",
        fg_color="#ffffff",
    )
    Button_deletebooking_back.place(x=770, y=660)

def go_back14():
    delete_bookingwindow.withdraw()
    bookingwindow.deiconify()
   
def delete_booking_(bookingid_to_delete):
    cursor.execute('''DELETE FROM bookings WHERE booking_id = ? ''', (bookingid_to_delete,))
    conn.commit()

#--------------------- หน้า report ----------------------

def show_report():
    global show_reportwindow
    admin_main_menu.withdraw()
    show_reportwindow= Toplevel()
    show_reportwindow.title("Report")
    show_reportwindow.geometry("1950x1080")
    show_reportwindow.configure(bg="#f2d8d7")


    # ตารางแสดงข้อมูลรายการ booking ที่มีอยู่
    title_label = ttk.Label(show_reportwindow, text="Booking History", font=("Georgia", 16))
    title_label.place(x=450, y=20)
    columns = ("booking_id", "membership_id", "service_id", "service_name", "staff_id", "staff_name", "booking_date", "start_time", "end_time", "customer_phone", "price", "discounted", "total_price")
    bookingtable = ttk.Treeview(show_reportwindow, columns=columns, show='headings', height=30)
    column_widths = {
        "booking_id": 75,
        "membership_id": 90,
        "service_id": 70,
        "service_name": 120,
        "staff_id": 65,
        "staff_name": 70,
        "booking_date": 80,
        "start_time": 70,
        "end_time": 70,
        "customer_phone": 100,
        "price": 60,
        "discounted": 70,
        "total_price": 75
    }
    for col in columns:
        bookingtable.heading(col, text=col)
        bookingtable.column(col, width=column_widths[col])
    bookingtable.place(x=450, y=50)

    def fetch_data():
        service_name = service_name_combobox.get()
        staff_name = staff_name_combobox.get()
        date = date_combobox.get()
        month = month_combobox.get()
        year = year_combobox.get()
        member_id = member_id_combobox.get()

        # Fetch the data (no changes needed)
        query_conditions = []
        query_params = []

        if service_name != 'None':
            query_conditions.append("service_name=?")
            query_params.append(service_name)
        if staff_name != 'None':
            query_conditions.append("staff_name=?")
            query_params.append(staff_name)
        if date != 'None':
            query_conditions.append("booking_date=?")
            query_params.append(date)
        if month != 'None':
            query_conditions.append("strftime('%m', booking_date)=?")
            query_params.append(month)
        if year != 'None':
            query_conditions.append("strftime('%Y', booking_date)=?")
            query_params.append(year)
        if member_id != 'None':
            query_conditions.append("membership_id=?")
            query_params.append(member_id)

        query = "SELECT * FROM bookings"
        if query_conditions:
            query += " WHERE " + " AND ".join(query_conditions)

        cursor.execute(query, tuple(query_params))
        rows = cursor.fetchall()

        # Update table
        for row in bookingtable.get_children():
            bookingtable.delete(row)

        total_sales = 0
        for row in rows:
            bookingtable.insert("", "end", values=row)
            total_sales += row[-1]  # Assuming total_price is the last column

        total_sales_value.config(text="{:,.2f}".format(total_sales))

        # Return parameters ไปใช้ใน create_pdf()
        return service_name, staff_name, date, month, year, member_id


    # ดึงข้อมูลจากตาราง bookings สำหรับเมนู drop-down
    cursor.execute("SELECT DISTINCT service_name FROM bookings")
    service_names = ['None'] + [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT staff_name FROM bookings")
    staff_names = ['None'] + [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT booking_date FROM bookings")
    dates = ['None'] + [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT strftime('%m', booking_date) FROM bookings")
    months = ['None'] + [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT strftime('%Y', booking_date) FROM bookings")
    years = ['None'] + [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT DISTINCT membership_id FROM bookings")
    member_ids = ['None'] + [row[0] for row in cursor.fetchall()]

    # สร้างเมนู drop-down สำหรับเลือก service name
    Label(show_reportwindow, text="Service Name", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").place(x=90, y=150)
    service_name_combobox = ttk.Combobox(show_reportwindow, values=service_names, font=("Georgia", 14))
    service_name_combobox.place(x=90, y=180)

    # สร้างเมนู drop-down สำหรับเลือก staff name
    Label(show_reportwindow, text="Staff Name", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").place(x=90, y=220)
    staff_name_combobox = ttk.Combobox(show_reportwindow, values=staff_names, font=("Georgia", 14))
    staff_name_combobox.place(x=90, y=250)

    # สร้างเมนู drop-down สำหรับเลือก date
    Label(show_reportwindow, text="Date", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").place(x=90, y=290)
    date_combobox = ttk.Combobox(show_reportwindow, values=dates, font=("Georgia", 14))
    date_combobox.place(x=90, y=320)

    # สร้างเมนู drop-down สำหรับเลือก month
    Label(show_reportwindow, text="Month", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").place(x=90, y=360)
    month_combobox = ttk.Combobox(show_reportwindow, values=months, font=("Georgia", 14))
    month_combobox.place(x=90, y=390)

    # สร้างเมนู drop-down สำหรับเลือก year
    Label(show_reportwindow, text="Year", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").place(x=90, y=430)
    year_combobox = ttk.Combobox(show_reportwindow, values=years, font=("Georgia", 14))
    year_combobox.place(x=90, y=460)

    # สร้างเมนู drop-down สำหรับเลือก member id
    Label(show_reportwindow, text="Member ID", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").place(x=90, y=500)
    member_id_combobox = ttk.Combobox(show_reportwindow, values=member_ids, font=("Georgia", 14))
    member_id_combobox.place(x=90, y=530)

    # สร้างปุ่มสำหรับดึงข้อมูล
    button_fetch = customtkinter.CTkButton(master=show_reportwindow, text="confirm", command=fetch_data,font=("Georgia", 20),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=150,bg_color="#f2d8d7",fg_color="#ffffff")
    button_fetch.place(x=140, y=600)

    # ปุ่ม Print
    button_print = customtkinter.CTkButton(master=show_reportwindow, text="print", 
        command=lambda: create_pdf(bookingtable, *fetch_data()), 
        font=("Georgia", 16), text_color="#000000",
        hover=True, hover_color="#949494", height=30, width=120, fg_color="#ffffff")
    button_print.place(x=1345, y=700)

    # ปุ่มย้อนกลับไปหน้าเมนู
    Button_gomenu = customtkinter.CTkButton(master=show_reportwindow,command=reportshow_go_menu,
        text="back",font=("Georgia", 25),text_color="#000000",hover=True,hover_color="#949494",height=50,width=80,
        border_width=2,corner_radius=20,border_color="#f2d8d7",bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_gomenu.place(x=25, y=700)

    # กล่องสำหรับแสดงยอดขายรวม
    total_sales_label = Label(show_reportwindow, text="Total Sales:", font=("Georgia", 14), bg="#f2d8d7", fg="#000000")
    total_sales_label.place(x=990, y=700)

    Label(show_reportwindow, text="Baht", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").place(x=1280, y=700)
    Label(show_reportwindow, text="Sales Report", font=("Georgia", 22), bg="#f2d8d7", fg="#000000").place(x=140, y=80)
    
    total_sales_value = Label(show_reportwindow, text="0", font=("Georgia", 14), bg="#ffffff", fg="#000000", width=15, anchor="e")
    total_sales_value.place(x=1100, y=700)


def create_pdf(bookingtable, service_name, staff_name, date, month, year, member_id):
    # ดึงข้อมูลมาจาก bookingtable
    rows = []
    for row in bookingtable.get_children():
        row_data = bookingtable.item(row)["values"]
        rows.append(row_data)

    # ลงทะเบียนฟอนต์ภาษาไทย
    pdfmetrics.registerFont(TTFont('THSarabun', r'C:\Users\HP\Desktop\gg\THSarabunNew.ttf'))

    # ตั้งชื่อไฟล์ pdf
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_filename = f"sales_report_{current_time}.pdf"

    # สร้างไฟล์ pdf แสดงยอดขาย
    pdf = SimpleDocTemplate(
        pdf_filename,
        pagesize=landscape(A4),
        topMargin=20,
        leftMargin=50,
        rightMargin=50,
        bottomMargin=30)

    # Header
    header_text = "รายงานการขายร้าน Spa Day"
    heading_center = Paragraph(
        header_text,
        ParagraphStyle(
            name='CenterHeading',
            fontName='THSarabun',
            fontSize=20,
            alignment=0,
            leading=24,
            spaceAfter=10))

    # Add the query filter explanation
    query_info = f"บริการ: {service_name}      พนักงาน: {staff_name} <br />" \
             f"วันที่: {date}      เดือน: {month}     ปี: {year} <br />" \
             f"หมายเลขสมาชิก: {member_id}"

    query_info_paragraph = Paragraph(
        query_info,
        ParagraphStyle(
            name="QueryInfo",
            fontName="THSarabun",
            fontSize=14,
            alignment=0, 
            leading=24,))

    # Print date and time
    print_datetime = datetime.now().strftime("วันที่พิมพ์: %d/%m/%Y เวลา: %H:%M:%S")
    print_datetime_paragraph = Paragraph(
        print_datetime,
        ParagraphStyle(
            name="RightDate",
            fontName="THSarabun",
            fontSize=14,
            alignment=0,
            leading=18,
            spaceAfter=10))
    
    # สร้างตาราง
    data = [
        ["Booking ID", "Member ID", "Service ID", "Service Name", "Staff ID", "Staff Name", "Booking Date", "Start Time", "End Time", "Customer Phone", "Price", "Discounted", "Total Price"]
    ]
    total_sales = 0

    for row in rows:
        if len(row) == 13:  # Ensure the row has exactly 13 columns
            try:
                total_sales += float(row[-1])
            except ValueError:
                print(f"Invalid data in row: {row[-1]}")
            data.append(row)
        else:
            print(f"Row data does not match column headers: {row}")

    # แต่งขนาดแต่ละคอลัมน์
    col_widths = [40, 40, 40, 100, 30, 50, 70, 60, 60, 80, 60, 50, 70]

    # แต่งตาราง
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([ 
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'THSarabun'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # รวมยอดขาย
    total_sales_text = Paragraph(
        f"<b>รวมยอดขาย: {total_sales:,.2f} บาท</b>",
        ParagraphStyle(
            name="รวมยอดขาย",
            fontName="THSarabun",
            fontSize=14,
            alignment=2,
            spaceBefore=10
        )
    )

    # Add elements to PDF
    elements = [heading_center, query_info_paragraph, print_datetime_paragraph, table, total_sales_text]
    pdf.build(elements)

    # Open PDF file after creation
    os.system(f'start {pdf_filename}')


def reportshow_go_menu():
    show_reportwindow.withdraw()
    admin_main_menu.deiconify()

#--------------------------------------------------------------------
def show_receipt(): 
    global receipt_window
    master.withdraw()
    
    receipt_window = Toplevel()
    receipt_window.title("Print receipt")
    receipt_window.geometry("1950x1080")
    receipt_window.configure(bg="#f2d8d7")

    # ตารางแสดงข้อมูลรายการ booking ที่มีอยู่
    title_label = ttk.Label(receipt_window, text=" Enter Booking ID to Print Receipt ", font=("Georgia", 16))
    title_label.place(x=600, y=45)
    columns = ("booking_id", "membership_id", "service_id", "service_name", "staff_id", "staff_name", "booking_date", "start_time", "end_time", "customer_phone", "price", "discounted", "total_price")
    bookingtable = ttk.Treeview(receipt_window, columns=columns, show='headings', height=22)
    # กำหนดขนาดคอลัมน์
    column_widths = {
        "booking_id": 80,
        "membership_id": 90,
        "service_id": 120,
        "service_name": 200,
        "staff_id": 80,
        "staff_name": 120,
        "booking_date": 100,
        "start_time": 100,
        "end_time": 100,
        "customer_phone": 120,
        "price": 100,
        "discounted": 100,
        "total_price": 120 }
    for col in columns:
        bookingtable.heading(col, text=col)
        bookingtable.column(col, width=column_widths[col])
        bookingtable.place(x=50, y=100)
    # ดึงข้อมูลจาก sql ตาราง bookings
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    for row in rows:
        bookingtable.insert("", "end",  values=row)

     # ช่องกรอก booking_id
    Entry_booking_ID = customtkinter.CTkEntry(master=receipt_window,
        placeholder_text="enter booking id",placeholder_text_color="#454545",
        font=("Georgia", 14),text_color="#000000",height=50,width=300,
        border_width=1,corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Entry_booking_ID.place(x=620, y=600)

    def on_confirm(event=None):
        booking_id = Entry_booking_ID.get() 
        print_receipt(booking_id)
        Entry_booking_ID.delete(0, END)

    Button_ok = customtkinter.CTkButton(master=receipt_window,command=on_confirm,  
        text="confirm",font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,border_color="#f2d8d7",
        bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_ok.place(x=640, y=680)

    Entry_booking_ID.bind("<Return>", on_confirm)


    def go_back():
        receipt_window.withdraw()
        master.deiconify()

    Button_deletebooking_back = customtkinter.CTkButton(master=receipt_window,command=go_back,
        text="back to menu",font=("Georgia", 14),text_color="#000000",
        hover=True,hover_color="#949494",height=40,width=120,
        corner_radius=20,bg_color="#f2d8d7",fg_color="#ffffff",)
    Button_deletebooking_back.place(x=770, y=680)

    
def print_receipt(booking_id):
        # ดึงข้อมูลจาก booking_id
        cursor.execute(
            "SELECT service_name, price ,discounted,total_price FROM bookings WHERE booking_id = ?", 
            (booking_id,))
        customer_data = cursor.fetchone()

        service_name, price ,discounted, total_price = customer_data
        
        # ฟอนต์ภาษาไทย
        pdfmetrics.registerFont(TTFont('THSarabun', r'C:\Users\HP\Desktop\gg\THSarabunNew.ttf'))
        
        # ตั้งชื่อไฟล์
        receipt_filename = f"receipt_{booking_id}.pdf"
        # ตรวจสอบว่าไฟล์มีอยู่แล้วหรือไม่
        if os.path.exists(receipt_filename): os.remove(receipt_filename)  # ลบไฟล์เก่า

        # ตกแต่งใบเสร็จ
        c = canvas.Canvas(receipt_filename, pagesize=A7)

        # กำหนดขนาดและระยะ
        margin_left = 20
        margin_top = 270
        line_spacing = 15

        # หัวใบเสร็จ
        for _ in range(20):  # วาดซ้ำหลายครั้งเพื่อความหนา
            c.setFont('THSarabun', 12)
            c.drawString(margin_left, margin_top, "Spa Day : 099-042-9364")
            c.setFont('THSarabun', 10)
            c.drawString(margin_left, margin_top - line_spacing, f"Receipt for Booking ID: {booking_id}")
            c.drawString(margin_left, margin_top - 2 * line_spacing, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # เส้นแบ่ง
        margin_top -= 3 * line_spacing
        c.setStrokeColorRGB(0, 0, 0)
        c.setLineWidth(0.5)
        c.line(margin_left, margin_top, 190, margin_top)

        # รายละเอียดบริการ
        margin_top -= line_spacing
        c.setFont('THSarabun', 11)
        c.drawString(margin_left, margin_top, f"{service_name}")
        c.drawRightString(190, margin_top, f"{price:,.2f} Baht")

        # เส้นแบ่ง
        margin_top -= 0.7 * line_spacing
        c.setStrokeColorRGB(0, 0, 0)
        c.setLineWidth(0.5)
        c.line(margin_left, margin_top, 190, margin_top)

        # ส่วนลดสมาชิก
        margin_top -= line_spacing
        c.setFont('THSarabun', 12)
        c.drawString(margin_left, margin_top, "Member Discount (10%)")
        c.drawRightString(190, margin_top, f"-{discounted:,.2f} Baht")

        # รวมยอด
        margin_top -= line_spacing
        c.setFont('THSarabun', 12)
        for _ in range(20):  # วาดซ้ำหลายครั้งเพื่อความหนา
            c.drawString(margin_left, margin_top, "Total")
            c.drawRightString(190, margin_top, f"{total_price:,.2f} Baht")

        # แทรกรูปภาพ
        image_path = "C:/Users/HP/Desktop/gg/promptpay1.jpg"
        image_width = 120  # กำหนดขนาดของรูป
        image_height = 120
        c.drawImage(image_path, (margin_left + 25), margin_top - image_height - 10, width=image_width, height=image_height)

        # ข้อความปิดท้าย
        margin_top -= image_height + 16  # ปรับตำแหน่งข้อความให้พอดีกับรูป
        c.setFont('THSarabun', 12)
        # วาดข้อความตรงกลาง
        text_width = c.stringWidth("Thank you for your visit!", 'THSarabun', 14)
        center_position = (220 - text_width) / 2  # คำนวณตำแหน่งตรงกลาง
        c.drawString(center_position, margin_top, "Thank you for your visit!")


        # บันทึก PDF
        c.save()
        os.system(f'start {receipt_filename}')



# ---------------------------show window--------------------------------
def refresh_ui(window_showservice):
    """รีเฟรชหน้าจอ"""
    for widget in window_showservice.winfo_children():
        widget.destroy()
    show_imgser(window_showservice)

def add_imgser(name, price, duration, image_path, window_showservice):
    """เพิ่มพนักงานใหม่"""
    try:
        cursor.execute("INSERT INTO image (name, price, duration, image_path) VALUES (?, ?, ?, ?)", (name, price, duration, image_path))
        conn.commit()
        refresh_ui(window_showservice)
    except Exception as e:
        print(f"Error adding imgservice: {e}")

def delete_imgser(img_id, window_showservice):
    """ลบพนักงานออกจากฐานข้อมูล"""
    try:
        cursor.execute("SELECT image_path FROM image WHERE id = ?", (img_id,))
        image_path = cursor.fetchone()
        if image_path and os.path.exists(image_path[0]):
            os.remove(image_path[0])
        cursor.execute("DELETE FROM image WHERE id = ?", (img_id,))
        conn.commit()
        refresh_ui(window_showservice)
    except Exception as e:
        print(f"Error deleting imgservice: {e}")

def browse_image(entry_image_path):
    """เลือกไฟล์รูปภาพ"""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;*.jpeg")])
    if file_path:
        new_path = f"images/{os.path.basename(file_path)}"
        os.makedirs("images", exist_ok=True)
        shutil.copy(file_path, new_path)
        entry_image_path.delete(0, "end")
        entry_image_path.insert(0, new_path)

def update_imgser(img_id, name, price, duration, image_path, window_showservice):
    """แก้ไขข้อมูลบริการ"""
    try:
        cursor.execute("UPDATE image SET name = ?, price = ?, duration = ?, image_path = ? WHERE id = ?", (name, price, duration, image_path, img_id))
        conn.commit()
        refresh_ui(window_showservice)
    except Exception as e:
        print(f"Error updating imgservice: {e}")

def edit_imgser(img_id, current_name, current_price, current_duration, current_image_path, window_showservice):
    """เปิดหน้าต่างใหม่เพื่อแก้ไขข้อมูลบริการ"""
    edit_window = Toplevel(window_showservice)
    edit_window.title("แก้ไขข้อมูลพนักงาน")

    entry_name = Entry(edit_window)
    entry_name.grid(row=0, column=1, padx=20, pady=20)
    entry_name.insert(0, current_name)

    entry_price = Entry(edit_window)
    entry_price.grid(row=1, column=1, padx=20, pady=20)
    entry_price.insert(0, current_price)

    entry_duration = Entry(edit_window)
    entry_duration.grid(row=2, column=1, padx=20, pady=20)
    entry_duration.insert(0, current_duration)

    entry_image_path = Entry(edit_window)
    entry_image_path.grid(row=3, column=1, padx=20, pady=20)
    entry_image_path.insert(0, current_image_path)

    Button(edit_window, text="เลือกไฟล์", command=lambda: browse_image(entry_image_path)).grid(row=3, column=2, padx=10, pady=10)
    Button(edit_window, text="บันทึก", command=lambda: update_imgser(img_id, entry_name.get(), entry_price.get(), entry_duration.get(), entry_image_path.get(), window_showservice)).grid(row=4, column=1, padx=10, pady=10)

    edit_window.mainloop()

def show_imgser(window_showservice):
    """แสดงข้อมูลบริการ"""
    frame = Frame(window_showservice, bg="#f2d8d7")
    frame.pack(fill="both", expand=True)

    try:
        cursor.execute("SELECT id, name, price, duration, image_path FROM image ORDER BY id DESC")
        imgser = cursor.fetchall()
    except Exception as e:
        print(f"Error fetching imgservice: {e}")
        return

    entry_name = customtkinter.CTkEntry(
        master=window_showservice,
        placeholder_text="name",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_name.place(x=20, y=20)

    entry_price = customtkinter.CTkEntry(
        master=window_showservice,
        placeholder_text="price",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_price.place(x=300, y=20)

    entry_duration = customtkinter.CTkEntry(
        master=window_showservice,
        placeholder_text="duration",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_duration.place(x=580, y=20)

    entry_image_path = customtkinter.CTkEntry(
        master=window_showservice,
        placeholder_text="image path",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_image_path.place(x=860, y=20)

    customtkinter.CTkButton(
        master=frame,
        text="file",
        font=("Georgia", 14),
        text_color="#000000",
        hover_color="#949494",
        height=40,
        width=100,
        border_width=2,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",
        command=lambda: browse_image(entry_image_path)
    ).place(x=1120, y=20)

    customtkinter.CTkButton(
        master=frame,
        text="add",
        font=("Georgia", 14),
        text_color="#000000",
        hover_color="#949494",
        height=40,
        width=100,
        border_width=2,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",
        command=lambda: add_imgser(entry_name.get(), entry_price.get(), entry_duration.get(), entry_image_path.get(), window_showservice)
    ).place(x=1240, y=20)

    for index, (img_id, name, price, duration, image_path) in enumerate(imgser, start=2):
        row = index // 3  # แถว (Row)
        col = index % 3   # คอลัมน์ (Column)

        emp_frame = Frame(frame, bg="#f2d8d7")
        emp_frame.grid(row=row, column=col, padx=85, pady=95, sticky="w")

        try:
            img = Image.open(image_path)
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            Label(emp_frame, image=img, bg="#f2d8d7").grid(row=0, column=0, padx=10)
            emp_frame.image = img
        except Exception as e:
            Label(emp_frame, text="Image not found", bg="white").grid(row=0, column=0, padx=5)
            print(f"Error loading image: {e}")

        Label(emp_frame, text=name, bg="#f2d8d7", font=("Georgia", 14)).grid(row=1, column=0, padx=10, pady=5)
        Label(emp_frame, text=price, bg="#f2d8d7", font=("Georgia", 14)).grid(row=2, column=0, padx=10, pady=5)
        Label(emp_frame, text=duration, bg="#f2d8d7", font=("Georgia", 14)).grid(row=3, column=0, padx=10, pady=5)

def show_service():
    global show_servicewindow
    show_servicewindow = Toplevel()
    show_servicewindow.title("showservice")
    show_servicewindow.geometry("1950x1080")
    show_servicewindow.configure(bg="#f2d8d7")
    show_imgser(show_servicewindow)



#--------------------- หน้า show staff ----------------------

def refresh_ui(windowshow_staff):
    """รีเฟรชหน้าจอ"""
    for widget in windowshow_staff.winfo_children():
        widget.destroy()
    show_employees(windowshow_staff)

def add_employee(name, role, image_path, windowshow_staff):
    """เพิ่มพนักงานใหม่"""
    try:
        cursor.execute("INSERT INTO picture (name, role, image_path) VALUES (?, ?, ?)", (name, role, image_path))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error adding employee: {e}")

def delete_employee(emp_id, windowshow_staff):
    """ลบพนักงานออกจากฐานข้อมูล"""
    try:
        cursor.execute("SELECT image_path FROM picture WHERE id = ?", (emp_id,))
        image_path = cursor.fetchone()
        if image_path and os.path.exists(image_path[0]):
            os.remove(image_path[0])
        cursor.execute("DELETE FROM picture WHERE id = ?", (emp_id,))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error deleting employee: {e}")

def browse_image(entry_image_path):
    """เลือกไฟล์รูปภาพ"""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;*.jpeg")])
    if file_path:
        new_path = f"images/{os.path.basename(file_path)}"
        os.makedirs("images", exist_ok=True)
        shutil.copy(file_path, new_path)
        entry_image_path.delete(0, "end")
        entry_image_path.insert(0, new_path)

def update_employee(emp_id, name, role, image_path, windowshow_staff):
    """แก้ไขข้อมูลพนักงาน"""
    try:
        cursor.execute("UPDATE picture SET name = ?, role = ?, image_path = ? WHERE id = ?", (name, role, image_path, emp_id))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error updating employee: {e}")

def edit_employee(emp_id, current_name, current_role, current_image_path, windowshow_staff):
    """เปิดหน้าต่างใหม่เพื่อแก้ไขข้อมูลพนักงาน"""
    edit_window = Toplevel(windowshow_staff)
    edit_window.title("แก้ไขข้อมูลพนักงาน")

    entry_name = Entry(edit_window)
    entry_name.grid(row=0, column=1, padx=20, pady=20)
    entry_name.insert(0, current_name)

    entry_role = Entry(edit_window)
    entry_role.grid(row=1, column=1, padx=20, pady=20)
    entry_role.insert(0, current_role)

    entry_image_path = Entry(edit_window)
    entry_image_path.grid(row=2, column=1, padx=20, pady=20)
    entry_image_path.insert(0, current_image_path)

    Button(edit_window, text="เลือกไฟล์", command=lambda: browse_image(entry_image_path)).grid(row=2, column=2, padx=10, pady=10)
    Button(edit_window, text="บันทึก", command=lambda: update_employee(emp_id, entry_name.get(), entry_role.get(), entry_image_path.get(), windowshow_staff)).grid(row=3, column=1, padx=10, pady=10)

    edit_window.mainloop()

def show_employees(windowshow_staff):
    """แสดงข้อมูลพนักงาน"""
    frame = Frame(windowshow_staff, bg="#f2d8d7")
    frame.pack(fill="both", expand=True)

    try:
        cursor.execute("SELECT id, name, role, image_path FROM picture ORDER BY id DESC")
        employees = cursor.fetchall()
    except Exception as e:
        print(f"Error fetching employees: {e}")
        return

    entry_name = customtkinter.CTkEntry(
        master=windowshow_staff,
        placeholder_text="name",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_name.place(x=20, y=20)

    entry_role = customtkinter.CTkEntry(
        master=windowshow_staff,
        placeholder_text="position",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_role.place(x=330, y=20)

    entry_image_path = customtkinter.CTkEntry(
        master=windowshow_staff,
        placeholder_text="image path",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_image_path.place(x=650, y=20)
    
    customtkinter.CTkButton(
        master=frame,
        text="file",
        font=("Georgia", 14),
        text_color="#000000",
        hover_color="#949494",
        height=40,
        width=100,
        border_width=2,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",
        command=lambda: browse_image(entry_image_path)
    ).place(x=980, y=20)

    customtkinter.CTkButton(
        master=frame,
        text="add",
        font=("Georgia", 14),
        text_color="#000000",
        hover_color="#949494",
        height=40,
        width=100,
        border_width=2,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff",
        command=lambda: add_employee(entry_name.get(), entry_role.get(), entry_image_path.get(), windowshow_staff)
    ).place(x=1100, y=20)

    # Display employees in a grid
    for index, (emp_id, name, role, image_path) in enumerate(employees):
        row = index // 3  # แถว (Row)
        col = index % 3   # คอลัมน์ (Column)

        emp_frame = Frame(frame, bg="#f2d8d7")
        emp_frame.grid(row=row, column=col, padx=85, pady=95, sticky="w")

        try:
            img = Image.open(image_path)
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            Label(emp_frame, image=img, bg="#f2d8d7").grid(row=0, column=0, padx=10)
            emp_frame.image = img
        except Exception as e:
            Label(emp_frame, text="Image not found", bg="white").grid(row=0, column=0, padx=5)
            print(f"Error loading image: {e}")

        Label(emp_frame, text=f"name: {name}\nposition: {role}", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").grid(row=1, column=0, padx=10, sticky="n")

        # ปุ่ม Delete
        customtkinter.CTkButton(
            master=emp_frame,
            text="Delete",
            font=("Georgia", 14),
            text_color="#000000",
            hover_color="#949494",
            height=40,
            width=100,
            border_width=2,
            corner_radius=20,
            border_color="#f2d8d7",
            bg_color="#f2d8d7",
            fg_color="#ffffff",
            command=lambda emp_id=emp_id: delete_employee(emp_id, windowshow_staff),
        ).grid(row=2, column=0, padx=10, pady=5)

        # ปุ่ม Edit
        customtkinter.CTkButton(
            master=emp_frame,
            text="Edit",
            font=("Georgia", 14),
            text_color="#000000",
            hover_color="#949494",
            height=40,
            width=100,
            border_width=2,
            corner_radius=20,
            border_color="#f2d8d7",
            bg_color="#f2d8d7",
            fg_color="#ffffff",
            command=lambda emp_id=emp_id, name=name, role=role, image_path=image_path: edit_employee(emp_id, name, role, image_path, windowshow_staff),
        ).grid(row=3, column=0, padx=10, pady=5)


def show_staff():
    """ฟังก์ชันเรียกหน้าต่างแสดงข้อมูลพนักงาน"""
    windowshow_staff = Toplevel()
    windowshow_staff.title("แสดงข้อมูลพนักงาน")
    windowshow_staff.configure(bg="#f2d8d7")
    windowshow_staff.geometry("1950x1080")

def refresh_ui(windowshow_staff):
    """รีเฟรชหน้าจอ"""
    for widget in windowshow_staff.winfo_children():
        widget.destroy()
    show_employees(windowshow_staff)

def add_employee(name, role, image_path, windowshow_staff):
    """เพิ่มพนักงานใหม่"""
    try:
        cursor.execute("INSERT INTO picture (name, role, image_path) VALUES (?, ?, ?)", (name, role, image_path))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error adding employee: {e}")

def delete_employee(emp_id, windowshow_staff):
    """ลบพนักงานออกจากฐานข้อมูล"""
    try:
        cursor.execute("SELECT image_path FROM picture WHERE id = ?", (emp_id,))
        image_path = cursor.fetchone()
        if image_path and os.path.exists(image_path[0]):
            os.remove(image_path[0])
        cursor.execute("DELETE FROM picture WHERE id = ?", (emp_id,))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error deleting employee: {e}")

def browse_image(entry_image_path):
    """เลือกไฟล์รูปภาพ"""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;*.jpeg")])
    if file_path:
        new_path = f"images/{os.path.basename(file_path)}"
        os.makedirs("images", exist_ok=True)
        shutil.copy(file_path, new_path)
        entry_image_path.delete(0, "end")
        entry_image_path.insert(0, new_path)

def update_employee(emp_id, name, role, image_path, windowshow_staff):
    """แก้ไขข้อมูลพนักงาน"""
    try:
        cursor.execute("UPDATE picture SET name = ?, role = ?, image_path = ? WHERE id = ?", (name, role, image_path, emp_id))
        conn.commit()
        refresh_ui(windowshow_staff)
    except Exception as e:
        print(f"Error updating employee: {e}")

def edit_employee(emp_id, current_name, current_role, current_image_path, windowshow_staff):
    """เปิดหน้าต่างใหม่เพื่อแก้ไขข้อมูลพนักงาน"""
    edit_window = Toplevel(windowshow_staff)
    edit_window.title("แก้ไขข้อมูลพนักงาน")

    entry_name = Entry(edit_window)
    entry_name.grid(row=0, column=1, padx=20, pady=20)
    entry_name.insert(0, current_name)

    entry_role = Entry(edit_window)
    entry_role.grid(row=1, column=1, padx=20, pady=20)
    entry_role.insert(0, current_role)

    entry_image_path = Entry(edit_window)
    entry_image_path.grid(row=2, column=1, padx=20, pady=20)
    entry_image_path.insert(0, current_image_path)

    Button(edit_window, text="เลือกไฟล์", command=lambda: browse_image(entry_image_path)).grid(row=2, column=2, padx=10, pady=10)
    Button(edit_window, text="บันทึก", command=lambda: update_employee(emp_id, entry_name.get(), entry_role.get(), entry_image_path.get(), windowshow_staff)).grid(row=3, column=1, padx=10, pady=10)

    edit_window.mainloop()

def show_employees(windowshow_staff):
    """แสดงข้อมูลพนักงาน"""
    frame = Frame(windowshow_staff, bg="#f2d8d7")
    frame.pack(fill="both", expand=True)

    try:
        cursor.execute("SELECT id, name, role, image_path FROM picture ORDER BY id DESC")
        employees = cursor.fetchall()
    except Exception as e:
        print(f"Error fetching employees: {e}")
        return

    entry_name = customtkinter.CTkEntry(
        master=windowshow_staff,
        placeholder_text="name",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_name.place(x=20, y=20)

    entry_role = customtkinter.CTkEntry(
        master=windowshow_staff,
        placeholder_text="position",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_role.place(x=330, y=20)

    entry_image_path = customtkinter.CTkEntry(
        master=windowshow_staff,
        placeholder_text="image path",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_image_path.place(x=650, y=20)
    
    customtkinter.CTkButton(
    master=frame,
    text="file",
    font=("Georgia", 14),
    text_color="#000000",
    hover_color="#949494",
    height=40,
    width=100,
    border_width=2,
    corner_radius=20,
    border_color="#f2d8d7",
    bg_color="#f2d8d7",
    fg_color="#ffffff",
    command=lambda: browse_image(entry_image_path)
).place(x=980, y=20)
    customtkinter.CTkButton(
    master=frame,
    text="add",
    font=("Georgia", 14),
    text_color="#000000",
    hover_color="#949494",
    height=40,
    width=100,
    border_width=2,
    corner_radius=20,
    border_color="#f2d8d7",
    bg_color="#f2d8d7",
    fg_color="#ffffff",
    command=lambda: add_employee(entry_name.get(), entry_role.get(), entry_image_path.get(), windowshow_staff)
).place(x=1100, y=20)

    # Display employees in a grid
    for index, (emp_id, name, role, image_path) in enumerate(employees):
        row = index // 3  # แถว (Row)
        col = index % 3   # คอลัมน์ (Column)

        emp_frame = Frame(frame, bg="#f2d8d7")
        emp_frame.grid(row=row, column=col, padx=85, pady=95, sticky="w")

        try:
            img = Image.open(image_path)
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            Label(emp_frame, image=img, bg="#f2d8d7").grid(row=0, column=0, padx=10)
            emp_frame.image = img
        except Exception as e:
            Label(emp_frame, text="Image not found", bg="white").grid(row=0, column=0, padx=5)
            print(f"Error loading image: {e}")

        Label(emp_frame, text=f"name: {name}\nposition: {role}", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").grid(row=1, column=0, padx=10, sticky="n")

        # ปุ่ม Delete
        customtkinter.CTkButton(
            master=emp_frame,
            text="Delete",
            font=("Georgia", 14),
            text_color="#000000",
            hover_color="#949494",
            height=40,
            width=100,
            border_width=2,
            corner_radius=20,
            border_color="#f2d8d7",
            bg_color="#f2d8d7",
            fg_color="#ffffff",
            command=lambda emp_id=emp_id: delete_employee(emp_id, windowshow_staff),
        ).grid(row=2, column=0, padx=10, pady=5)

        # ปุ่ม Edit
        customtkinter.CTkButton(
            master=emp_frame,
            text="Edit",
            font=("Georgia", 14),
            text_color="#000000",
            hover_color="#949494",
            height=40,
            width=100,
            border_width=2,
            corner_radius=20,
            border_color="#f2d8d7",
            bg_color="#f2d8d7",
            fg_color="#ffffff",
            command=lambda emp_id=emp_id, name=name, role=role, image_path=image_path: edit_employee(emp_id, name, role, image_path, windowshow_staff),
        ).grid(row=3, column=0, padx=10, pady=5)


def show_staff():
    """ฟังก์ชันเรียกหน้าต่างแสดงข้อมูลพนักงาน"""
    windowshow_staff = Toplevel()
    windowshow_staff.title("แสดงข้อมูลพนักงาน")
    windowshow_staff.configure(bg="#f2d8d7")
    windowshow_staff.geometry("1950x1080")
    canvas = Canvas(windowshow_staff, bg="#f2d8d7", highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(windowshow_staff, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # สร้าง Frame ภายใน Canvas
    frame = Frame(canvas, bg="#f2d8d7")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # ฟังก์ชันอัปเดต Scrollregion เมื่อเนื้อหาเปลี่ยน
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", update_scrollregion)

    # การเลื่อนด้วยเมาส์ (Windows ใช้ delta เป็น +/-120)
    def on_mouse_wheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # สำหรับ Windows
    canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))  # Linux (Scroll Up)
    canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))   # Linux (Scroll Down)

    show_employees(frame)
# แสดงข้อมูลพนักงานใน Frame


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk

    root = ttk.Tk()
    root.title("Image Viewer")

    menu = ttk.Menu(root)
    root.config(menu=menu)

    file_menu = ttk.Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open Image", command=open_image)

    panel = ttk.Label(root)
    panel.pack(padx=10, pady=10)
    root.mainloop()


#------------------------หน้า show service------------------------------------

def refresh_ui(window_showservice):
    """รีเฟรชหน้าจอ"""
    for widget in window_showservice.winfo_children():
        widget.destroy()
    show_showservice(window_showservice)

def add_showservice(name, price, image_path, window_showservice):
    """เพิ่มรายการสปาใหม่"""
    try:
        cursor.execute("INSERT INTO imageservice (name, price, image_path) VALUES (?, ?, ?)", (name, price, image_path))
        conn.commit()
        refresh_ui(window_showservice)
    except Exception as e:
        print(f"Error adding showservice: {e}")

def delete_showservice(ssv_id, window_showservice):
    """ลบรายการสปาออกจากฐานข้อมูล"""
    try:
        cursor.execute("SELECT image_path FROM imageservice WHERE id = ?", (ssv_id,))
        image_path = cursor.fetchone()
        if image_path and os.path.exists(image_path[0]):
            os.remove(image_path[0])
        cursor.execute("DELETE FROM imageservice WHERE id = ?", (ssv_id,))
        conn.commit()
        refresh_ui(window_showservice)
    except Exception as e:
        print(f"Error deleting showservice: {e}")

def browse_image(entry_image_path):
    """เลือกไฟล์รูปภาพ"""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;*.jpeg")])
    if file_path:
        new_path = f"c/{os.path.basename(file_path)}"
        os.makedirs("c", exist_ok=True)
        shutil.copy(file_path, new_path)
        entry_image_path.delete(0, "end")
        entry_image_path.insert(0, new_path)

def update_showservice(ssv_id, name, price, image_path, window_showservice):
    
    try:
        cursor.execute("UPDATE imageservice SET name = ?, price = ?, image_path = ? WHERE id = ?", (name, price, image_path, ssv_id))
        conn.commit()
        refresh_ui(window_showservice)
    except Exception as e:
        print(f"Error updating showservice: {e}")

def edit_shoeservice(ssv_id, current_name, current_price, current_image_path, window_showservice):
    
    edit_window = Toplevel(window_showservice)
    edit_window.title("แก้ไขข้อมูลรายการสปา")

    entry_name = Entry(edit_window)
    entry_name.grid(row=0, column=1, padx=20, pady=20)
    entry_name.insert(0, current_name)

    entry_price = Entry(edit_window)
    entry_price.grid(row=1, column=1, padx=20, pady=20)
    entry_price.insert(0, current_price)

    entry_image_path = Entry(edit_window)
    entry_image_path.grid(row=2, column=1, padx=20, pady=20)
    entry_image_path.insert(0, current_image_path)

    Button(edit_window, text="เลือกไฟล์", command=lambda: browse_image(entry_image_path)).grid(row=2, column=2, padx=10, pady=10)
    Button(edit_window, text="บันทึก", command=lambda: update_showservice(ssv_id, entry_name.get(), entry_price.get(), entry_image_path.get(), window_showservice)).grid(row=3, column=1, padx=10, pady=10)

    edit_window.mainloop()

def show_showservice(window_showservice):
    """แสดงข้อมูลบริการ"""
    frame = Frame(window_showservice, bg="#f2d8d7")
    frame.pack(fill="both", expand=True)

    try:
        cursor.execute("SELECT id, name, price, image_path FROM imageservice ORDER BY id DESC")
        showservice = cursor.fetchall()
    except Exception as e:
        print(f"Error fetching showservice: {e}")
        return

    entry_name = customtkinter.CTkEntry(
        master=window_showservice,
        placeholder_text="name",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_name.place(x=20, y=20)

    entry_price = customtkinter.CTkEntry(
        master=window_showservice,
        placeholder_text="price",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_price.place(x=330, y=20)

    entry_image_path = customtkinter.CTkEntry(
        master=window_showservice,
        placeholder_text="image path",
        placeholder_text_color="#454545",
        font=("Georgia", 14),
        text_color="#000000",
        height=50,
        width=250,
        border_width=1,
        corner_radius=20,
        border_color="#f2d8d7",
        bg_color="#f2d8d7",
        fg_color="#ffffff"
    )
    entry_image_path.place(x=650, y=20)
    
    customtkinter.CTkButton(
    master=frame,
    text="file",
    font=("Georgia", 14),
    text_color="#000000",
    hover_color="#949494",
    height=40,
    width=100,
    border_width=2,
    corner_radius=20,
    border_color="#f2d8d7",
    bg_color="#f2d8d7",
    fg_color="#ffffff",
    command=lambda: browse_image(entry_image_path)
    ).place(x=980, y=20)

    customtkinter.CTkButton(
    master=frame,
    text="add",
    font=("Georgia", 14),
    text_color="#000000",
    hover_color="#949494",
    height=40,
    width=100,
    border_width=2,
    corner_radius=20,
    border_color="#f2d8d7",
    bg_color="#f2d8d7",
    fg_color="#ffffff",
    command=lambda: add_showservice(entry_name.get(), entry_price.get(), entry_image_path.get(), window_showservice)
    ).place(x=1100, y=20)

    # Display showservice in a grid
    for index, (ssv_id, name, price, image_path) in enumerate(showservice):
        row = index // 3  # แถว (Row)
        col = index % 3   # คอลัมน์ (Column)

        ssv_frame = Frame(frame, bg="#f2d8d7")
        ssv_frame.grid(row=row, column=col, padx=85, pady=95, sticky="w")

        try:
            img = Image.open(image_path)
            img = img.resize((300, 300), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            Label(ssv_frame, image=img, bg="#f2d8d7").grid(row=0, column=0, padx=10)
            ssv_frame.image = img
        except Exception as e:
            Label(ssv_frame, text="Image not found", bg="white").grid(row=0, column=0, padx=5)
            print(f"Error loading image: {e}")

        Label(ssv_frame, text=f"{name}\nprice: {price} baht", font=("Georgia", 14), bg="#f2d8d7", fg="#000000").grid(row=1, column=0, padx=10, sticky="n")

        # ปุ่ม Delete
        customtkinter.CTkButton(
            master=ssv_frame,
            text="Delete",
            font=("Georgia", 14),
            text_color="#000000",
            hover_color="#949494",
            height=40,
            width=100,
            border_width=2,
            corner_radius=20,
            border_color="#f2d8d7",
            bg_color="#f2d8d7",
            fg_color="#ffffff",
            command=lambda ssv_id=ssv_id: delete_showservice(ssv_id, window_showservice),
        ).grid(row=2, column=0, padx=10, pady=5)

        # ปุ่ม Edit
        customtkinter.CTkButton(
            master=ssv_frame,
            text="Edit",
            font=("Georgia", 14),
            text_color="#000000",
            hover_color="#949494",
            height=40,
            width=100,
            border_width=2,
            corner_radius=20,
            border_color="#f2d8d7",
            bg_color="#f2d8d7",
            fg_color="#ffffff",
            command=lambda ssv_id=ssv_id, name=name, price=price, image_path=image_path: edit_shoeservice(ssv_id, name, price, image_path, window_showservice),
        ).grid(row=3, column=0, padx=10, pady=5)


def show_service():
    """ฟังก์ชันเรียกหน้าต่างแสดงข้อมูลบริการ"""
    window_showservice = Toplevel()
    window_showservice.title("แสดงข้อมูลรายการสปา")
    window_showservice.configure(bg="#f2d8d7")
    window_showservice.geometry("1950x1080")

    canvas = Canvas(window_showservice, bg="#f2d8d7", highlightthickness=0)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(window_showservice, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # สร้าง Frame ภายใน Canvas
    frame = Frame(canvas, bg="#f2d8d7")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # ฟังก์ชันอัปเดต Scrollregion เมื่อเนื้อหาเปลี่ยน
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", update_scrollregion)

    # การเลื่อนด้วยเมาส์ (Windows ใช้ delta เป็น +/-120)
    def on_mouse_wheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)  # สำหรับ Windows
    canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))  # Linux (Scroll Up)
    canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))   # Linux (Scroll Down)
    
    show_showservice(frame)
    
# แสดงข้อมูลพนักงานใน Frame


# Run the main loop
window.mainloop()
