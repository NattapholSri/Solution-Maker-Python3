import sympy as symp
#import numpy
#import math


def Taylor_series_with_sol(func,n_max,n=0):
    x = symp.symbols("x")
    if n >= n_max:
        diff_now = symp.diff(func)
        print('diff',n,diff_now)
        sol = diff_now.subs(x,0)
        return sol * ((x**n) / symp.factorial(n))
    elif n == 0:
        sol = func.subs(x,0)
        print("no diff",func)
        this_level = sol * ((x**n) / symp.factorial(n))
        n = n+1
        print("f(n)(0) * x**n / n!  value in this level:",this_level,"\n")
        return this_level + Taylor_series_with_sol(func,n_max,n)
    else:
        diff_now = symp.diff(func)
        print('diff',n,diff_now)
        sol = diff_now.subs(x,0)
        n = n+1
        this_level = sol * ((x**n) / symp.factorial(n))
        print("f(n)(0) * x**n / n!  value in this level:",this_level,"\n")
        return this_level + Taylor_series_with_sol(diff_now,n_max,n)


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
run = True
while run:
    mode = int(input("Select Mode [0,1]:"))
    if mode == 1:
        f = str(input("Enter Function expression:="))
        diff_level = int(input("Enter length of taylor series to show:="))
        show_n = input("[optional] show n only:=")
        f = symp.sympify(f)
        Taylor_series_with_sol(f,diff_level)
        print(show_n) if show_n != "" else print("No value")
    else:
        run = False
        print("exit program")



a,b,x = symp.symbols('a b x')
f1 = 1/(2-(2*x))
sym_exp = symp.sin(x)
sym_exp2 = symp.exp(-x)

answer_exp = symp.simplify(Taylor_series_with_sol(f1,10))

ask = str(input("want to substitution?[y/n]:")).lower()
if ask == "y":
    ask_v = int(input('Enter substitution value='))
    print(answer_exp.subs(ask_v))