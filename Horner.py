from sympy import *
import math

r = math.pi
i=0
ans = 0
ans2=0
sup = [] #เก็บค่าหลังดิป
sup2 = [] # เก็บ X ที่เพิ่มขึ้น
x = symbols('x') #กำหนดแทนสัญสักษณ์
a = symbols('a') #กำหนดแทนสัญสักษณ์
di = sin(a)
dy = 0
n = 9 # 0-9 10จำนวน
for i in range(10) : #ให้เก็บจำนวน10ค่า
    dy = di.replace(a,int(0))

    #if dy != 0: #ว่าคำตอบมีค่าเท่ากับ 0 ไหม

    sup.append(dy/math.factorial(i)) # a/n!
    print(di, '/',i,'!', ' = ', dy,'/',math.factorial(i))
    #sup2.append((x ** i)) #x^n

    di = diff(di) #ดิฟต่อเนื่อง

print(sup)
#print(sup2)

for i in range(10):#เพื่อรวมค่า
    print(sup[n], '+', '(', ans, '*', '(', r, '/', 4, ')', ')', '=', sup[n]+(ans*(r/4)))
    ans = sup[n]+(ans*(r/4))# bn = an + bn*x

    n -= 1
print('ANS','=',ans) # แสดงคำตอบ



