from tkinter import *
from tkinter import scrolledtext
from Taylor_series import Taylor_series_with_subs

# Preload function
def limit_view_set():
    if lm_view.get() == None or lm_view.get() == "":
        print(-1)
        return -1
    else:
        print('else',lm_view.get())
        return int(lm_view.get())

def run_taylor():
    tx_result = Taylor_series_with_subs(expr_str.get(),int(n_str.get()),0,limit_view_set(),x_str.get())
    out.delete('1.0',END)
    out.insert(END,str(tx_result ))

# GUI General config

window = Tk()
window.title("Taylor's Series (Solution mk Programs)")
window.geometry('640x480')

# expression input zone

lbl_e = Label(window, text="Expression:",font=("Comic Sans MS",22))
lbl_e.grid(column=0, row=0)


# N and X input value
lbl_x = Label(window, text="substitution(optional):",font=("Comic Sans MS",20))
lbl_x.grid(column=0,row=5)
label_N = Label(window, text="n:",font=("Comic Sans MS",20))
label_N.grid(column=0,row=3)

x_str = Entry(window, width=10)
n_str = Entry(window, width=10)
x_str.grid(column=0,row=6)
n_str.grid(column=0,row=4)

# limit view zone

lbl_e = Label(window, text="limit view:",font=("Comic Sans MS",18))
lbl_e.grid(column=2, row=0)

lm_view = Entry(window)
lm_view.grid(column=2, row=1)

# exe(Run) button
expr_str = Entry(window, width=40)
expr_str.grid(column=0, row=2)
exe_btn = Button(window, text="Run", font=("Comic Sans MS",22),command=run_taylor)
exe_btn.grid(column=2, row=6)



# output zone
out = scrolledtext.ScrolledText(window, height = 10, width = 55)
out.grid(column=0,row=8)

window.mainloop()

