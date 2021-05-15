
from tkinter import *
from tkinter import scrolledtext
from sympy import *
import sympy as sym
import math

a = symbols('a') #กำหนดแทนสัญสักษณ์

def horner(fn,n,sub):
    r = math.pi

    di = fn
    poly =fn
    result = int(poly[0])
    x = sub
    #n = n # 0-9 10จำนวน
    for i in range(1, n):
        result1 = (result * x )+ int(poly[i])
        out.insert(END,str(result)+'*'+ str(x) + '+' + str(poly[i])+ '=' + str(result1)+'\n')
        result = result1
    #return result1
    print(result1)
    out.insert(END,'P(x=' + str(sub)  +')'+' = bn = '+str(result) )





        #if dy != 0: #ว่าคำตอบมีค่าเท่ากับ 0 ไหม





window = Tk()
window.title("Horner’ Scheme (Solution mk Programs)")
window.geometry('600x600')

def helloCallBack():
    print('start')
    out.delete('1.0', END)
    out.insert(END, "show Solution:\n")
    fn=sym.sympify(E1.get())
    n= int(E2.get())
    if E3.get() == '':
        sub = 0
    else:
        sub = float(E3.get())
    horner(fn,n,sub)

run = Button(window, text ="run",font=("Comic Sans MS",20), command = helloCallBack)
run.grid(column=1, row=3)
L1 = Label(window, text="an - a0 :",font=("Comic Sans MS",18))
L1.grid(column=0, row=0)
L2 = Label(window, text="n :",font=("Comic Sans MS",18))
L2.grid(column=0, row=1)
L3 = Label(window, text="X = :",font=("Comic Sans MS",18))
L3.grid(column=0, row=2)
E1 = Entry(window, bd =5)
E1.grid(column=1, row=0)
E2 = Entry(window, bd =5)
E2.grid(column=1, row=1)
E3 = Entry(window, bd =5)
E3.grid(column=1, row=2)

out = scrolledtext.ScrolledText(window, height = 20, width = 70)
out.grid(column=0,row=4,columnspan=3)






window.mainloop()