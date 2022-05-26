from cgitb import text
from sqlite3 import Cursor, Row
import tkinter
from tkinter import *
from tkinter import font
import pymysql

connection = pymysql.connect(host="localhost",user="root",password="",database="crud")

cursor=connection.cursor()

app = Tk()
app.title("By Rishi")
app.geometry("700x600")
app.config(bg="cyan")

nameVar=StringVar()
contactVar=StringVar()
genderVar=StringVar()
addressVar=StringVar()

def handleForm():
        name= nameVar.get()
        contact=contactVar.get()
        gender=genderVar.get()
        address=addressVar.get()
        cursor.execute("insert into records (name,contact,gender,address) value ('%s','%s','%s','%s')" % (name,contact,gender,address))
        connection.commit()
        resetForm()

def resetForm():
        nameVar.set("")
        contactVar.set("")
        genderVar.set("")
        addressVar.set("")
       

nameLabel = Label(app,text="Admission Form",padx=10,pady=10,bg="cyan",font=("Arial Bold",44,"bold"))
nameLabel.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

nameLabel=Label(app,text="Name",padx=10,pady=10,bg="cyan",font=("Arial",24))
nameLabel.grid(row=1,column=0,padx=10,pady=10)
name=Entry(app,width=25,font=("Arial",26),textvariable=nameVar)
name.grid(row=1,column=1,padx=10,pady=10)

contactLabel=Label(app,text="Contact",padx=10,pady=10,bg="cyan",font=("Arial",24))
contactLabel.grid(row=2,column=0,padx=10,pady=10)
contact=Entry(app,width=25,font=("Arial",26),textvariable=contactVar)
contact.grid(row=2,column=1,padx=10,pady=10)

genderLabel=Label(app,text="Gender",padx=10,pady=10,bg="cyan",font=("Arial",24))
genderLabel.grid(row=3,column=0,padx=10,pady=10)
gender=Entry(app,width=25,font=("Arial",26),textvariable=genderVar)
gender.grid(row=3,column=1,padx=10,pady=10)

addressLabel=Label(app,text="Address",padx=10,pady=10,bg="cyan",font=("Arial",26))
addressLabel.grid(row=4,column=0,padx=10,pady=10)
address=Entry(app,width=25,font=("Arial",26),textvariable=addressVar)
address.grid(row=4,column=1,padx=10,pady=10)

btn=Button(app,text="Reset",padx=10,pady=10,bd=5,bg="red",fg="White",font=("Arial",20),command=resetForm)
btn.grid(row=6,column=0)

btn=Button(app,text="Submit",padx=10,pady=10,bd=5,bg="green",fg="White",font=("Arial",20),command=handleForm)
btn.grid(row=6,column=1)



app.mainloop()


value =input("inter your")
result = {"uppercase":0,"lowercase":0}

for c in value:
        if c.isupper():
                result["uppercase"]+=1
        elif c.islower():
                result["lowercase"]+=1
        else:
                pass

print("Uppercase = %d \n Lowecase = %d" % (result["uppercase"],result["lowercase"]))