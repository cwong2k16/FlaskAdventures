import Tkinter 

root = Tkinter.Tk()
root.title("Hello example")
root.geometry("200x100")

w = Tkinter.Label(root, text="Hello, world!")
w.pack()

root.mainloop()
