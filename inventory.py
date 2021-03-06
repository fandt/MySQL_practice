from Tkinter import *
import os
import sqlite3
import MySQLdb
from MySQLdb.constants import FIELD_TYPE
import csv
import fileinput
import os
from datetime import datetime

class ClickInvoke:
  def __init__(self, master):
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry(str(width)+"x"+str(height/4))
    self.b1 = Button(root, 
                         text="DONE", fg="red",
                         command=root.quit)
    self.b1.pack(side=LEFT)
    inventorylist = "C:/Users/Rebecca/Desktop/Overland/Ordering Guide old.csv"
    brands = csv.reader(open(inventorylist))
    cdate = str(format(datetime.today(),"%Y-%m-%d"))
    file = "C:/Users/Rebecca/Desktop/Overland/Balance_Report/"+cdate+".csv"
    alphab=[]
    for brand in brands:
        alpha = brand[0][0]
        if alpha not in alphab:
            alphab.append(alpha)
    alphab=alphab[0:2]+sorted(alphab[2:])
    for value in alphab:
        self.b1 = Button(text=value,command=lambda arg=value:self.get_bottles(arg))
        self.b1.pack(side=LEFT)
        self.b1.config(height=height/8, width=width/(8*len(alphab)))
        print len(alphab)
    
      
    
  def write_slogan(self,letter):
    print "This is easy to use!" +str(letter)
    sub.destroy()
    global subw
    subw=Toplevel()
    subw.title("Go ahead")
    msg=Message(subw,text=letter)
    msg.pack()
    button=Button(subw,text="ok", width=10,command=lambda :self.outtie(entry.get(),letter))
    button.pack()
    entry=Entry(subw)
    entry.pack()
    Label(subw,text="count:").pack()


  def outtie(self,entry,letter):
    print entry
    subw.destroy()
    print letter
    conn = MySQLdb.connect(user = 'root',host="127.0.0.1",db = 'bottlesareus',
                       port = 3306)
    c = conn.cursor()
    test=c.execute("select * from brands")
    cdate = str(format(datetime.today(),"%Y-%m-%d"))
    lettero = "'"+letter[0]+"'"
    c.execute("insert into inventory(bottlei, counti, datei, orderi) values(%s,%s,%s,1)",(lettero,entry,cdate))
    print lettero +", "+entry+", "+cdate
    conn.commit()
    conn.close()


  def get_bottles(self,letter):
      inventorylist= "C:/Users/Rebecca/Desktop/Overland/Ordering Guide old.csv"
      brands = csv.reader(open(inventorylist))
      bottles=[]
      for brand in brands:
          alpha = brand[0][0]
          if alpha == letter:
              bottles.append(brand)
      global sub
      sub=Toplevel()
      sub.title("Go ahead")
      for bottle in bottles:
          msg=Message(sub)
          msg.pack()
          button=Button(sub,text=bottle, command=lambda arg=bottle:self.write_slogan(arg))
          button.pack()


root = Tk()
app = ClickInvoke(root)
root.mainloop()

