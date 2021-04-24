from tkinter import *
from tkinter import scrolledtext
import sympy as sym

# custom function for GUI
def Taylor_series_with_subs(func,n_max,n=0,view_lm=-1,subs_v=None):
    # translate string expression to function
    func = sym.sympify(func)

    # check limit view
    if view_lm == -1:
        view_lm = n_max+1

    # recursive from first to the end of 'n'
    x = sym.symbols("x")
    if n >= n_max:
        diff_now = sym.diff(func)
        sol = diff_now.subs(x,0)
        final_level = sol * ((x**n) / sym.factorial(n))
        if n <= view_lm:
            out.insert(END,'diff f' + str(n) + ": " + str(diff_now))
            out.insert(END," -> f(n)(0) * x**n / n! value in this level: " + str(final_level) + " \n")
            out.insert(END,"\n")
        return final_level
    elif n == 0:
        sol = func.subs(x,0)
        this_level = sol * ((x**n) / sym.factorial(n))
        n = n+1
        if n <= view_lm:
            out.insert(END,"no diff " + str(func))
            out.insert(END," -> f(n)(0) * x**n / n! value in this level: " + str(this_level) + " \n")

        if subs_v == None or subs_v == "":
            func = this_level + Taylor_series_with_subs(func, n_max, n, view_lm)
            out.insert(END,"\nFull Form: " + str(func))
            return func
        else:
            func = this_level + Taylor_series_with_subs(func,n_max,n,view_lm)
            out.insert(END,"\nFull Form: " + str(func))
            out.insert(END,"\nsubstituted value = " + str(func.subs(x,subs_v)))
            return func
    else:
        diff_now = sym.diff(func)
        sol = diff_now.subs(x,0)
        n = n+1
        this_level = sol * ((x**n) / sym.factorial(n))
        if n <= view_lm:
            out.insert(END,'diff f' + str(n) + ":" + str(diff_now))
            out.insert(END," -> f(n)(0) * x**n / n! value in this level: " + str(this_level) + " \n")
        return this_level + Taylor_series_with_subs(diff_now,n_max,n,view_lm)

# Preload function
def limit_view_set():
    if lm_view.get() == None or lm_view.get() == "":
        print(-1)
        return -1
    else:
        print('else',lm_view.get())
        return int(lm_view.get())

def run_taylor():
    out.delete('1.0', END)
    out.insert(END, "show Solution:\n")
    Taylor_series_with_subs(expr_str.get(),int(n_str.get()),0,limit_view_set(),x_str.get())

    out.insert(END,"\n\nDone!")

# GUI General config

window = Tk()
window.title("Taylor's Series (Solution mk Programs)")
window.geometry('800x600')

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
out = scrolledtext.ScrolledText(window, height = 20, width = 70)
out.grid(column=0,row=8)

window.mainloop()

