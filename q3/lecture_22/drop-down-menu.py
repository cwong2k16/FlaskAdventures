from Tkinter import *
root = Tk()
root.geometry("300x330")
root.title("Hello mouse world")
canvas = Canvas(root)
text = "hello"

size = 12               # a fixed size

fontname="Times"        # initial font type

def sayHello():
    global text
    text = "hello"

def sayGoodbye():
    global text
    text = "goodbye"

def buttonPressed(evt): # font type is now taking from variable: fontname
    if evt.widget == canvas:
        canvas.create_text(evt.x, evt.y, text=text, font=(fontname, size))

def settimes():         # change font type to "Times"
    global fontname
    fontname = "Times"

def sethelvetica():     # change font type to Helvetica
    global fontname
    fontname = "Helvetica"

hellob = Button(root, text="Hello", command=sayHello)
goodbyeb = Button(root, text="Good Byte", command=sayGoodbye)
root.bind("<Button-1>", buttonPressed)

# create two new menus 
menubar = Menu(root)
fontMenu = Menu(menubar)
fontMenu.add("command",label="Times",command=settimes)
fontMenu.add("command",label="Helvetica", command=sethelvetica)
menubar.add("cascade",label="Font", menu=fontMenu)

canvas.pack()
hellob.pack()
goodbyeb.pack()

root.config(menu=menubar) # the top-level window uses the new menubar

root.mainloop()
