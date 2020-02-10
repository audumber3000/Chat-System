import _tkinter
from functools import partial
import tkinter as tk
import pymongo
from pymongo import MongoClient
from tkinter import *
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


def rev():

 print()
 connection = MongoClient(
     "mongodb+srv://audumber:audumber@cluster0-bj3vd.mongodb.net/test?retryWrites=true&w=majority")

 database = connection['audu']
 collection = database['audu']

 myquery = ({"ID":"101"})

 mydoc = collection.find_one(myquery)
 print("audu")
 label9 = tk.Label(top, text=mydoc, font=("Helvitaka", 10), bg="red").place(x=20, y=250)

 return mydoc




def chat(e2):
     print("hello1")

     msg=e2.get()
     connection = MongoClient(
      "mongodb+srv://audumber:audumber@cluster0-bj3vd.mongodb.net/test?retryWrites=true&w=majority")

     database = connection['audu']
     collection = database['audu']

     myquery = {"ID":"101", "message":msg }
     myquery1={"ID":"101"}

     mydoc1= collection.delete_one(myquery1)
     mydoc = collection.insert_one(myquery)
     print("hello world")


if __name__=="__main__":
 top = tk.Tk()

 top.configure(bg="light sky blue")
 top.geometry("600x450")


 var = tk.StringVar()
 label = tk.Label(top, text="             Chat Line                     " ,bg="royal blue", font=("Helvetica", 35)).place(x = 0, y = 0)
 label7 = tk.Label(top,text="                                                      build by zsploit.co.in                                                                "
                   ,bg="royal blue", font=("Helvetika" ,10)).place(x=0,y=430)
 a=StringVar()
 e2 = tk.Entry(top ,width=50 ,bg="white",textvariable=a,fg="black").place(x=100,y=370)


 k="Sender"
 label1 = tk.Label(top,text=k,font=("Helvitaka" ,20)).place(x=2,y=150)
 label2 = tk.Label(top,text="Reciver",font=("Helvitaka" ,20)).place(x=500,y=150)
 label3=tk.Label(top,text="<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",bg="sky blue",fg="black").place(x=110,y=160)


 label4 = tk.Label(top,text=k,font=("Helvitaka" , 20)).place(x=2 ,y=300)
 label5= tk.Label(top,text="Reciver",font=("Helvitaka",20)).place(x=500,y=300)
 label6=tk.Label(top,text=">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",bg="sky blue",fg="black").place(x=110,y=310)



 img = ImageTk.PhotoImage(Image.open("rsz_1download.png"))
 imglabel = Label(top, image=img).place(x=100 , y=0)





 rev=partial(rev)
 chat=partial(chat,a)
 b1=tk.Button(top,text="Send",command=chat, bg="dark blue").place(x=530,y=365)


 b2=tk.Button(top,text="Get" , command=rev , bg="dark blue").place(x=50,y=200)



 tk.mainloop()











