from Tkinter import *

root = Tk()
root.geometry("300x360") # modified a bit to show the slider at bottom
root.title("Hello mouse world")
canvas = Canvas(root)
text = "hello"

size = 10                # variable that will be set by slider

def sayHello():
    global text
    text = "hello"

def sayGoodbye():
    global text
    text = "goodbye"

def updateSize(svalue):  # call back for slider
    global size
    size = int(svalue)

def buttonPressed(evt):  # added font type and size at the end of create_text
    if evt.widget == canvas:
        canvas.create_text(evt.x, evt.y, text=text, font=("Times",size))

hellob = Button(root, text="Hello", command=sayHello)
goodbyeb = Button(root, text="Good Byte", command=sayGoodbye)
root.bind("<Button-1>", buttonPressed)

# new to the slider program
slide = Scale(root, from_=5,to=24,orient=HORIZONTAL,command=updateSize)
slide.set(12)            # set initial size

canvas.pack()
hellob.pack()
goodbyeb.pack()
slide.pack(fill=X)       # fill horizontally

root.mainloop()
