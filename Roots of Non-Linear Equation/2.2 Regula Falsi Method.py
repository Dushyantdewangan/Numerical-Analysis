# Regula-Falsi Method
import math
def f(x):
    return (x*x*x-4*x -9)
def regula(x1,x2,p):
    x=x1-(f(x1)*(x2-x1)/(f(x2)-f(x1)))
    x=round(x,p+1)
    return x
x1=int(input("Enter value of x1 "))
x2=int(input("Enter value of x2 "))
maxitr = int(input("Enter max no. of iterations "))
p = int(input("Enter precision  "))
err=pow(10,-p)
itr=1
xp=x1
while (itr<=maxitr):
    x=regula(x1,x2,p)
    if (f(x1)*f(x)<0):
        x2=x
    else:
        x1=x
    print("After", itr , "iterations , root = ", x)
    if(abs(x-xp)< err):
        print("Value of root is ", x)
        exit()
    xp=x
    itr=itr+1
print("Increase maximum iterations")