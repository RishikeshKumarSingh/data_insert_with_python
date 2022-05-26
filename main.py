from cgitb import text
from multiprocessing import connection
import tkinter
from tkinter import *
import pymysql

app = Tk()
app.title("by rishi")

connection = pymysql.connect(host="localhost",user="root",password="",database="crud")
cursor= connection.cursor()



nameVar= StringVar()
contactVar= StringVar()

def insertData():
        nameData = nameVar.get()
        contactData = contactVar.get()
        cursor.execute("insert into phonebook (name,contact) value ('%s','%s')" % (nameData,contactData))
        connection.commit()


app.geometry("500x400")
app.config(bg="cyan")

nameLabel = Label(app,text="Name",padx=10,pady=10)
nameLabel.grid(row=0,column=0,padx=10,pady=10)
name = Entry(app,width=50,textvariable=nameVar)
name.grid(row=0,column=1,padx=10,pady=10)

contactLabel = Label(app,text="Contact",padx=10,pady=10)
contactLabel.grid(row=1,column=0,padx=10,pady=10)
contact = Entry(app,width=50,textvariable=contactVar)
contact.grid(row=1,column=1,padx=10,pady=10)


btn = Button(app,text="submit",padx=10,pady=10,command=insertData)
btn.grid(row=2,column=0,columnspan=2)

app.mainloop()