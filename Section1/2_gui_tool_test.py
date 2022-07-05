from tkinter import *

def printHello():
    print('High!')
    print('This is called by method!')

root = Tk()

w = Label(root, text="python Test by Label")
b = Button(root, text="Button", command=printHello)
c = Button(root, text="Quit", command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()
