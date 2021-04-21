from tkinter import *

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

window = Tk()
window.title("Taylor's Series (Solution mk Programs)")
lbl = Label(window, text="Expression:",font=("Comic Sans MS",22))
lbl.grid(column=0, row=0)
exe_btn = Button(window, text="Run", command=clicked, font=("Comic Sans MS",22))
exe_btn.grid(column=2, row=2)
window.geometry('640x480')
txt = Entry(window, width=10)
txt.grid(column=0, row=2)
window.mainloop()

