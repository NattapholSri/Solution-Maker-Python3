import sys
import sympy

sympy.init_printing()

def lagrange_polynomial(max_x):
    m3_dict = {"1": "simpson's 1/3 rule", "2": "simpson's 3/8 rule", "3": "Boole's rule"}
    dx = "(b-a)/"+str(max_x)
    h = sympy.Symbol("h")
    multiple_A = []
    substi_chk = str(input("substitution?[y/n]:"))
    subs_bool = False


    def substitution_var_ask(max_x):
        global xs,x0s,x1s,x2s,x3s,x4s
        if max_x == 2:
            xs = str(input("x value:"))
            x0s = str(input("x0 value:"))
            x1s = str(input("x1 value:"))
            x2s = str(input("x2 value:"))
        elif max_x == 3:
            xs = str(input("x value:"))
            x0s = str(input("x0 value:"))
            x1s = str(input("x1 value:"))
            x2s = str(input("x2 value:"))
            x3s = str(input("x3 value:"))
        elif max_x == 4:
            xs = str(input("x value:"))
            x0s = str(input("x0 value:"))
            x1s = str(input("x1 value:"))
            x2s = str(input("x2 value:"))
            x3s = str(input("x3 value:"))
            x4s = str(input("x4 value:"))
        else:
            print("error!")

    if substi_chk.lower() == "y":
        subs_bool = True
        substitution_var_ask(max_x)

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

    # Main loop
    if max_x == 2:
        print("run mode:",m3_dict["1"])
        for i in range(max_x+1):
            func_form = create_lag(i,max_x)
            print("L" + str(i) + ":", func_form)
            if subs_bool == True:
                x, x0, x1, x2 = sympy.symbols('x x0 x1 x2')
                print("substitute value[x,x0,x1,x2]:",xs,x0s,x1s,x2s)
                func_form = func_form.subs([(x,xs),(x0,x0s),(x1,x1s),(x2,x2s)])
                print("substitute result:",func_form)

            if i == 1:
                h_form = 4*h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A1 =",h_form)
            else:
                h_form = h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A"+str(i)+" =",h_form)
    elif max_x == 3:
        print("run mode:", m3_dict["2"])
        for i in range(max_x+1):
            func_form = create_lag(i, max_x)
            print("L" + str(i) + ":", func_form)
            if subs_bool == True:
                x, x0, x1, x2, x3 = sympy.symbols('x x0 x1 x2 x3')
                print("substitute value[x,x0,x1,x2,x3]:",xs,x0s,x1s,x2s,x3s)
                func_form = func_form.subs([(x,xs),(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s)])
                print("substitute result:",func_form)

            if i == 1 or i == 2:
                h_form = 3*h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A"+str(i)+" =",h_form)
            else:
                h_form = h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A"+str(i)+" =",h_form)
    elif max_x == 4:
        print("run mode:", m3_dict["3"])
        for i in range(max_x+1):
            func_form = create_lag(i, max_x)
            print("L" + str(i) + ":", func_form)
            if subs_bool == True:
                x, x0, x1, x2, x3, x4 = sympy.symbols('x x0 x1 x2 x3 x4')
                print("substitute value[x,x0,x1,x2,x3,x4]:",xs,x0s,x1s,x2s,x3s,x4s)
                func_form = func_form.subs([(x,xs),(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s),(x4,x4s)])
                print("substitute result:",func_form)

            if i == 2:
                h_form = 12*h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A2 =",h_form)
            elif i == 1 or i == 3:
                h_form = 32*h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A"+str(i)+" =",h_form)
            else:
                h_form = 7*h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A"+str(i)+" =",h_form)
    else:
        print("Not Support Mode")
        sys.exit()

    simpli_expr = sympy.simplify(create_inside_expr(multiple_A))

    if subs_bool == True:
        if max_x == 2:
            simpli_expr = simpli_expr.subs([(x0,x0s),(x1,x1s),(x2,x2s)])
        elif max_x == 3:
            simpli_expr = simpli_expr.subs([(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s)])
        else:
            simpli_expr = simpli_expr.subs([(x0,x0s),(x1,x1s),(x2,x2s),(x3,x3s),(x4,x4s)])
        a1 = input('a value=')
        b1 = input('b value=')
        a,b = sympy.symbols("a b")
        dx = sympy.sympify(dx)
        dx = dx.subs([(a,a1),(b,b1)])

    simpli_expr = simpli_expr.subs(h,dx)
    print("\nI =",simpli_expr,",h =",dx)

#lagrange_polynomial(2)
