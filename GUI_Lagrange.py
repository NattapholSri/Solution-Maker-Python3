import tkinter as tk
from tkinter import scrolledtext
import sympy

# call Lagrange windows
def call_Lag_window():
    Lag_windows.mainloop()

def run_lagrange():
    out.delete("1.0",tk.END)
    if Var1.get() == 0:
        out.insert(tk.END,"larange polynomial Mode wasn't selected.\nplease select one.\n")
    else:
        input_num = Var1.get() + 1
        lagrange_polynomial(input_num)

def lagrange_polynomial(max_x):
    m3_dict = {"1": "simpson's 1/3 rule", "2": "simpson's 3/8 rule", "3": "Boole's rule"}
    dx = "(b-a)/"+str(max_x)
    h = sympy.Symbol("h")
    multiple_A = []
    subs_bool = subs_var.get()

    def substitution_var_ask():
        global xs,x0s,x1s,x2s,x3s,x4s
        xs = x_ent.get()
        x0s = x0_ent.get()
        x1s = x1_ent.get()
        x2s = x2_ent.get()
        x3s = x3_ent.get()
        x4s = x4_ent.get()

    def var_chk(mode):
        done = True
        mode = mode + 2
        listvar = [xs,x0s,x1s,x2s,x3s,x4s]
        for var in listvar[:mode]:
            if var == None or var == "":
                done = False
                break
        return done


    # create lagrange form for each xi
    def create_lag(i,n,v_str="x"):
        top = ""
        bottom = ""
        for j in range(n+1):
            if j != i:
                if top != "":
                    top=top+"*"
                top = top + "(" + v_str + "-" + (v_str + str(j) )+ ")"
                if bottom != "":
                    bottom+="*"
                bottom = bottom + "(" + (v_str + str(i)) + "-" + (v_str + str(j))+ ")"

        expr = sympy.sympify(top + "/(" + bottom + ")")
        return expr

    # function to return h value in point
    def h_form_rtn(n):
        if n == 2:
            return h / 3
        elif n == 3:
            return (3 * h) / 8
        elif n == 4:
            return (2 * h) / 45

    # create 'I' expression (Answer)
    def create_inside_expr(Array_a):
        f = sympy.Function('f')
        x0 = sympy.Symbol("x0")
        in_expr = f(x0) * Array_a[0]
        for i in range(max_x):
            str_i = "x" + str(i+1)
            in_expr = in_expr + (f(sympy.Symbol(str_i))*Array_a[i+1])
        return in_expr

    # substitution Value get
    if subs_bool == True:
        substitution_var_ask()
        if not var_chk(max_x):
            out.insert(tk.END,"some substitution values is missing. please check.")
            return

    # Main loop
    if max_x == 2:
        out.insert(tk.END,"run mode: " + str(m3_dict["1"])+ "\n")
        for i in range(max_x+1):
            func_form = create_lag(i,max_x)
            out.insert(tk.END,"\n"+"L" + str(i) + ": " + str(func_form))
            if subs_bool == True:
                x, x0, x1, x2 = sympy.symbols('x x0 x1 x2')
                out.insert(tk.END,"\n"+"substitute value[x,x0,x1,x2]:"+ str(xs)+" "+str(x0s)+" "+str(x1s)+" "+str(x2s))
                func_form = func_form.subs([(x,xs),(x0,x0s),(x1,x1s),(x2,x2s)])
                out.insert(tk.END,"\n"+"substitute result: " + str(func_form))

            if i == 1:
                h_form = 4*h_form_rtn(max_x)
                multiple_A.append(h_form)
                out.insert(tk.END,"\n"+"A1 =" + str(h_form))
            else:
                h_form = h_form_rtn(max_x)
                multiple_A.append(h_form)
                out.insert(tk.END,"\n"+"A"+str(i)+" = " + str(h_form))
    elif max_x == 3:
        out.insert(tk.END,"run mode: "+ str(m3_dict["2"]) + "\n")
        for i in range(max_x+1):
            func_form = create_lag(i, max_x)
            out.insert(tk.END,"\n"+"L" + str(i) + ": " + str(func_form))
            if subs_bool == True:
                x, x0, x1, x2, x3 = sympy.symbols('x x0 x1 x2 x3')
                out.insert(tk.END,"\n"+"substitute value[x,x0,x1,x2,x3]:"+ str(xs)+" "+str(x0s)+" "+str(x1s)+" "+str(x2s)+" "+str(x3s))
                func_form = func_form.subs([(x,xs),(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s)])
                out.insert(tk.END,"\n"+"substitute result:"+ str(func_form))

            if i == 1 or i == 2:
                h_form = 3*h_form_rtn(max_x)
                multiple_A.append(h_form)
                out.insert(tk.END,"\n"+"A"+str(i)+" = ",str(h_form))
            else:
                h_form = h_form_rtn(max_x)
                multiple_A.append(h_form)
                out.insert(tk.END,"\n"+"A"+str(i)+" = ",str(h_form))
    elif max_x == 4:
        out.insert(tk.END,"run mode: "+ str(m3_dict["3"])+ "\n")
        for i in range(max_x+1):
            func_form = create_lag(i, max_x)
            out.insert(tk.END,"\n"+"L" + str(i) + ": " + str(func_form))
            if subs_bool == True:
                x, x0, x1, x2, x3, x4 = sympy.symbols('x x0 x1 x2 x3 x4')
                out.insert(tk.END,"\n"+"substitute value[x,x0,x1,x2,x3,x4]:"+ str(xs)+" "+str(x0s)+" "+str(x1s)+" "+str(x2s)+" "+ \
                      str(x3s)+" "+str(x4s))
                func_form = func_form.subs([(x,xs),(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s),(x4,x4s)])
                out.insert(tk.END,"\n"+"substitute result:"+ str(func_form))

            if i == 2:
                h_form = 12*h_form_rtn(max_x)
                multiple_A.append(h_form)
                out.insert(tk.END,"\n"+"A2 = " + str(h_form))
            elif i == 1 or i == 3:
                h_form = 32*h_form_rtn(max_x)
                multiple_A.append(h_form)
                out.insert(tk.END,"\n"+"A"+str(i)+" = " + str(h_form))
            else:
                h_form = 7*h_form_rtn(max_x)
                multiple_A.append(h_form)
                out.insert(tk.END,"\n"+"A"+str(i)+" = " + str(h_form))
    else:
        out.insert(tk.END,"\n"+"Not Support Mode")
        return

    simpli_expr = sympy.simplify(create_inside_expr(multiple_A))

    if subs_bool == True:
        if max_x == 2:
            simpli_expr = simpli_expr.subs([(x0,x0s),(x1,x1s),(x2,x2s)])
        elif max_x == 3:
            simpli_expr = simpli_expr.subs([(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s)])
        else:
            simpli_expr = simpli_expr.subs([(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s),(x4,x4s)])
        a1 = a_ent.get()
        b1 = b_ent.get()
        a,b = sympy.symbols("a b")
        dx = sympy.sympify(dx)
        dx = dx.subs([(a,a1),(b,b1)])

    simpli_expr = simpli_expr.subs(h,dx)
    out.insert(tk.END,"\n"+"\nI =" + str(simpli_expr),",h =" +str(dx))
    return


# windows

Lag_windows = tk.Tk()
Lag_windows.title("Lagrange Solution Creator")
Lag_windows.geometry("800x650")

# --- Header --- #
mode_txt = tk.Label(Lag_windows,text="mode:",font=("Comic Sans MS",20))
mode_txt.pack(padx=5, pady=5)

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

# label of substitution
subs_var = tk.BooleanVar()
sub_chk = tk.Checkbutton(Lag_windows, text="substitution:",font=("Comic Sans MS",16), \
                         variable=subs_var,onvalue=True,offvalue=False)
sub_chk.pack(padx=5, pady=5)

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
h_lbl = tk.Label(frame2, text="h=(b-a)/n:",font=("Comic Sans MS",14))
h_lbl.grid(row=3,column=1)
as_lbl = tk.Label(frame2, text="a:",font=("Comic Sans MS",14))
as_lbl.grid(row=2,column=2)
bs_lbl = tk.Label(frame2, text="b:",font=("Comic Sans MS",14))
bs_lbl.grid(row=2,column=3)

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
a_ent = tk.Entry(frame2, width=12)
a_ent.grid(row=3,column=2)
b_ent = tk.Entry(frame2, width=12)
b_ent.grid(row=3,column=3)

#
exe_btn = tk.Button(Lag_windows, text="Run", font=("Comic Sans MS",20),command=run_lagrange)
exe_btn.pack(padx=5,pady=20)

# output Zone
out_lbl = tk.Label(Lag_windows, text="Solution:",font=("Comic Sans MS",18))
out_lbl.pack(padx=5, pady=5, side='left')
out = scrolledtext.ScrolledText(Lag_windows, height = 20, width = 70)
out.pack(padx=5, pady=5)

call_Lag_window()
