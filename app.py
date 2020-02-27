import tkinter as tk
from config import *


root = tk.Tk()
root.geometry(str(display_height)+"x"+str(display_width))

expression = str()

def add_to_str(to_add):
    global expression
    expression+=str(to_add)

text_box=tk.Label(root,text=expression,height=2,width=20)
text_box.grid(row=0,column=0,columnspan=3,rowspan=text_row_span)



def create_button1(row,column,text,function,argument):
    b=tk.Button(root,text=text,fg='blue',bg='black',command=function(argument))
    b.config(height=2,width=5)
    b.grid(row=row,column=column)

def create_button(row,column,text):
    b=tk.Button(root,text=text,fg='blue',bg='black')
    b.config(height=2,width=5)
    b.grid(row=row,column=column)


for i in range (9):
    w=i%3
    h=int(i/3)
    create_button1(text_row_span+h,w,i+1,add_to_str,i+1)



create_button(text_row_span+3,1,"0")
create_button(text_row_span+3,0,"+")
create_button(text_row_span+3,2,"-")

create_button(text_row_span+4,0,"*")
create_button(text_row_span+4,1,"/")
create_button(text_row_span+4,2,"=")




for i in range (3):
    k=i+1
    root.grid_columnconfigure(k,minsize=20)
    root.grid_rowconfigure(k,minsize=20)


print(expression)
root.mainloop()