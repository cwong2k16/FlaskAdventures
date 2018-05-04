from tkinter import *

width=32

root = Tk()
root.geometry("300x500")
root.title("CSE 337 Drawing Program")
canvas = Canvas(root)

def buttonPressed(evt): 
   if evt.widget == canvas:
      canvas.create_text(evt.x, evt.y, text='hello')

label1 = Label(root, text="Param 1")
label2 = Label(root, text="Param 2")
label3 = Label(root, text="Param 3")
label4 = Label(root, text="Param 4")

e1 = Entry(root, width=width)
e2 = Entry(root, width=width)
e3 = Entry(root, width=width)
e4 = Entry(root, width=width)

radio1 = Radiobutton(root,text="Rectangle",variable=1,value=1)
radio2 = Radiobutton(root,text="Line",variable=1,value=2)
radio3 = Radiobutton(root,text="Oval",variable=1,value=3)

label1.grid(row=25, column=0)
label2.grid(row=26, column=0)
label3.grid(row=27, column=0)
label4.grid(row=28, column=0)

e1.grid(row=25, column=1)
e2.grid(row=26, column=1)
e3.grid(row=27, column=1)
e4.grid(row=28, column=1)

radio1.grid(row=29, column=0)
radio2.grid(row=30, column=0)
radio3.grid(row=31, column=0)

canvas.grid(row=0, rowspan=25, column=0, columnspan=25)

root.mainloop()
