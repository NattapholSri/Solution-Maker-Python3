import sympy as symp
#import numpy
#import math


def Taylor_series_with_sol(func,n_max,n=0):
    x = symp.symbols("x")
    if n >= n_max:
        diff_now = symp.diff(func)
        print('diff',n,diff_now)
        sol = diff_now.subs(x,0)
        final_level = sol * ((x**n) / symp.factorial(n))
        print("f(n)(0) * x**n / n!  value in this level:", final_level, "\n")
        return final_level
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


#---Code for debug---#

#a,b,x = symp.symbols('a b x')
#f1 = 1/(2-(2*x))
#sym_exp = symp.sin(x)
#sym_exp2 = symp.exp(-x)

#answer_exp = symp.simplify(Taylor_series_with_sol(f1,10))
