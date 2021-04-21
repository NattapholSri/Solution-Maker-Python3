import sympy as symp

def Taylor_series_with_sol(func,n_max,n=0,view_lm=-1):
    # check limit view
    if view_lm == -1:
        view_lm = n_max+1

    x = symp.symbols("x")
    if n >= n_max:
        diff_now = symp.diff(func)
        sol = diff_now.subs(x,0)
        final_level = sol * ((x**n) / symp.factorial(n))
        if n <= view_lm:
            print('diff', n, ":", diff_now)
            print("f(n)(0) * x**n / n!  value in this level:", final_level, "\n")
        return final_level
    elif n == 0:
        sol = func.subs(x,0)
        this_level = sol * ((x**n) / symp.factorial(n))
        n = n+1
        if n <= view_lm:
            print("no diff", func)
            print("f(n)(0) * x**n / n!  value in this level:",this_level,"\n")
        return this_level + Taylor_series_with_sol(func,n_max,n,view_lm)
    else:
        diff_now = symp.diff(func)
        sol = diff_now.subs(x,0)
        n = n+1
        this_level = sol * ((x**n) / symp.factorial(n))
        if n <= view_lm:
            print('diff', n,":", diff_now)
            print("f(n)(0) * x**n / n!  value in this level:",this_level,"\n")
        return this_level + Taylor_series_with_sol(diff_now,n_max,n,view_lm)


#---Code for debug---#

#a,b,x = symp.symbols('a b x')
#f1 = 1/(2-(2*x))
#sym_exp = symp.sin(x)
#sym_exp2 = symp.exp(-x)

#answer_exp = symp.simplify(Taylor_series_with_sol(f1,10))

