import tkinter as tk
from config import *
import random

root = tk.Tk()
root.geometry(str(display_height)+"x"+str(display_width))

expression = str()

def add_to_str(to_add):
    global expression
    expression=expression + to_add
    print(to_add)
    text_box.config(text=expression)

text_box=tk.Label(root, text=expression ,height=2)
# text_box.grid(row=0,column=0,columnspan=6,rowspan=text_row_span)
text_box.pack()

def find():
    global expression





def get_insult():
    global expression
    expression = str()
    insult_size=len(insults)
    print(insult_size)
    expression=insults[random.randint(0,insult_size-1)]
    print(expression)
    text_box.config(text=expression)
    expression=str()

frame1=tk.Frame(root)
frame1.pack()
okaygay=0
for i in range (9):
    w=i%3
    h=int(i/3)
    # create_button1(text_row_span+h,w,i+1,add_to_str,i+1)
    b = (tk.Button(frame1,text=str(i+1),fg='blue',bg='red',
    command=lambda gga=str(i+1): add_to_str(gga)))
    b.config(height=2,width=5)
    b.grid(row=text_row_span+h,column=(2*w))



b = (tk.Button(frame1,text="0",fg='blue',bg='red',
    command=lambda gga=str(0): add_to_str(gga)))
b.config(height=2,width=5)
b.grid(row=text_row_span+3,column=2)


b = (tk.Button(frame1,text="+",fg='blue',bg='red',
    command=lambda gga="+": add_to_str(gga)))
b.config(height=2,width=5)
b.grid(row=text_row_span+3,column=0)

b = (tk.Button(frame1,text="-",fg='blue',bg='red',
    command=lambda gga="-": add_to_str(gga)))
b.config(height=2,width=5)
b.grid(row=text_row_span+3,column=4)

b = (tk.Button(frame1,text="*",fg='blue',bg='red',
    command=lambda gga="*": add_to_str(gga)))
b.config(height=2,width=5)
b.grid(row=text_row_span+4,column=0)

b = (tk.Button(frame1,text="/",fg='blue',bg='red',
    command=lambda gga="/": add_to_str(gga)))
b.config(height=2,width=5)
b.grid(row=text_row_span+4,column=2)


# create_button(text_row_span+4,2,"=",command=lambda: get_insult())
a=tk.Button(frame1,text="=",fg='blue',bg='black',command=get_insult)
a.config(height=2,width=5)
a.grid(row=text_row_span+4,column=4)




for i in range (3):
    k=i+1
    root.grid_columnconfigure(k,minsize=20)
    root.grid_rowconfigure(k,minsize=20)


print("it is",expression)
root.mainloop()