import sympy as symp
from Taylor_series import Taylor_series_with_sol
from Lagrange_polynomial import lagrange_polynomial


run = True
while run:
    print("Function select: \n0 or else = exit")
    print("1 = Taylor's series")
    print("3 = show lagrange polynomial")
    mode = int(input("Select Mode [0,1,3]:"))
    if mode == 1:
        f = str(input("Enter Function expression:="))
        diff_level = int(input("Enter length of taylor series to show:="))
        show_n = input("[optional] show n only:=")
        f = symp.sympify(f)
        ans = symp.simplify(Taylor_series_with_sol(f,diff_level))
        print(show_n) if show_n != "" else print("No value")
        print("Taylor's form:",ans)
        ask = str(input("want to substitution?[y/n]:")).lower()
        if ask == "y":
            ask_v = int(input('Enter substitution value='))
            print(ans.subs(ask_v))
        print("Done!\n")
    elif mode == 3:
        print("Mode select\n1 = simpson's 1/3 rule\n2 = simpson's 3/8 rule\n3 = Boole's rule")
        f = int(input("Enter mode value:="))
        lagrange_polynomial(f+1)
        print("Done!\n")
    else:
        run = False
        print("exit program")