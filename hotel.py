from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import filedialog,messagebox
from PyQt5.QtPrintSupport import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
# from bill import *
import os
import sys
import random
import time 
import pymysql
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector

mydb=pymysql.connect(host="localhost",user="root",password="",database="project")
cursor=mydb.cursor()

root=Tk()
root.geometry('1920x960+0+0')
root.config(bg='firebrick4')
root.title('Hotel Management System ')

def Window1():
    def Update(rows):
        room_table.delete(*room_table.get_children())
        for i in rows:
            room_table.insert('','end',values=i)
    def getrow(event):
        rowid=room_table.identify_row(event.y)
        item=room_table.item(room_table.focus())
        room_no_var.set(item['values'][0])
        room_type_var.set(item['values'][1])
        room_rate_var.set(item['values'][2])

    def add_rooms():
        if room_no_var.get()=="" or room_type_var.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=conn.cursor()
                cur.execute("insert into rooms(room_no,room_type,room_rate)values(%s,%s,%s)",(room_no_var.get(),
                                                    room_type_var.get(),
                                                    room_rate_var.get(),
                                                    ))

                conn.commit()
                fetch_room_data()
                conn.close()                                    
                messagebox.showinfo("success","customer has been added",parent=root) 
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=root)                   

    def fetch_room_data():
        conn=pymysql.connect(host="localhost",user="root",password="",database="project")
        cur=conn.cursor()
        cur.execute("select * from rooms")
        rows=cur.fetchall()
        if len(rows)!=0:
            room_table.delete(*room_table.get_children())
            for row in rows:
                room_table.insert('',END,values=row)
            conn.commit()
        conn.close()

    def Update1(rows):
        hall_table.delete(*hall_table.get_children())
        for i in rows:
            hall_table.insert('','end',values=i)
    def getrow1(event):
        rowid=hall_table.identify_row(event.y)
        item=hall_table.item(hall_table.focus())
        hall_no_var.set(item['values'][0])
        hall_seting_capacity_var.set(item['values'][1])
        hall_rate_var.set(item['values'][2])

    def add_hall():        
        if hall_seting_capacity_var.get()=="" or hall_rate_var.get()=="":
            messagebox.showerror("Error","All fields are requaired")
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=conn.cursor()
                cur.execute("insert into hall(hall_no,hall_seting_capacity,hall_rate)values(%s,%s,%s)",
                            (hall_no_var.get(),hall_seting_capacity_var.get(),hall_rate_var.get()))

                conn.commit()
                fetch_hall_data()
                conn.close()                                                  
                messagebox.showinfo("success","customer has been added",parent=root) 
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=root)          
    def fetch_hall_data():
        conn=pymysql.connect(host="localhost",user="root",password="",database="project")
        cur=conn.cursor()
        cur.execute("select * from hall")
        rows=cur.fetchall()
        if len(rows)!=0:
            hall_table.delete(*hall_table.get_children())
            for row in rows:
                hall_table.insert('',END,values=row)
            conn.commit()
        conn.close()
    
    #============== all variable==================
    room_no_var=StringVar()
    room_type_var=StringVar()
    room_rate_var=StringVar()
    hall_no_var=StringVar()
    hall_seting_capacity_var=StringVar()
    hall_rate_var=StringVar()

    topFrame=Frame(root,bd=8,relief=RIDGE,width=910,height=80)
    topFrame.place(x=360,y=1)

    labelTitle=Label(topFrame,text='Add Room and Hall',font=('times new roman',30,'bold'))
    labelTitle.place(x=150,y=1)
    #====================main =========================
    rightFrame=Frame(root,bd=8,relief=RIDGE,width=910,height=570)
    rightFrame.place(x=360,y=80)

    roomFrame=Frame(rightFrame,bd=8,relief=RIDGE,width=446,height=550)
    roomFrame.place(x=1,y=1)

    rooms_detailsFrame=LabelFrame(roomFrame,font=('times new roman',19,'bold'),bd=8,fg='black',width=428,height=130)
    rooms_detailsFrame.place(x=1,y=1)

    labelCostofFood=Label(rooms_detailsFrame,text='Room No:-',font=('times new roman',14),fg='black',).place(x=1,y=1)
    textCostofFood=Entry(rooms_detailsFrame,textvariable=room_no_var,font=('times new roman',14),bd=6,width=10).place(x=150,y=1)

    ttk.Label(rooms_detailsFrame,text = "Room Type:-",font = ("Times New Roman", 14)).place(x=1,y=40)
  
    # Create Combobox
    country = ttk.Combobox(rooms_detailsFrame, width =20, textvariable =room_type_var ) 
  
    # Adding combobox drop down list 
    country['values'] = (' AC', ' Single', ' Double')
    country.place(x=150,y=40,height=28)
    country.current()

    buttonReset=Button(rooms_detailsFrame,command=add_rooms,text='Add',font=('times new roman',14,'bold'),bd=3,fg='black',bg='red4')
    buttonReset.place(x=310,y=30)

    labelCostofFood=Label(rooms_detailsFrame,text='Room Rate:-',font=('times new roman',14),fg='black',).place(x=1,y=75)
    textCostofFood=Entry(rooms_detailsFrame,textvariable=room_rate_var,font=('times new roman',14),bd=6,width=10).place(x=150,y=75)
    #===========search Frame==========
    room_view_Frame=Frame(roomFrame,bd=8,relief=RIDGE)
    room_view_Frame.place(x=1,y=130,width=428,height=400)

    scroll_x=Scrollbar(room_view_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(room_view_Frame,orient=VERTICAL)
    room_table=ttk.Treeview(room_view_Frame,columns=("room_no","room_type","room_rate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=room_table.xview)
    scroll_y.config(command=room_table.yview)
    room_table.heading("room_no",text="Room No.")
    room_table.heading("room_type",text="Room Type")
    room_table.heading("room_rate",text="Room Rate")
    room_table['show']='headings'
    room_table.column("room_no",width=135)
    room_table.column("room_type",width=135)
    room_table.column("room_rate",width=135)
    room_table.pack(fill=BOTH,expand=1)
    room_table.bind('<Double 1>' ,getrow)
    fetch_room_data()

    hallFrame=Frame(rightFrame,bd=8,relief=RIDGE,width=446,height=550)
    hallFrame.place(x=446,y=1)

    hall_view_Frame=Frame(hallFrame,bd=8,relief=RIDGE)
    hall_view_Frame.place(x=1,y=130,width=428,height=400)

    scroll_x=Scrollbar(hall_view_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(hall_view_Frame,orient=VERTICAL)
    hall_table=ttk.Treeview(hall_view_Frame,columns=("hall_no","hall_seting_capacity","hall_rate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=hall_table.xview)
    scroll_y.config(command=hall_table.yview)
    hall_table.heading("hall_no",text=" Hall No.")
    hall_table.heading("hall_seting_capacity",text="Hall seting capacity")
    hall_table.heading("hall_rate",text="Hall Rate")
    hall_table['show']='headings'
    hall_table.column("hall_no",width=135)
    hall_table.column("hall_seting_capacity",width=135)
    hall_table.column("hall_rate",width=135)
    hall_table.pack(fill=BOTH,expand=1)
    hall_table.bind('<Double 1>' ,getrow1)

    query="SELECT hall_no,hall_seting_capacity,hall_rate from hall"
    cursor.execute(query)
    rows=cursor.fetchall()
    Update1(rows)

    halls_detailsFrame=LabelFrame(hallFrame,font=('times new roman',19,'bold'),bd=8,fg='black',width=428,height=130)
    halls_detailsFrame.place(x=1,y=1)

    labelCostofFood=Label(halls_detailsFrame,text='Hall No:-',font=('times new roman',14),fg='black',)
    labelCostofFood.place(x=1,y=1)
    textCostofFood=Entry(halls_detailsFrame,textvariable=hall_no_var,font=('times new roman',14),bd=6,width=10)
    textCostofFood.place(x=170,y=1)

    labelTitle=Label(halls_detailsFrame,text='Hall Seting Capacity:-',font=('times new roman',14))
    labelTitle.place(x=1,y=40)
    sb1 = Spinbox(halls_detailsFrame,textvariable=hall_seting_capacity_var, from_= 50, to = 500,width=5)
    sb1.place(x=170,y=40,height=28)

    buttonReset=Button(halls_detailsFrame,text='Add',command=add_hall,font=('times new roman',14,'bold'),bd=3,fg='black',bg='red4')
    buttonReset.place(x=310,y=30)

    labelCostofFood=Label(halls_detailsFrame,text='Hall Rate:-',font=('times new roman',14),fg='black',)
    labelCostofFood.place(x=1,y=75)
    textCostofFood=Entry(halls_detailsFrame,textvariable=hall_rate_var,font=('times new roman',14),bd=6,width=10)
    textCostofFood.place(x=170,y=75)

def Window2():
    def check():
            conn=pymysql.connect(host="localhost",user="root",password="",database="project")
            cur=conn.cursor()
            cur.execute("SELECT  room_no,room_type FROM rooms WHERE room_no not in (SELECT room_number  FROM room_booking WHERE ((arrival_date = '"+ str(a1_var.get())+ "') and (departure_date = '" + str(d1_var.get())+"')))")
            rows = cur.fetchall()
            if len(rows)!=0:
                    room_table.delete(*room_table.get_children())
                    for row in rows:
                        room_table.insert('',END,values=row)
                    conn.commit()
            conn.close()


    def check_hall():
            conn=pymysql.connect(host="localhost",user="root",password="",database="project")
            cur=conn.cursor()
            cur.execute("SELECT  hall_no,hall_seting_capacity FROM hall WHERE hall_no not in (SELECT hall_no  FROM hall_booking WHERE ((arrival_date = '"+ str(ar1_var.get())+ "') and (departure_date = '" + str(dp1_var.get())+"')))")
            rows = cur.fetchall()
            if len(rows)!=0:
                    hall_table.delete(*hall_table.get_children())
                    for row in rows:
                        hall_table.insert('',END,values=row)
                    conn.commit()
            conn.close()
    #==================variable===============
    a1_var=StringVar()
    d1_var=StringVar()
    ar1_var=StringVar()
    dp1_var=StringVar()

    topFrame=Frame(root,bd=8,relief=RIDGE,width=910,height=80)
    topFrame.place(x=360,y=1)

    labelTitle=Label(topFrame,text='Rooms/halls check availabity and view',font=('times new roman',30,'bold'))
    labelTitle.place(x=150,y=1)

    rightFrame=Frame(root,bd=8,relief=RIDGE,width=910,height=570)
    rightFrame.place(x=360,y=80)

    roomFrame=Frame(rightFrame,bd=8,relief=RIDGE,width=446,height=550)
    roomFrame.place(x=1,y=1)

    rooms_detailsFrame=LabelFrame(roomFrame,text='Rooms Details',font=('times new roman',19,'bold'),bd=8,fg='black',width=400,height=120)
    rooms_detailsFrame.place(x=10,y=1)

    labelArrival_Date=Label(rooms_detailsFrame,text='Arrival_Date',font=('times new roman',16,'bold'))
    labelArrival_Date.place(x=1,y=1)
    calArrival_Date= DateEntry(rooms_detailsFrame,textvariable=a1_var, width=12,background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=5)

    labelDeparture_Date=Label(rooms_detailsFrame,text='Departure_Date',font=('times new roman',16,'bold'))
    labelDeparture_Date.place(x=1,y=35)
    calArrival_Date= DateEntry(rooms_detailsFrame, width=12,textvariable=d1_var, background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=40)

    buttonReset=Button(rooms_detailsFrame,text='Check',command=check,font=('times new roman',14,'bold'),bd=3,padx=5,fg='black',bg='red4')
    buttonReset.place(x=280,y=13)

    searchFrame=Frame(roomFrame,bd=8,relief=RIDGE)
    searchFrame.place(x=1,y=120,width=428,height=412)

    scroll_x=Scrollbar(searchFrame,orient=HORIZONTAL)
    scroll_y=Scrollbar(searchFrame,orient=VERTICAL)
    room_table=ttk.Treeview(searchFrame,columns=(1,2),show="headings",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=room_table.xview)
    scroll_y.config(command=room_table.yview)
    room_table.heading(1,text="Room No")
    room_table.heading(2,text="Room Type")
    room_table.column(1,width=130)
    room_table.column(2,width=130)
    room_table.pack(fill=BOTH,expand=1)

    room_table.pack()
    hallFrame=Frame(rightFrame,bd=8,relief=RIDGE,width=446,height=550)
    hallFrame.place(x=446,y=1)
    searchFrame=Frame(hallFrame,bd=8,relief=RIDGE)
    searchFrame.place(x=1,y=120,width=428,height=412)

    scroll_x=Scrollbar(searchFrame,orient=HORIZONTAL)
    scroll_y=Scrollbar(searchFrame,orient=VERTICAL)
    hall_table=ttk.Treeview(searchFrame,columns=(1,2),show="headings",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=hall_table.xview)
    scroll_y.config(command=hall_table.yview)
    hall_table.heading(1,text="hall No")
    hall_table.heading(2,text="hall_seting_capacity")
    hall_table.column(1,width=130)
    hall_table.column(2,width=130)
    hall_table.pack(fill=BOTH,expand=1)

    hall_table.pack()

    halls_detailsFrame=LabelFrame(hallFrame,text='Halls Details',font=('times new roman',19,'bold'),bd=8,fg='black',width=400,height=120)
    halls_detailsFrame.place(x=10,y=1)

    labelArrival_Date=Label(halls_detailsFrame,text='Arrival_Date',font=('times new roman',16,'bold'))
    labelArrival_Date.place(x=1,y=1)
    calArrival_Date= DateEntry(halls_detailsFrame, width=12,textvariable=ar1_var, background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=5)

    labelDeparture_Date=Label(halls_detailsFrame,text='Departure_Date',font=('times new roman',16,'bold'))
    labelDeparture_Date.place(x=1,y=35)
    calArrival_Date= DateEntry(halls_detailsFrame, width=12,textvariable=dp1_var,background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=40)

    buttonReset=Button(halls_detailsFrame,text='Check',command=check_hall,font=('times new roman',14,'bold'),bd=3,padx=5,fg='black',bg='red4')
    buttonReset.place(x=280,y=13)

def Window3():
    def add_customer():
            if first_name_var.get()=="" or id_type_var.get()=="":
                messagebox.showerror("Error","All fields are requaired")
            else:
                try:

                    conn=pymysql.connect(host="localhost",user="root",password="",database="project")
                    cur=conn.cursor()
                    cur.execute("insert into customer(first_name,last_name,mobile_no,address,id_type,id_no)values(%s,%s,%s,%s,%s,%s)",
                                                                        (first_name_var.get(),
                                                                        last_name_var.get(),
                                                                        mobile_no_var.get(),
                                                                        address_var.get(),
                                                                        id_type_var.get(),
                                                                        id_no_var.get()
                                                                        ))
                    conn.commit()
                    fetch_customer_data()
                    conn.close()                                    
                    messagebox.showinfo("success","customer has been added",parent=root) 
                except Exception as es:
                    messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=root)                   


    def getrow(event):
            rowid=customer_table.identify_row(event.y)
            item=customer_table.item(customer_table.focus())
            first_name_var.set(item['values'][0])
            last_name_var.set(item['values'][1])
            mobile_no_var.set(item['values'][2])
            address_var.set(item['values'][3])
            id_type_var.set(item['values'][4])
            id_no_var.set(item['values'][5])
      
    def fetch_customer_data():
            conn=pymysql.connect(host="localhost",user="root",password="",database="project")
            cur=conn.cursor()
            cur.execute("select * from customer")
            rows=cur.fetchall()
            if len(rows)!=0:
                customer_table.delete(*customer_table.get_children())
                for row in rows:
                    customer_table.insert('',END,values=row)
                conn.commit()
            conn.close()

        #============== all variable==================
    first_name_var=StringVar()
    last_name_var=StringVar()
    mobile_no_var=StringVar()
    address_var=StringVar()
    id_type_var=StringVar()
    id_no_var=StringVar()

    topFrame=Frame(root,bd=8,relief=RIDGE,width=900,height=80)
    topFrame.place(x=360,y=1)

    labelTitle=Label(topFrame,text='Customer Information / View',font=('times new roman',30,'bold'))
    labelTitle.place(x=250,y=1)

    rightFrame=Frame(root,bd=8,relief=RIDGE,width=900,height=580)
    rightFrame.place(x=360,y=80)

    labelTitle=Label(rightFrame,text='Personal Information',font=('times new roman',20,'bold'))
    labelTitle.place(x=300,y=1)
    labelCostofFood=Label(rightFrame,text='First Name:-',font=('times new roman',16),fg='black',)
    labelCostofFood.place(x=50,y=45)
    textCostofFood=Entry(rightFrame,font=('times new roman',16,'bold'),textvariable=first_name_var,bd=6,width=20)
    textCostofFood.place(x=170,y=45)

    labelCostofFood=Label(rightFrame,text='Last Name:-',font=('times new roman',16,),fg='black',)
    labelCostofFood.place(x=450,y=45)
    textCostofFood=Entry(rightFrame,font=('times new roman',16,'bold'),textvariable=last_name_var,bd=6,width=20)
    textCostofFood.place(x=565,y=45)

    labelTitle=Label(rightFrame,text='Contact Information',font=('times new roman',20,'bold'))
    labelTitle.place(x=300,y=85)
    labelCostofFood=Label(rightFrame,text='mobile Number:-',font=('times new roman',16),fg='black',)
    labelCostofFood.place(x=50,y=125)
    textCostofFood=Entry(rightFrame,font=('times new roman',16,'bold'),textvariable=mobile_no_var,bd=6,width=20)
    textCostofFood.place(x=200,y=125)

    labelCostofFood=Label(rightFrame,text='Address:-',font=('times new roman',16,),fg='black',)
    labelCostofFood.place(x=450,y=125)
    textCostofFood=Entry(rightFrame,font=('times new roman',16,'bold'),textvariable=address_var,bd=6,width=20)
    textCostofFood.place(x=565,y=125)

    labelTitle=Label(rightFrame,text='Identification Information',font=('times new roman',20,'bold'))
    labelTitle.place(x=300,y=165)
    Label(rightFrame, text="ID Type *  :- ",font=('times new roman',16),fg='black').place(x=50, y=200)
    # state combobox
    monthchoosen = ttk.Combobox(rightFrame,font=('times new roman',16,'bold'),textvariable=id_type_var,width=19)
    monthchoosen['values'] = (' AdharCard',' Driving Licence',' Passport')
    monthchoosen.current()
    monthchoosen.place(x=200, y=200)

    labelCostofFood=Label(rightFrame,text='ID Number :-',font=('times new roman',16,),fg='black',)
    labelCostofFood.place(x=450,y=200)
    textCostofFood=Entry(rightFrame,font=('times new roman',16,'bold'),textvariable=id_no_var,bd=6,width=20)
    textCostofFood.place(x=565,y=200)

    buttonReset=Button(rightFrame,text='Submit',command=add_customer,font=('times new roman',14,'bold'),bd=3,padx=5,fg='black',bg='red4')
    buttonReset.place(x=400,y=250)

    customerFrame=Frame(rightFrame,bd=8,relief=RIDGE)
    customerFrame.place(x=1,y=300,width=870,height=250)

    scroll_x=Scrollbar(customerFrame,orient=HORIZONTAL)
    scroll_y=Scrollbar(customerFrame,orient=VERTICAL)
    customer_table=ttk.Treeview(customerFrame,columns=("first_name","last_name","mobile_no","address","id_type","id_no"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=customer_table.xview)
    scroll_y.config(command=customer_table.yview)
    customer_table.heading("first_name",text="First Name.")
    customer_table.heading("last_name",text="Last Name.")
    customer_table.heading("mobile_no",text="Mobile Number.")
    customer_table.heading("address",text="Address.")
    customer_table.heading("id_type",text="ID Type.")
    customer_table.heading("id_no",text="ID Number.")

    customer_table['show']='headings'
    customer_table.column("first_name",width=150)
    customer_table.column("last_name",width=150)
    customer_table.column("mobile_no",width=150)
    customer_table.column("address",width=150)
    customer_table.column("id_type",width=150)
    customer_table.column("id_no",width=150)
    fetch_customer_data()
    customer_table.pack(fill=BOTH,expand=1)
    customer_table.bind('<Double 1>' ,getrow)

def Window4():

    mydb=pymysql.connect(host="localhost",user="root",password="",database="project")
    cursor=mydb.cursor()

    #=====================variables==========================
    type_of_room_var=StringVar()
    room_number_var=StringVar()
    arrival_date_var=StringVar()
    departure_date_var=StringVar()
    advance_payment_var=StringVar()

    #===================functions============================

    def Update(rows):
        room_table.delete(*room_table.get_children())
        for i in rows:
            room_table.insert('','end',values=i)

    def search():
        q2=type_of_room_var.get()
        query="SELECT room_no,room_type from rooms WHERE room_type LIKE '%"+q2+"%'"
        cursor.execute(query)
        rows=cursor.fetchall()
        Update(rows)
 
    def clear():
        query="SELECT room_no,room_type from rooms"
        cursor.execute(query)
        rows=cursor.fetchall()
        Update(rows)

    def getrow(event):
        rowid=room_table.identify_row(event.y)
        item=room_table.item(room_table.focus())
        room_number_var.set(item['values'][0])
        type_of_room_var.set(item['values'][1])
   

    def add_room():
        
        if advance_payment_var.get()=="" or  type_of_room_var.get()=="":
            messagebox.showerror("Error","All fields are requaired")
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=conn.cursor()
                cur.execute("insert into room_booking (arrival_date,departure_date,advance_payment,type_of_room,room_number)values(%s,%s,%s,%s,%s)",
                                                                            (arrival_date_var.get(),
                                                                            departure_date_var.get(),
                                                                            advance_payment_var.get(),
                                                                            type_of_room_var.get(),
                                                                            room_number_var.get()
                                                                            ))
                conn.commit()
                fetch_room_booking_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=root) 
            except Exception as es:
                 messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=root)           
            
    def fetch_room_booking_data():
        conn=pymysql.connect(host="localhost",user="root",password="",database="project")
        cur=conn.cursor()
        cur.execute("select * from room_booking")
        rows=cur.fetchall()
        if len(rows)!=0:
            customer_table.delete(*customer_table.get_children())
            for row in rows:
                customer_table.insert('',END,values=row)
            conn.commit()
        conn.close()

    topFrame=Frame(root,bd=8,relief=RIDGE,width=900,height=80)
    topFrame.place(x=360,y=1)

    labelTitle=Label(topFrame,text='Room Booking and View',font=('times new roman',30,'bold'))
    labelTitle.place(x=320,y=1)

    rightFrame=Frame(root,bd=10,relief=RIDGE,width=900,height=250)
    rightFrame.place(x=360,y=82)

    labelArrival_Date=Label(rightFrame,text='Arrival_Date',font=('times new roman',14))
    labelArrival_Date.place(x=10,y=1)
    calArrival_Date= DateEntry(rightFrame,textvariable=arrival_date_var, width=12,background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=5)

    labelDeparture_Date=Label(rightFrame,text='Departure_Date',font=('times new roman',14))
    labelDeparture_Date.place(x=10,y=40)
    calArrival_Date= DateEntry(rightFrame,textvariable=departure_date_var, width=12,background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=40)
    ttk.Label(rightFrame, text = "Advance Payment", 
            font = ("Times New Roman", 14)).place(x=1,y=80)
    
    # Create Combobox
    n = tk.StringVar() 
    country = ttk.Combobox(rightFrame, width = 10, textvariable =advance_payment_var) 
    
    # Adding combobox drop down list 
    country['values'] = ("Paid") 
    
    country.place(x=150,y=80)
    country.current()


    buttonReset=Button(rightFrame,command=add_room,text='Confirm',font=('times new roman',14,'bold'),bd=5,fg='black',bg='red4')
    buttonReset.place(x=50,y=150)

    wrapper1=LabelFrame(rightFrame,text="rooms list")
    wrapper1.place(x=500,y=1,width=380,height=230)

    wrapper2=LabelFrame(rightFrame,text="search")
    wrapper2.place(x=270,y=1,width=220,height=230)

    lbl=Label(wrapper2,text="room type")
    lbl.grid(row=0,column=0,padx=6,pady=3)
    ent=Entry(wrapper2,textvariable=type_of_room_var)
    ent.grid(row=1,column=0,padx=6,pady=3)
    lbl=Label(wrapper2,text="room number")
    lbl.grid(row=2,column=0,padx=6,pady=3)
    ent=Entry(wrapper2,textvariable=room_number_var)
    ent.grid(row=3,column=0,padx=6,pady=3)
    btn=Button(wrapper2,text="search",command=search,fg='black',bg='red4')
    btn.grid(row=1,column=1,padx=6,pady=3)
    cbtn=Button(wrapper2,text="clear",command=clear,fg='black',bg='red4')
    cbtn.grid(row=2,column=1,padx=6,pady=3)

    scroll_x=Scrollbar(wrapper1,orient=HORIZONTAL)
    scroll_y=Scrollbar(wrapper1,orient=VERTICAL)
    room_table=ttk.Treeview(wrapper1,columns=(1,2),show="headings",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=room_table.xview)
    scroll_y.config(command=room_table.yview)
    room_table.heading(1,text="room no")
    room_table.heading(2,text="room type")
    room_table.pack()
    room_table.bind('<Double 1>' ,getrow)

    query="SELECT room_no,room_type from rooms"
    cursor.execute(query)
    rows=cursor.fetchall()
    Update(rows)

    searchFrame=Frame(root,bd=8,relief=RIDGE)
    searchFrame.place(x=372,y=334,width=898,height=300)

    scroll_x=Scrollbar(searchFrame,orient=HORIZONTAL)
    scroll_y=Scrollbar(searchFrame,orient=VERTICAL)
    customer_table=ttk.Treeview(searchFrame,columns=(1,2,3,4,5),show="headings",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=customer_table.xview)
    scroll_y.config(command=customer_table.yview)
    customer_table.heading(1,text="Arrival Date")
    customer_table.heading(2,text="Departure Date")
    customer_table.heading(3,text="Advance Payment")
    customer_table.heading(4,text="room type")
    customer_table.heading(5,text="room no")
    customer_table.pack()
    fetch_room_booking_data()

def Window5():
    
    mydb=pymysql.connect(host="localhost",user="root",password="",database="project")
    cursor=mydb.cursor()

    #=====================variables==========================
    arrival_date_var=StringVar()
    departure_date_var=StringVar()
    advance_payment_var=StringVar()
    hall_no_var=StringVar()
    Facilities_var=StringVar()
    #===================functions============================

    def hall_booking():
        
        if hall_no_var.get()=="" or arrival_date_var.get()=="":
            messagebox.showerror("Error","All fields are requaired")
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=conn.cursor()
             
                    
                cur.execute("insert into hall_booking (arrival_date,departure_date,advance_payment,hall_no,facilities)values(%s,%s,%s,%s,%s)",
                                                                            (arrival_date_var.get(),
                                                                            departure_date_var.get(),
                                                                            advance_payment_var.get(),
                                                                            hall_no_var.get(),
                                                                            Facilities_var.get()
                                                                            ))
                conn.commit()
                fetch_hall_booking_data()
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=root) 
            except Exception as es:
                 messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=root) 
     
    def fetch_hall_booking_data():
        conn=pymysql.connect(host="localhost",user="root",password="",database="project")
        cur=conn.cursor()
        cur.execute("select * from hall_booking")
        rows=cur.fetchall()
        if len(rows)!=0:
            customer_table.delete(*customer_table.get_children())
            for row in rows:
                customer_table.insert('',END,values=row)
            conn.commit()
        conn.close()
    
    topFrame=Frame(root,bd=8,relief=RIDGE,width=900,height=80)
    topFrame.place(x=360,y=1)

    labelTitle=Label(topFrame,text='Halls Booking and View',font=('times new roman',30,'bold'))
    labelTitle.place(x=250,y=1)

    rightFrame=Frame(root,bd=10,relief=RIDGE,width=900,height=220)
    rightFrame.place(x=360,y=82)

    labelArrival_Date=Label(rightFrame,text='Arrival_Date',font=('times new roman',14))
    labelArrival_Date.place(x=10,y=1)
    calArrival_Date= DateEntry(rightFrame,textvariable=arrival_date_var, width=12, 
    background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=5)

    labelDeparture_Date=Label(rightFrame,text='Departure_Date',font=('times new roman',14))
    labelDeparture_Date.place(x=10,y=40)
    calArrival_Date= DateEntry(rightFrame,textvariable=departure_date_var, width=12,background='darkblue', foreground='black', borderwidth=2)
    calArrival_Date.place(x=160,y=40)

    ttk.Label(rightFrame, text = "Hall No:", 
            font = ("Times New Roman", 14)).place(x=10,y=80)
    
    # Create Combobox
    n = tk.StringVar() 
    country = ttk.Combobox(rightFrame, width = 20, textvariable =hall_no_var) 
    
    # Adding combobox drop down list 
    country['values'] = (' 1',  
                            ' 2', 
                            ' 3', 
                            ' 4', 
                            ' 5') 
    
    country.place(x=160,y=80) 
    country.current()

    ttk.Label(rightFrame, text = "Facilities", 
            font = ("Times New Roman", 14)).place(x=10,y=120)
    
    # Create Combobox
    n = tk.StringVar() 
    country = ttk.Combobox(rightFrame, width = 20, textvariable =Facilities_var) 
    
    # Adding combobox drop down list 
    country['values'] = ("wedding","birthday","business meeting") 
    
    country.place(x=160,y=120)
    country.current()
    ttk.Label(rightFrame, text = "Advance Payment", 
            font = ("Times New Roman", 14)).place(x=10,y=160)
    
    # Create Combobox
    n = tk.StringVar() 
    country = ttk.Combobox(rightFrame, width = 10, textvariable =advance_payment_var) 
    
    # Adding combobox drop down list 
    country['values'] = ("Paid") 
    
    country.place(x=160,y=160)
    country.current()

    buttonReset=Button(rightFrame,text='Submit',command=hall_booking,font=('times new roman',14,'bold'),bd=5,fg='black',bg='red4')
    buttonReset.place(x=400,y=80)

    searchFrame=Frame(root,bd=8,relief=RIDGE)
    searchFrame.place(x=360,y=300,width=900,height=360)

    scroll_x=Scrollbar(searchFrame,orient=HORIZONTAL)
    scroll_y=Scrollbar(searchFrame,orient=VERTICAL)
    customer_table=ttk.Treeview(searchFrame,columns=(1,2,3,4,5),show="headings",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=customer_table.xview)
    scroll_y.config(command=customer_table.yview)
    customer_table.heading(1,text="Arrival Date")
    customer_table.heading(2,text="Departure Date")
    customer_table.heading(3,text="Advance Payment")
    customer_table.heading(4,text="Hall no")
    customer_table.heading(5,text="Facilities_var")
    customer_table.column(1,width=150)
    customer_table.column(2,width=150)
    customer_table.column(3,width=150)
    customer_table.column(4,width=150)
    customer_table.column(5,width=150)
    customer_table.pack(fill=BOTH,expand=1)

    customer_table.pack()
    fetch_hall_booking_data()

def Window6():
  
    def file_print():
            app = QApplication(sys.argv) 
            # creating a QPrintDialog
            dlg = QPrintDialog()

            # if executed
            if dlg.exec_():

                # print the text
                editor.print_(dlg.printer())


    def reset():
        x=random.randint(1000,9999)
        bill_no.set(str(x))
        bill_entry.insert(0,bill_no)
        textReceipt.delete(1.0,END)
        e_samosa.set('0')
        e_pizza.set('0')
        e_Tortilla_Wrap.set('0')
        e_Burger.set('0')
        e_Pasta.set('0')
        e_Fries.set('0')
        e_Veg_bites.set('0')
        e_Garlic_bread.set('0')
        e_Veg_Roll.set('0')

        e_lassi.set('0')
        e_coffee.set('0')
        e_faluda.set('0')
        e_roohafza.set('0')
        e_shikanji.set('0')
        e_jaljeera.set('0')
        e_masalatea.set('0')
        e_badammilk.set('0')
        e_coldrinks.set('0')

        e_kitkat.set('0')
        e_oreo.set('0')
        e_apple.set('0')
        e_vanilla.set('0')
        e_banana.set('0')
        e_brownie.set('0')
        e_pineapple.set('0')
        e_chocolate.set('0')
        e_blackforest.set('0')

        textpizza.config(state=DISABLED)
        textsamosa.config(state=DISABLED)
        textTortilla_Wrap.config(state=DISABLED)
        textBurger.config(state=DISABLED)
        textPasta.config(state=DISABLED)
        textGarlic_bread.config(state=DISABLED)
        textVeg_Roll.config(state=DISABLED)
        textVeg_bites.config(state=DISABLED)
        textFries.config(state=DISABLED)

        textlassi.config(state=DISABLED)
        textcoffee.config(state=DISABLED)
        textjaljeera.config(state=DISABLED)
        textroohafza.config(state=DISABLED)
        textshikanji.config(state=DISABLED)
        textbadammilk.config(state=DISABLED)
        textmasalatea.config(state=DISABLED)
        textfaluda.config(state=DISABLED)
        textcolddrinks.config(state=DISABLED)

        textoreo.config(state=DISABLED)
        textapple.config(state=DISABLED)
        textkitkat.config(state=DISABLED)
        textvanilla.config(state=DISABLED)
        textbanana.config(state=DISABLED)
        textbrownie.config(state=DISABLED)
        textpineapple.config(state=DISABLED)
        textchocolate.config(state=DISABLED)
        textblackforest.config(state=DISABLED)

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var12.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var12.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)
        var23.set(0)
        var24.set(0)
        var25.set(0)
        var26.set(0)
        var27.set(0)

        costofdrinksvar.set('')
        costofsnacksvar.set('')
        costofcakesvar.set('')
        subtotalvar.set('')
        servicetaxvar.set('')
        totalcostvar.set('')
        c_name.set('')
        phone.set('')
        bill_no.set('')
        # bill_no=StringVar()
        # x=random.randint(1000,9999)
        # bill_no.set(str(x))




    def save():
        if textReceipt.get(1.0,END)=='\n':
            pass
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
            if url==None:
                pass
            else:

                bill_data=textReceipt.get(1.0,END)
                url.write(bill_data)
                url.close()
                messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

    def receipt():
        global date
        if costofsnacksvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
            textReceipt.delete(1.0,END)
            # x=random.randint(100,10000)
            # billnumber='BILL'+str(x)
            date=time.strftime('%d/%m/%Y')
            # textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
            textReceipt.insert(END,"\tWELCOME TO RESTAURANT\n\tPhone-No.739275410")
            textReceipt.insert(END,f"\n\tDate.:"+date+'\t')
            textReceipt.insert(END,f"\n\nBill no. : {bill_no.get()}")
            textReceipt.insert(END,f"\nCustomer Name : {c_name.get()}")
            textReceipt.insert(END,f"\nPhone No. : {phone.get()}")
            textReceipt.insert(END,'\n''************************************************************\n')
            textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
            textReceipt.insert(END,'************************************************************\n')
            if e_pizza.get()!='0':
                textReceipt.insert(END,f'pizza\t\t\t{int(e_pizza.get())*10}\n\n')

            if e_samosa.get()!='0':
                textReceipt.insert(END,f'samosa\t\t\t{int(e_samosa.get())*60}\n\n')

            if e_Burger.get()!='0':
                textReceipt.insert(END,f'Burger\t\t\t{int(e_Burger.get())*100}\n\n')

            if e_Fries.get() != '0':
                textReceipt.insert(END, f'Fries:\t\t\t{int(e_Fries.get()) * 30}\n\n')

            if e_Tortilla_Wrap.get() != '0':
                textReceipt.insert(END, f'Tortilla_Wrap:\t\t\t{int(e_Tortilla_Wrap.get()) * 50}\n\n')

            if e_Garlic_bread.get() != '0':
                textReceipt.insert(END, f'Garlic_bread:\t\t\t{int(e_Garlic_bread.get()) * 100}\n\n')

            if e_Pasta.get() != '0':
                textReceipt.insert(END, f'Pasta:\t\t\t{int(e_Pasta.get()) * 40}\n\n')

            if e_Veg_Roll.get() != '0':
                textReceipt.insert(END, f'Veg_Roll:\t\t\t{int(e_Veg_Roll.get()) * 120}\n\n')

            if e_Veg_bites.get() != '0':
                textReceipt.insert(END, f'Veg_bites:\t\t\t{int(e_Veg_bites.get()) * 120}\n\n')

            if e_lassi.get() != '0':
                textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

            if e_coffee.get() != '0':
                textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

            if e_faluda.get() != '0':
                textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n\n')

            if e_shikanji.get() != '0':
                textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 30}\n\n')

            if e_jaljeera.get() != '0':
                textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 40}\n\n')

            if e_roohafza.get() != '0':
                textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 60}\n\n')

            if e_masalatea.get() != '0':
                textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_masalatea.get()) * 20}\n\n')

            if e_badammilk.get() != '0':
                textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_badammilk.get()) * 50}\n\n')

            if e_coldrinks.get() != '0':
                textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n\n')

            if e_oreo.get() != '0':
                textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 400}\n\n')

            if e_apple.get() != '0':
                textReceipt.insert(END, f'Apple:\t\t\t{int(e_apple.get()) * 300}\n\n')

            if e_kitkat.get() != '0':
                textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 500}\n\n')

            if e_banana.get() != '0':
                textReceipt.insert(END, f'Banana:\t\t\t{int(e_banana.get()) * 450}\n\n')

            if e_brownie.get() != '0':
                textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 800}\n\n')

            if e_pineapple.get() != '0':
                textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_pineapple.get()) * 620}\n\n')

            if e_chocolate.get() != '0':
                textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 700}\n\n')

            if e_blackforest.get() != '0':
                textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

            if e_vanilla.get() != '0':
                textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 550}\n\n')

            textReceipt.insert(END,'************************************************************\n')
            if costofsnacksvar.get()!='0 Rs':
                textReceipt.insert(END,f'Cost Of snacks\t\t\t{priceofsnacks}Rs\n\n')
            if costofdrinksvar.get() != '0 Rs':
                textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
            if costofcakesvar.get() != '0 Rs':
                textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

            textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
            textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
            textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
            textReceipt.insert(END,'***************************************************************\n')

        else:
            messagebox.showerror('Error','No Item Is selected')



    def totalcost():
        

            global priceofsnacks,priceofDrinks,priceofCakes,subtotalofItems
            if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
                var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
                var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var12.get() != 0 or var15.get() != 0 or \
                var16.get() != 0 or var17.get() != 0 or var12.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
                var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
                var26.get() != 0 or var27.get() != 0:

                item1=int(e_pizza.get())
                item2=int(e_samosa.get())
                item3=int(e_Burger.get())
                item4 = int(e_Tortilla_Wrap.get())
                item5 = int(e_Pasta.get())
                item6 = int(e_Fries.get())
                item7 = int(e_Veg_bites.get())
                item8 = int(e_Garlic_bread.get())
                item9 = int(e_Veg_Roll.get())

                item10 = int(e_lassi.get())
                item11 = int(e_coffee.get())
                item12 = int(e_faluda.get())
                item13 = int(e_shikanji.get())
                item12 = int(e_jaljeera.get())
                item15 = int(e_roohafza.get())
                item16 = int(e_masalatea.get())
                item17 = int(e_badammilk.get())
                item12 = int(e_coldrinks.get())

                item19 = int(e_oreo.get())
                item20 = int(e_apple.get())
                item21 = int(e_kitkat.get())
                item22 = int(e_vanilla.get())
                item23 = int(e_banana.get())
                item24 = int(e_brownie.get())
                item25 = int(e_pineapple.get())
                item26 = int(e_chocolate.get())
                item27 = int(e_blackforest.get())

                priceofsnacks=(item1*10)+(item2*60)+(item3*100)+(item4*50)+ (item5*40) + (item6 * 30) + (item7 * 120) \
                            + (item8 * 100) + (item9 * 120)

                priceofDrinks=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item12 * 40) + (item15 * 60) \
                            + (item16 * 20) + (item17 * 50) + (item12 * 80)

                priceofCakes=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                            + (item25 * 620) + (item26 * 700) + (item27 * 550)

                costofsnacksvar.set(str(priceofsnacks)+ ' Rs')
                costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
                costofcakesvar.set(str(priceofCakes)+ ' Rs')

                subtotalofItems=priceofsnacks+priceofDrinks+priceofCakes
                subtotalvar.set(str(subtotalofItems)+' Rs')

                servicetaxvar.set('50 Rs')

                tottalcost=subtotalofItems+50
                totalcostvar.set(str(tottalcost)+' Rs')

            else:
                messagebox.showerror('Error','No Item Is selected')
            if c_name.get()=="" or phone.get()=="":
                messagebox.showerror("Error","Enter customer name and phone number ",parent=root2)
            else:
                conn=pymysql.connect(host="localhost",user="root",password="",database="project")
                cur=conn.cursor()
                cur.execute("insert into restaurant (c_name,phone,bill_no,totalcost)values(%s,%s,%s,%s)",
                                                                                    (c_name.get(),
                                                                                    phone.get(),
                                                                                    bill_no.get(),
                                                                                    totalcostvar.get()
                                                                                    ))
                conn.commit()
                conn.close()




    def pizza():
        if var1.get()==1:
            textpizza.config(state=NORMAL)
            textpizza.delete(0,END)
            textpizza.focus()
        else:
            textpizza.config(state=DISABLED)
            e_pizza.set('0')

    def samosa():
        if var2.get()==1:
            textsamosa.config(state=NORMAL)
            textsamosa.delete(0,END)
            textsamosa.focus()

        else:
            textsamosa.config(state=DISABLED)
            e_samosa.set('0')

    def Burger():
        if var3.get()==1:
            textBurger.config(state=NORMAL)
            textBurger.delete(0,END)
            textBurger.focus()

        else:
            textBurger.config(state=DISABLED)
            e_Burger.set('0')

    def Tortilla_Wrap():
        if var4.get() == 1:
            textTortilla_Wrap.config(state=NORMAL)
            textTortilla_Wrap.focus()
            textTortilla_Wrap.delete(0, END)
        elif var4.get() == 0:
            textTortilla_Wrap.config(state=DISABLED)
            e_Tortilla_Wrap.set('0')


    def Pasta():
        if var5.get() == 1:
            textPasta.config(state=NORMAL)
            textPasta.focus()
            textPasta.delete(0, END)
        elif var5.get() == 0:
            textPasta.config(state=DISABLED)
            e_Pasta.set('0')


    def Fries():
        if var6.get() == 1:
            textFries.config(state=NORMAL)
            textFries.focus()
            textFries.delete(0, END)
        elif var6.get() == 0:
            textFries.config(state=DISABLED)
            e_Fries.set('0')


    def Veg_bites():
        if var7.get() == 1:
            textVeg_bites.config(state=NORMAL)
            textVeg_bites.focus()
            textVeg_bites.delete(0, END)
        elif var7.get() == 0:
            textVeg_bites.config(state=DISABLED)
            e_Veg_bites.set('0')


    def Garlic_bread():
        if var8.get() == 1:
            textGarlic_bread.config(state=NORMAL)
            textGarlic_bread.focus()
            textGarlic_bread.delete(0, END)
        elif var8.get() == 0:
            textGarlic_bread.config(state=DISABLED)
            e_Garlic_bread.set('0')


    def Veg_Roll():
        if var9.get() == 1:
            textVeg_Roll.config(state=NORMAL)
            textVeg_Roll.focus()
            textVeg_Roll.delete(0, END)
        elif var9.get() == 0:
            textVeg_Roll.config(state=DISABLED)
            e_Veg_Roll.set('0')


    def lassi():
        if var10.get() == 1:
            textlassi.config(state=NORMAL)
            textlassi.focus()
            textlassi.delete(0, END)
        elif var10.get() == 0:
            textlassi.config(state=DISABLED)
            e_lassi.set('0')


    def coffee():
        if var11.get() == 1:
            textcoffee.config(state=NORMAL)
            textcoffee.focus()
            textcoffee.delete(0, END)
        elif var11.get() == 0:
            textcoffee.config(state=DISABLED)
            e_coffee.set('0')


    def faluda():
        if var12.get() == 1:
            textfaluda.config(state=NORMAL)
            textfaluda.focus()
            textfaluda.delete(0, END)
        elif var12.get() == 0:
            textfaluda.config(state=DISABLED)
            e_faluda.set('0')


    def shikanji():
        if var13.get() == 1:
            textshikanji.config(state=NORMAL)
            textshikanji.focus()
            textshikanji.delete(0, END)
        elif var13.get() == 0:
            textshikanji.config(state=DISABLED)
            e_shikanji.set('0')


    def jaljeera():
        if var12.get() == 1:
            textjaljeera.config(state=NORMAL)
            textjaljeera.focus()
            textjaljeera.delete(0, END)
        elif var12.get() == 0:
            textjaljeera.config(state=DISABLED)
            e_jaljeera.set('0')


    def roohafza():
        if var15.get() == 1:
            textroohafza.config(state=NORMAL)
            textroohafza.focus()
            textroohafza.delete(0, END)
        elif var15.get() == 0:
            textroohafza.config(state=DISABLED)
            e_roohafza.set('0')


    def masalatea():
        if var16.get() == 1:
            textmasalatea.config(state=NORMAL)
            textmasalatea.focus()
            textmasalatea.delete(0, END)
        elif var16.get() == 0:
            textmasalatea.config(state=DISABLED)
            e_masalatea.set('0')


    def badammilk():
        if var17.get() == 1:
            textbadammilk.config(state=NORMAL)
            textbadammilk.focus()
            textbadammilk.delete(0, END)
        elif var17.get() == 0:
            textbadammilk.config(state=DISABLED)
            e_badammilk.set('0')


    def colddrinks():
        if var12.get() == 1:
            textcolddrinks.config(state=NORMAL)
            textcolddrinks.focus()
            textcolddrinks.delete(0, END)
        elif var12.get() == 0:
            textcolddrinks.config(state=DISABLED)
            e_coldrinks.set('0')


    def oreo():
        if var19.get() == 1:
            textoreo.config(state=NORMAL)
            textoreo.focus()
            textoreo.delete(0, END)
        elif var19.get() == 0:
            textoreo.config(state=DISABLED)
            e_oreo.set('0')


    def apple():
        if var20.get() == 1:
            textapple.config(state=NORMAL)
            textapple.focus()
            textapple.delete(0, END)
        elif var20.get() == 0:
            textapple.config(state=DISABLED)
            e_apple.set('0')


    def kitkat():
        if var21.get() == 1:
            textkitkat.config(state=NORMAL)
            textkitkat.focus()
            textkitkat.delete(0, END)
        elif var21.get() == 0:
            textkitkat.config(state=DISABLED)
            e_kitkat.set('0')


    def vanilla():
        if var22.get() == 1:
            textvanilla.config(state=NORMAL)
            textvanilla.focus()
            textvanilla.delete(0, END)
        elif var22.get() == 0:
            textvanilla.config(state=DISABLED)
            e_vanilla.set('0')


    def banana():
        if var23.get() == 1:
            textbanana.config(state=NORMAL)
            textbanana.focus()
            textbanana.delete(0, END)
        elif var23.get() == 0:
            textbanana.config(state=DISABLED)
            e_banana.set('0')


    def brownie():
        if var24.get() == 1:
            textbrownie.config(state=NORMAL)
            textbrownie.focus()
            textbrownie.delete(0, END)
        elif var24.get() == 0:
            textbrownie.config(state=DISABLED)
            e_brownie.set('0')


    def pineapple():
        if var25.get() == 1:
            textpineapple.config(state=NORMAL)
            textpineapple.focus()
            textpineapple.delete(0, END)
        elif var25.get() == 0:
            textpineapple.config(state=DISABLED)
            e_pineapple.set('0')


    def chocolate():
        if var26.get() == 1:
            textchocolate.config(state=NORMAL)
            textchocolate.focus()
            textchocolate.delete(0, END)
        elif var26.get() == 0:
            textchocolate.config(state=DISABLED)
            e_chocolate.set('0')


    def blackforest():
        if var27.get() == 1:
            textblackforest.config(state=NORMAL)
            textblackforest.focus()
            textblackforest.delete(0, END)
        elif var27.get() == 0:
            textblackforest.config(state=DISABLED)
            e_blackforest.set('0')


    #Variables


    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var12 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var12 = IntVar()
    var19 = IntVar()
    var20 = IntVar()
    var21 = IntVar()
    var22 = IntVar()
    var23 = IntVar()
    var24 = IntVar()
    var25 = IntVar()
    var26 = IntVar()
    var27 = IntVar()

    e_pizza=StringVar()
    e_samosa=StringVar()
    e_Tortilla_Wrap = StringVar()
    e_Fries = StringVar()
    e_Burger = StringVar()
    e_Veg_bites = StringVar()
    e_Pasta = StringVar()
    e_Veg_Roll = StringVar()
    e_Garlic_bread = StringVar()

    e_lassi=StringVar()
    e_coffee = StringVar()
    e_faluda = StringVar()
    e_shikanji = StringVar()
    e_roohafza = StringVar()
    e_jaljeera = StringVar()
    e_masalatea = StringVar()
    e_badammilk = StringVar()
    e_coldrinks = StringVar()

    e_oreo=StringVar()
    e_kitkat = StringVar()
    e_vanilla = StringVar()
    e_apple = StringVar()
    e_blackforest = StringVar()
    e_banana = StringVar()
    e_brownie = StringVar()
    e_pineapple = StringVar()
    e_chocolate = StringVar()

    costofsnacksvar=StringVar()
    costofdrinksvar=StringVar()
    costofcakesvar=StringVar()
    subtotalvar=StringVar()
    servicetaxvar=StringVar()
    totalcostvar=StringVar()

    e_pizza.set('0')
    e_samosa.set('0')
    e_Tortilla_Wrap.set('0')
    e_Burger.set('0')
    e_Pasta.set('0')
    e_Fries.set('0')
    e_Veg_bites.set('0')
    e_Veg_Roll.set('0')
    e_Garlic_bread.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_kitkat.set('0')
    e_banana.set('0')
    e_pineapple.set('0')
    e_apple.set('0')
    e_chocolate.set('0')
    e_oreo.set('0')
    e_blackforest.set('0')
    e_brownie.set('0')
    e_vanilla.set('0')
    c_name=StringVar()
    bill_no=StringVar()
    x=random.randint(1000,9999)
    bill_no.set(str(x))
    phone=StringVar()

    root2= Toplevel()

    root2.geometry('1920x960+0+0')
    root.config(bg='firebrick4')
    root2.title('Restaurant Management System ')


    topFrame=Frame(root2,bd=10,bg='firebrick4',relief=RIDGE)
    topFrame.place(x=1,y=1)

    detailsFrame=Frame(root2,bg='firebrick4',bd=10,relief=RIDGE,width=1275,height=60)
    detailsFrame.place(x=1,y=75)

    cust_name=Label(detailsFrame,text="Customer Name:-",font=('arial',14),bg='firebrick4',fg='white').place(x=1,y=1)
    cust_entry=Entry(detailsFrame,borderwidth=4,width=30,textvariable=c_name).place(x=170,y=5)
            
    contact_name=Label(detailsFrame,text="Contact No:-",font=('arial',14),bg='firebrick4',fg='white').place(x=400,y=1)      
    contact_entry=Entry(detailsFrame,borderwidth=4,width=30,textvariable=phone).place(x=530,y=5)
            
    bill_name=Label(detailsFrame,text="Bill.No:-",font=('arial',14),bg='firebrick4',fg='white').place(x=750,y=1)
    bill_entry=Entry(detailsFrame,borderwidth=4,width=30,textvariable=bill_no).place(x=840,y=5)

    labelTitle=Label(topFrame,text='Restaurant Management System',bg='firebrick4',font=('arial',30,'bold'),fg='white',width=52)
    labelTitle.grid(row=0,column=0)


    #frames

    menuFrame=Frame(root2,bg='firebrick4',bd=10,relief=RIDGE)
    menuFrame.place(x=1,y=135)

    costFrame=Frame(menuFrame,bg='firebrick4',relief=RIDGE,pady=10)
    costFrame.pack(side=BOTTOM)

    snacksFrame=LabelFrame(menuFrame,text='snacks',font=('arial',19,'bold'),bg='firebrick4',bd=10,relief=RIDGE,fg='black',)
    snacksFrame.pack(side=LEFT)

    drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bg='firebrick4',bd=10,relief=RIDGE,fg='black')
    drinksFrame.pack(side=LEFT)

    cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bg='firebrick4',bd=10,relief=RIDGE,fg='black')
    cakesFrame.pack(side=LEFT)

    rightFrame=Frame(root2,bd=10,bg='firebrick4',relief=RIDGE)
    rightFrame.place(x=820,y=135)

    # calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
    # calculatorFrame.pack()

    recieptFrame=Frame(rightFrame,bg='firebrick4',bd=4,relief=RIDGE,height=500)
    recieptFrame.pack()

    buttonFrame=Frame(rightFrame,bg='firebrick4',bd=3,relief=RIDGE)
    buttonFrame.pack()

    ##snacks

    pizza=Checkbutton(snacksFrame,text='pizza                    ₹10',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var1
                    ,command=pizza)
    pizza.grid(row=0,column=0,sticky=W)

    samosa=Checkbutton(snacksFrame,text='samosa                ₹60',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var2
                    ,command=samosa)
    samosa.grid(row=1,column=0,sticky=W)

    Burger=Checkbutton(snacksFrame,text='Burger                 ₹100',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var3
                    ,command=Burger)
    Burger.grid(row=2,column=0,sticky=W)

    Tortilla_Wrap=Checkbutton(snacksFrame,text='Tortilla_Wrap      ₹50',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var4
                    ,command=Tortilla_Wrap)
    Tortilla_Wrap.grid(row=3,column=0,sticky=W)

    Pasta=Checkbutton(snacksFrame,text='Pasta                   ₹40',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var5
                    ,command=Pasta)
    Pasta.grid(row=4,column=0,sticky=W)

    Fries=Checkbutton(snacksFrame,text='Fries                   ₹30',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var6
                    ,command=Fries)
    Fries.grid(row=5,column=0,sticky=W)

    Veg_bites=Checkbutton(snacksFrame,text='Veg_bites           ₹120',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var7,
                    command=Veg_bites)
    Veg_bites.grid(row=6,column=0,sticky=W)
    0
    Garlic_bread=Checkbutton(snacksFrame,text='Garlic_bread        ₹10',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var8
                    ,command=Garlic_bread)
    Garlic_bread.grid(row=7,column=0,sticky=W)

    Veg_Roll=Checkbutton(snacksFrame,text='Veg_Roll            ₹120',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var9
                        ,command=Veg_Roll)
    Veg_Roll.grid(row=8,column=0,sticky=W)

    #Entry Fields for snacks Items

    textpizza=Entry(snacksFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pizza)
    textpizza.grid(row=0,column=1)

    textsamosa=Entry(snacksFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_samosa)
    textsamosa.grid(row=1,column=1)

    textBurger=Entry(snacksFrame,font=('arial',12,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Burger)
    textBurger.grid(row=2,column=1)

    textTortilla_Wrap = Entry(snacksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Tortilla_Wrap)
    textTortilla_Wrap.grid(row=3, column=1)

    textPasta = Entry(snacksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Pasta)
    textPasta.grid(row=4, column=1)

    textFries = Entry(snacksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Fries)
    textFries.grid(row=5, column=1)

    textVeg_bites = Entry(snacksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Veg_bites)
    textVeg_bites.grid(row=6, column=1)

    textGarlic_bread = Entry(snacksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Garlic_bread)
    textGarlic_bread.grid(row=7, column=1)

    textVeg_Roll = Entry(snacksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Veg_Roll)
    textVeg_Roll.grid(row=8, column=1)

    #Drinks

    lassi=Checkbutton(drinksFrame,text='Lassi                ₹50',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var10
                    ,command=lassi)
    lassi.grid(row=0,column=0,sticky=W)

    coffee=Checkbutton(drinksFrame,text='Coffee              ₹40',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var11
                    ,command=coffee)
    coffee.grid(row=1,column=0,sticky=W)

    faluda=Checkbutton(drinksFrame,text='Faluda             ₹80',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var12
                    ,command=faluda)
    faluda.grid(row=2,column=0,sticky=W)

    shikanji=Checkbutton(drinksFrame,text='Shikanji           ₹30',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var13
                        ,command=shikanji)
    shikanji.grid(row=3,column=0,sticky=W)

    jaljeera=Checkbutton(drinksFrame,text='Jaljeera            ₹40',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var12
                        ,command=jaljeera)
    jaljeera.grid(row=4,column=0,sticky=W)

    roohafza=Checkbutton(drinksFrame,text='Roohafza        ₹60',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var15
                        ,command=roohafza)
    roohafza.grid(row=5,column=0,sticky=W)

    masalatea=Checkbutton(drinksFrame,text='Masala Tea     ₹20',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var16
                        ,command=masalatea)
    masalatea.grid(row=6,column=0,sticky=W)

    badammilk=Checkbutton(drinksFrame,text='Badam Milk    ₹50',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var17
                        ,command=badammilk)
    badammilk.grid(row=7,column=0,sticky=W)

    colddrinks=Checkbutton(drinksFrame,text='Cold Drinks   ₹80',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var12
                        ,command=colddrinks)
    colddrinks.grid(row=8,column=0,sticky=W)

    #entry fields for drink items

    textlassi = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
    textlassi.grid(row=0, column=1)

    textcoffee = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
    textcoffee.grid(row=1, column=1)

    textfaluda = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
    textfaluda.grid(row=2, column=1)

    textshikanji = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shikanji)
    textshikanji.grid(row=3, column=1)

    textjaljeera = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_jaljeera)
    textjaljeera.grid(row=4, column=1)

    textroohafza = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roohafza)
    textroohafza.grid(row=5, column=1)

    textmasalatea = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_masalatea)
    textmasalatea.grid(row=6, column=1)

    textbadammilk = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_badammilk)
    textbadammilk.grid(row=7, column=1)

    textcolddrinks = Entry(drinksFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coldrinks)
    textcolddrinks.grid(row=8, column=1)

    #Cakes

    oreocake=Checkbutton(cakesFrame,text='Oreo                 ₹400',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var19
                        ,command=oreo)
    oreocake.grid(row=0,column=0,sticky=W)

    applecake=Checkbutton(cakesFrame,text='Apple               ₹300',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var20
                        ,command=apple)
    applecake.grid(row=1,column=0,sticky=W)

    kitkatcake=Checkbutton(cakesFrame,text='Kitkat               ₹500',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var21
                        ,command=kitkat)
    kitkatcake.grid(row=2,column=0,sticky=W)

    vanillacake=Checkbutton(cakesFrame,text='Vanilla             ₹550',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var22
                            ,command=vanilla)
    vanillacake.grid(row=3,column=0,sticky=W)

    bananacake=Checkbutton(cakesFrame,text='Banana           ₹450',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var23
                        ,command=banana)
    bananacake.grid(row=4,column=0,sticky=W)

    browniecake=Checkbutton(cakesFrame,text='Brownie          ₹800',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var24
                            ,command=brownie)
    browniecake.grid(row=5,column=0,sticky=W)

    pineapplecake=Checkbutton(cakesFrame,text='Pineapple       ₹620',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var25
                            ,command=pineapple)
    pineapplecake.grid(row=6,column=0,sticky=W)

    chocolatecake=Checkbutton(cakesFrame,text='Chocolate       ₹700',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var26
                            ,command=chocolate)
    chocolatecake.grid(row=7,column=0,sticky=W)

    blackforestcake=Checkbutton(cakesFrame,text='Black Forest   ₹500',font=('arial',12,'bold'),bg='firebrick4',onvalue=1,offvalue=0,variable=var27
                                ,command=blackforest)
    blackforestcake.grid(row=8,column=0,sticky=W)

    #entry fields for cakes

    textoreo = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
    textoreo.grid(row=0, column=1)

    textapple = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
    textapple.grid(row=1, column=1)

    textkitkat = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
    textkitkat.grid(row=2, column=1)

    textvanilla = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
    textvanilla.grid(row=3, column=1)

    textbanana = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_banana)
    textbanana.grid(row=4, column=1)

    textbrownie = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
    textbrownie.grid(row=5, column=1)

    textpineapple = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
    textpineapple.grid(row=6, column=1)

    textchocolate = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
    textchocolate.grid(row=7, column=1)

    textblackforest = Entry(cakesFrame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
    textblackforest.grid(row=8, column=1)

    #costlabels & entry fields

    labelCostofsnacks=Label(costFrame,text='Cost of snacks',font=('arial',14,'bold'),bg='firebrick4',fg='white')
    labelCostofsnacks.grid(row=0,column=0)

    textCostofsnacks=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=costofsnacksvar)
    textCostofsnacks.grid(row=0,column=1,padx=41,pady=3)

    labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',14,'bold'),bg='firebrick4',fg='white')
    labelCostofDrinks.grid(row=1,column=0)

    textCostofDrinks=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=costofdrinksvar)
    textCostofDrinks.grid(row=1,column=1,padx=41,pady=3)

    labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',14,'bold'),bg='firebrick4',fg='white')
    labelCostofCakes.grid(row=2,column=0)

    textCostofCakes=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=costofcakesvar)
    textCostofCakes.grid(row=2,column=1,padx=41,pady=3)

    labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',14,'bold'),bg='firebrick4',fg='white')
    labelSubTotal.grid(row=0,column=2)

    textSubTotal=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=subtotalvar)
    textSubTotal.grid(row=0,column=3,padx=41)

    labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',14,'bold'),bg='firebrick4',fg='white')
    labelServiceTax.grid(row=1,column=2)

    textServiceTax=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=servicetaxvar)
    textServiceTax.grid(row=1,column=3,padx=41)

    labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',14,'bold'),bg='firebrick4',fg='white')
    labelTotalCost.grid(row=2,column=2)

    textTotalCost=Entry(costFrame,font=('arial',14,'bold'),bd=6,width=12,state='readonly',textvariable=totalcostvar)
    textTotalCost.grid(row=2,column=3,padx=41)

    #Buttons

    buttonTotal=Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='black',bg='red4',bd=3,padx=5,
                    command=totalcost)
    buttonTotal.grid(row=0,column=0)

    buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',12,'bold'),fg='black',bg='red4',bd=3,padx=5
                        ,command=receipt)
    buttonReceipt.grid(row=0,column=1)

    buttonSave=Button(buttonFrame,text='Save',font=('arial',12,'bold'),fg='black',bg='red4',bd=3,padx=5
                    ,command=save)
    buttonSave.grid(row=0,column=2)

    buttonReset=Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='black',bg='red4',bd=3,padx=5,
                    command=reset)
    buttonReset.grid(row=0,column=4)

    #textarea for receipt

    textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=46,height=24)
    textReceipt.grid(row=0,column=0)

    root2.mainloop()

leftFrame=Frame(root,bd=8,relief=RIDGE)
leftFrame.place(x=1,y=1)

buttonTotal=Button(leftFrame,text='Add Rooms and halls',font=('times new roman',14,'bold'),command =Window1,pady=5,bd=3,width=30,fg='white',bg='red4').grid(row=1,column=0)
buttonTotal=Button(leftFrame,text='Rooms/halls check availabity and view',font=('times new roman',14,'bold'),pady=5,command=Window2,bd=3,width=30,fg='white',bg='red4').grid(row=3,column=0)
buttonReceipt=Button(leftFrame,text='customer information',font=('times new roman',14,'bold'),command=Window3,bd=3,pady=5,width=30,fg='white',bg='red4').grid(row=4,column=0)
buttonSend=Button(leftFrame,text='Rooms Booking and view',font=('times new roman',14,'bold'),command=Window4,bd=3,pady=5,width=30,fg='white',bg='red4').grid(row=6,column=0)
buttonReset=Button(leftFrame,text='Hall Booking and view',font=('times new roman',14,'bold'),command=Window5,bd=3,pady=5,width=30,fg='white',bg='red4').grid(row=7,column=0)
buttonReset=Button(leftFrame,text='Restaurant',font=('times new roman',14,'bold'),command=Window6,bd=3,pady=5,width=30,fg='white',bg='red4').grid(row=14,column=0)

# topFrame=Frame(root,bd=8,relief=RIDGE,width=900,height=80)
# topFrame.place(x=374,y=1)

# labelTitle=Label(topFrame,text='Rooms/halls check availabity and view',font=('times new roman',30,'bold'))
# labelTitle.place(x=150,y=1)
topFrame=Frame(root,bd=8,relief=RIDGE,width=910,height=80)
topFrame.place(x=360,y=1)

labelTitle=Label(topFrame,text='WELCOME TO SYSTEM',font=('times new roman',30,'bold'))
labelTitle.place(x=150,y=1)
rightFrame=Frame(root,bd=8,relief=RIDGE,width=365,height=150)
rightFrame.place(x=374,y=100)

    # rateFrame=Frame(root,bd=10,relief=RIDGE,width=365,height=150)
    # rateFrame.place(x=903,y=80)

labelTitle=Label(rightFrame,text='           Hall one :-Rs 5500',font=('times new roman',14))
labelTitle.place(x=1,y=10)
labelTitle=Label(rightFrame,text='           Hall two :-Rs 3000',font=('times new roman',14))
labelTitle.place(x=1,y=40)
labelTitle=Label(rightFrame,text='           Hall three :-Rs 6000',font=('times new roman',14))
labelTitle.place(x=1,y=70)
labelTitle=Label(rightFrame,text='           Hall four :-Rs 6000',font=('times new roman',14))
labelTitle.place(x=1,y=100)

taxFrame=Frame(root,bd=10,relief=RIDGE,width=365,height=140)
taxFrame.place(x=903,y=230)

labelTitle=Label(taxFrame,text='           Wedding Facilities :-Rs 5500',font=('times new roman',14))
labelTitle.place(x=1,y=10)
labelTitle=Label(taxFrame,text='           Birthday Facilities :-Rs 3000',font=('times new roman',14))
labelTitle.place(x=1,y=50)
labelTitle=Label(taxFrame,text='           Business meeting :-Rs 6000',font=('times new roman',14))
labelTitle.place(x=1,y=90)

rightFrame=Frame(root,bd=8,relief=RIDGE,width=365,height=150)
rightFrame.place(x=374,y=300)

    # rateFrame=Frame(root,bd=10,relief=RIDGE,width=365,height=150)
    # rateFrame.place(x=903,y=80)

labelTitle=Label(rightFrame,text='           AC Room :-Rs 5500',font=('times new roman',14))
labelTitle.place(x=1,y=10)
labelTitle=Label(rightFrame,text='           Single Room :-Rs 3000',font=('times new roman',14))
labelTitle.place(x=1,y=40)
labelTitle=Label(rightFrame,text='           Duable Room:-Rs 6000',font=('times new roman',14))
labelTitle.place(x=1,y=70)

# img1=Image.open(r"C:\Users\asus\Documents\New folder\hotel3.jpg")
# img1=img1.resize((1550,140),Image.ANTIALIAS)
# photoimg1=ImageTK.PhotoImage(img1)

# lblimg=Label(root,image=photoimg1,bd=4,relief=RIDGE)
# lblimg.place(x=0,y=0,width=230,height=140)
root.mainloop()