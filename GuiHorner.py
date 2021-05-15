
from tkinter import *
from tkinter import scrolledtext
from sympy import *
import sympy as sym
import math

a = symbols('a') #กำหนดแทนสัญสักษณ์
x = symbols('x') #กำหนดแทนสัญสักษณ์
def horner(fn,n):
    r = math.pi

    ans = 0

    sup = [] #เก็บค่าหลังดิป

    di = fn

    #n = n # 0-9 10จำนวน
    for i in range(n) : #ให้เก็บจำนวน10ค่า
        dy = di.replace(a,int(0))


        #if dy != 0: #ว่าคำตอบมีค่าเท่ากับ 0 ไหม

        sup.append(dy/math.factorial(i)) # a/n!
        print(di, '/',i,'!', ' = ', dy,'/',math.factorial(i))
        out.insert(END,str(di)+ '/'+ str(i) +'!'+ ' = '+ str(dy) +'/'+ str(math.factorial(i))+ '\n')
        #sup2.append((x ** i)) #x^n

        di = diff(di) #ดิฟต่อเนื่อง

    print(sup)
    out.insert(END,'\n')
    out.insert(END,str(sup)+'\n')
    out.insert(END,'\n')

    #print(sup2)

    print(len(sup))
    n= len(sup)-1
    for i in range(len(sup)):#เพื่อรวมค่า
        print('a',n,i)
        print(sup[n], '+', '(', ans, '*', '(', r, '/', 4, ')', ')', '=', sup[n]+(ans*(r/4)))

        out.insert(END,str(sup[n])+ '+'+ '('+ str(ans)+ '*'+ '('+ str(r)+ '/ 4 ' + ') ) = '+ str(sup[n]+(ans*(r/4))) + '\n')
        ans = sup[n]+(ans*(r/4))# bn = an + bn*x

        n -= 1
    print('ANS','=',ans) # แสดงคำตอบ
    out.insert(END, '\n')
    out.insert(END,'ANS'+'='+ str(ans))


window = Tk()
window.title("Horner’ Scheme (Solution mk Programs)")
window.geometry('600x600')

def helloCallBack():
    print('start')
    out.delete('1.0', END)
    out.insert(END, "show Solution:\n")
    fn=sym.sympify(E1.get())
    n= int(E2.get())
    horner(fn,n)

run = Button(window, text ="run",font=("Comic Sans MS",20), command = helloCallBack)
run.grid(column=1, row=2)
L1 = Label(window, text="Function :",font=("Comic Sans MS",18))
L1.grid(column=0, row=0)
L2 = Label(window, text="n :",font=("Comic Sans MS",18))
L2.grid(column=0, row=1)
E1 = Entry(window, bd =5)
E1.grid(column=1, row=0)
E2 = Entry(window, bd =5)
E2.grid(column=1, row=1)

out = scrolledtext.ScrolledText(window, height = 20, width = 70)
out.grid(column=0,row=3,columnspan=3)






window.mainloop()