from Tkinter import *
root = Tk()
root.geometry("300x300")
root.title("Hello mouse world")
canvas = Canvas(root)
text = "hello"

def sayHello():
   global text
   text = "hello"

def sayGoodbye():
   global text
   text = "goodbye"

def buttonPressed(evt): 
   if evt.widget == canvas:
      canvas.create_text(evt.x, evt.y, text=text)

hellob = Button(root, text="Hello", command=sayHello)
goodbyeb = Button(root, text="Good Bye", command=sayGoodbye)
root.bind("<Button-1>", buttonPressed)

canvas.pack()
hellob.pack()
goodbyeb.pack()

root.mainloop()
