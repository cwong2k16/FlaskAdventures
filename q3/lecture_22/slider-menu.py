from Tkinter import *

root = Tk()
root.geometry("300x360") # modified a bit to show the slider at bottom
root.title("Hello mouse world")
canvas = Canvas(root)
text = "hello"

size = 10                # variable that will be set by slider
fontname = "Times"       # initial font type

def sayHello():
    global text
    text = "hello"

def sayGoodbye():
    global text
    text = "goodbye"

def updateSize(svalue): # call back for slider
    global size
    size = int(svalue)

def settimes():         # change font type to "Times"
    global fontname
    fontname = "Times"

def sethelvetica():     # change font type to Helvetica
    global fontname
    fontname = "Helvetica"

def buttonPressed(evt): # added font type and size at the end of create_text
    if evt.widget == canvas:
        canvas.create_text(evt.x, evt.y, text=text, font=(fontname,size))

hellob = Button(root, text="Hello", command=sayHello)
goodbyeb = Button(root, text="Good Byte", command=sayGoodbye)
root.bind("<Button-1>", buttonPressed)

# new to the slider program
slide = Scale(root, from_=5,to=24,orient=HORIZONTAL,command=updateSize)
slide.set(12)            # set initial size

# create two new menus 
menubar = Menu(root)
fontMenu = Menu(menubar)
fontMenu.add("command",label="Times",command=settimes)
fontMenu.add("command",label="Helvetica", command=sethelvetica)
menubar.add("cascade",label="Font", menu=fontMenu)

canvas.pack()
hellob.pack()
goodbyeb.pack()
slide.pack(fill=X)       # fill horizontally

root.config(menu=menubar) # the top-level window uses the new menubar

root.mainloop()
