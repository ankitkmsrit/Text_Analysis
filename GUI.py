from tkinter import *
from Interest import research
from FinalCode import tarea
import re
def commandenter(l):
    print("CLICKED PROGRAMAICALLY")
    command1()
def command1():
    field=""
    dic = tarea()
    b=tb.get("1.0",END)
    b=b.upper().strip()
    s = ""
    count = 0
    tcount=0
    for i,j in dic.items():   # using regular expression finding faculty working in the research field provided by the user
        if re.match(b,i):
            for faculty in j:
                s = s + faculty + "\n"
                count+=1
        else:
            tcount+=1
    
    
    if(tcount==len(dic)):   #if the research field doesn't exist
        tbout.insert("1.0","Invalid Research Field name\n")
    else:
        if(count!=0):   #if there are atleast one faculty
            tbout.delete("1.0",END)
            tbout.insert("1.0","There are " +str(count)+" faculty who have done research in "+b+" field\n\n")
            tbout.insert("2.0",s)
        else:      #if there are no faculty working in that field
            tbout.delete("1.0",END)
            tbout.insert("2.0","There are no faculty working in " + b+" field\n")
            


def command2():
    tb.delete("1.0",END)
    tbout.delete("1.0",END)
            
root = Tk()
root.title("Compiler Design Project")
w = Label(root, text="Quantitative Text Analysis",bg="black")
w.configure(foreground="white")
w.config(font=('Courier',30,'bold'))
lb1=Label(root,text="Please enter a Research Field",bg="black")
lb1.configure(foreground='white')
lb1.config(font=('Courier',18,'bold'))

tb=Text(root)
btn1=Button(root,text="CLICK",command=command1)
btn1.config(font=('Courier',18,'bold'))
btn2=Button(root,text="CLEAR",command=command2)
btn2.config(font=('Courier',18,'bold'))
tb.bind('<Return>',commandenter)
w.pack()
lb1.pack()
tb.pack()
btn1.pack()
btn2.pack()
lb=Label(root,text="OUTPUT")
tbout=Text(root)
lb.pack()
tbout.pack()
root.mainloop()

