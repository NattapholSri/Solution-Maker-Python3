import sys
import sympy


def lagrange_polynomial(max_x):
    m3_dict = {"1": "simpson's 1/3 rule", "2": "simpson's 3/8 rule", "3": "Boole's rule"}
    dx = "(b-a)/"+str(max_x)
    h = sympy.Symbol("h")
    multiple_A = []

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
            print("L"+str(i)+":",create_lag(i,max_x))
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
            print("L"+str(i)+":",create_lag(i,max_x))
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
            print("L"+str(i)+":",create_lag(i,max_x))
            if i == 2:
                h_form = 12*h_form_rtn(max_x)
                multiple_A.append(h_form)
                print("A2 =",h_form)
            elif  i == 1 or i == 3:
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

    print("\nI =",simpli_expr,",h =",dx)

