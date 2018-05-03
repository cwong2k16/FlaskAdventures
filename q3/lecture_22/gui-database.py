import shelve
from Tkinter import *

data = shelve.open("database")
root = Tk()
root.geometry("400x200")
root.title("Telephone Database")

# make some of the widgets
cmd = IntVar()
lab = Label(root, text="Command:")
k1  = Label(root, text="key/search")
ke  = Entry(root, width=40)
vl  = Label(root, text="value")
ve  = Text(root, width=40, height=5)

def doRadio():
    c = cmd.get() # get the command number
    if c == 1: # search with a given name
        ve.delete("1.0", END)
        if data.has_key(ke.get()):
            ve.insert(END, data[ke.get()])
        else:
            ve.insert(END,"no information for key " + ke.get())
    elif c == 2: # insert a (name, phone number) record
        data[ke.get()] = ve.get("1.0", END)
        ve.delete("1.0", END)
        ve.insert(END, "database has been updated")
    else: # delete the record with given name
        del data[ke.get()]
        ve.delete("1.0", END)
        ve.insert(END, "entry has been deleted")

#finish making widgets
r1=Radiobutton(root,text="Find",variable=cmd,value=1,command=doRadio)
r2=Radiobutton(root,text="Insert",variable=cmd,value=2,command=doRadio)
r3=Radiobutton(root,text="Delete",variable=cmd,value=3,command=doRadio)

# lay out the grid
lab.grid(row=0, column=0)
r1.grid(row=0, column=1)
r2.grid(row=0, column=2)
r3.grid(row=0, column=3)
k1.grid(row=1, column=0) 
ke.grid(row=1, column=1,columnspan=3)
vl.grid(row=2, column=0)
ve.grid(row=2, column=1, columnspan=3)

# loop over main program, save database after user quits
root.mainloop()
data.close()

