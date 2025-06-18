# Secant Method
import math
def f(x):
    return (x*x-4*x-10)
def secant(x1,x2,p):
    x=x2-(f(x2)*(x2-x1)/(f(x2)-f(x1)))
    x=round(x,p+1)
    return x
x1=int(input("Enter the value of x1 "))
x2=int(input("Enter the value of x2 "))
maxitr = int(input("Enter max no. of iterations "))
p = int(input("Enter precision  "))
err=pow(10,-p)
itr=1
while (itr<=maxitr):
    x=secant(x1,x2,p)
    print(" After ", itr, "iterations ,  root=",x)
    if(abs(x-x2)< err):
        print("Value of root is ", x)
        exit()
    x1=x2
    x2=x
    itr=itr+1
print("Increase maximum iterations")