import tkinter as tk
from tkinter import scrolledtext

# call Lagrange windows
def call_Lag_window():
    Lag_windows.mainloop()

Lag_windows = tk.Tk()
Lag_windows.title("Lagrange Solution Creator")
Lag_windows.geometry("750x500")

# --- Select lagrange --- #
frame = tk.Frame(Lag_windows)
frame.pack()
Var1 = tk.IntVar()
mode_Btn1 = tk.Radiobutton(frame, text="Simpson's 1/3 rule", variable=Var1,value=1)
mode_Btn1.pack(padx=5, pady=5,side='left')
mode_Btn2 = tk.Radiobutton(frame, text="Simpson's 3/8 rule", variable=Var1,value=2)
mode_Btn2.pack(padx=5, pady=5,side='left')
mode_Btn3 = tk.Radiobutton(frame, text="boole's rule", variable=Var1,value=3)
mode_Btn3.pack(padx=5, pady=5, side='left')

# exe(Run) button
#expr_str = Entry(window, width=40)
#expr_str.grid(column=0, row=2)
exe_btn = tk.Button(Lag_windows, text="Run", font=("Comic Sans MS",20))
exe_btn.pack(padx=5,pady=20)

# label of substitution
x4_lbl = tk.Label(Lag_windows, text="substitution:",font=("Comic Sans MS",16))
x4_lbl.pack(padx=5, pady=5)

frame2 = tk.Frame(Lag_windows)
frame2.pack()
x4_lbl = tk.Label(frame2, text="x4:",font=("Comic Sans MS",14))
x4_lbl.grid(row=0,column=5)
x3_lbl = tk.Label(frame2, text="x3:",font=("Comic Sans MS",14))
x3_lbl.grid(row=0,column=4)
x2_lbl = tk.Label(frame2, text="x2:",font=("Comic Sans MS",14))
x2_lbl.grid(row=0,column=3)
x1_lbl = tk.Label(frame2, text="x1:",font=("Comic Sans MS",14))
x1_lbl.grid(row=0,column=2)
x0_lbl = tk.Label(frame2, text="x0:",font=("Comic Sans MS",14))
x0_lbl.grid(row=0,column=1)
x_lbl = tk.Label(frame2, text="x:",font=("Comic Sans MS",14))
x_lbl.grid(row=0,column=0)

# Entry box Management
x4_ent = tk.Entry(frame2, width=12)
x4_ent.grid(row=1,column=5)
x3_ent = tk.Entry(frame2, width=12)
x3_ent.grid(row=1,column=4)
x2_ent = tk.Entry(frame2, width=12)
x2_ent.grid(row=1,column=3)
x1_ent = tk.Entry(frame2, width=12)
x1_ent.grid(row=1,column=2)
x0_ent = tk.Entry(frame2, width=12)
x0_ent.grid(row=1,column=1)
x_ent = tk.Entry(frame2, width=12)
x_ent.grid(row=1,column=0)


# output Zone
out_lbl = tk.Label(Lag_windows, text="Solution:",font=("Comic Sans MS",18))
out_lbl.pack(padx=5, pady=5, side='left')
out = scrolledtext.ScrolledText(Lag_windows, height = 20, width = 70)
out.pack(padx=5, pady=5)

call_Lag_window()