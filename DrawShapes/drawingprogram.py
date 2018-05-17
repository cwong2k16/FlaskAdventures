from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x500")
root.title("CSE 337 Drawing Program")
canvas = Canvas(root)
v = IntVar()
x = IntVar()
color = "black"
shape = 0
array = []

def buttonPressed(evt):
      global param1
      global param2
      global param3
      global param4
      global width
      print('hello world')
      param1 = e1.get()
      param2 = e2.get()
      param3 = e3.get()
      param4 = e4.get()
      width = e5.get()
      if len(width)==0:
            width=1
      if evt.widget == canvas:  
            if errorHandler() == 1:
                  return
            else:
                  if shape not in (1, 2, 3):
                        messagebox.showinfo("No radio option selected", "No radio button was selected.")
                        return
                  elif(shape == 1):
                        array.append(canvas.create_rectangle(param1, param2, param3, param4, width=width, fill=color, outline=color))
                  elif(shape == 2):
                        array.append(canvas.create_line(param1, param2, param3, param4, width=width, fill=color))
                  else:
                        array.append(canvas.create_oval(param1, param2, param3, param4, width=width, fill=color, outline=color))

def deleteShape():
      if(len(array)>0):
            canvas.delete(array.pop())

def doShape():
      global shape
      shape = v.get()

def doColor():
      global color
      if(x.get() == 4):
            color = "red"
      elif(x.get() ==5):
            color = "green"
      else:
            color = "blue"

def errorHandler():
      x = 0
      if errorHandlerHelper(param1, "width"):
            messagebox.showinfo("Invalid Parameter", "Parameter 1 is invalid")
            x = 1
      if errorHandlerHelper(param2, "height"):
            messagebox.showinfo("Invalid Parameter", "Parameter 2 is invalid")
            x = 1
      if errorHandlerHelper(param3, "width"):
            messagebox.showinfo("Invalid Parameter", "Parameter 3 is invalid")
            x = 1
      if errorHandlerHelper(param4, "height"):
            messagebox.showinfo("Invalid Parameter", "Parameter 4 is invalid")
            x = 1
      if float(width) < 0:
            messagebox.showinfo("Invalid width size")
            x = 1
      return x

def errorHandlerHelper(param, widthOrHeight):
      if widthOrHeight == "width":
            return is_number(param) == False or len(param) == 0 or float(param) < 0 or float(param) > canvas.winfo_width()
      else:
            return is_number(param) == False or len(param) == 0 or float(param) < 0 or float(param) > canvas.winfo_height()

def is_number(number):
      try:
            float(number)
      except ValueError:
            return False
      return True

label1 = Label(root, text="Param 1")
label2 = Label(root, text="Param 2")
label3 = Label(root, text="Param 3")
label4 = Label(root, text="Param 4")
label5 = Label(root, text="Width")

e1 = Entry(root, width=32)
e2 = Entry(root, width=32)
e3 = Entry(root, width=32)
e4 = Entry(root, width=32)
e5 = Entry(root, width=32)

radio1 = Radiobutton(root,text="Rectangle",variable=v,value=1, command=doShape)
radio2 = Radiobutton(root,text="Line",variable=v,value=2, command=doShape)
radio3 = Radiobutton(root,text="Oval",variable=v,value=3, command=doShape)

radio4 = Radiobutton(root,text="Red",variable=x,value=4, command=doColor)
radio5 = Radiobutton(root,text="Green",variable=x,value=5, command=doColor)
radio6 = Radiobutton(root,text="Blue",variable=x,value=6, command=doColor)

label1.grid(row=25, column=0)
label2.grid(row=26, column=0)
label3.grid(row=27, column=0)
label4.grid(row=28, column=0)
label5.grid(row=29, column=0)

e1.grid(row=25, column=1)
e2.grid(row=26, column=1)
e3.grid(row=27, column=1)
e4.grid(row=28, column=1)
e5.grid(row=29, column=1)

radio1.grid(row=30, column=0)
radio2.grid(row=31, column=0, sticky='w')
radio3.grid(row=32, column=0, sticky='w')

radio4.grid(row=30, column=1, sticky='w')
radio5.grid(row=31, column=1, sticky='w')
radio6.grid(row=32, column=1, sticky='w')

delete = Button(root, text="Delete", command=deleteShape)

delete.grid(row=33, column = 0, sticky='w')

canvas.grid(row=0, rowspan=25, column=0, columnspan=25)

root.bind("<Button-1>", buttonPressed)

root.mainloop()