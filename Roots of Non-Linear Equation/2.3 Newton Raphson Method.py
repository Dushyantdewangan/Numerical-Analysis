# Newton-Raphson Method
import math
def f(x):
    return (x*x*x-4*x -9)
def Df(x):
    return(3*x*x-4)
def newt_raph(x1,p):
    x=x1-(f(x1)/Df(x1))
    x=round(x,p+1)
    return x
x1=int(input("Enter approx. value of root "))
maxitr = int(input("Enter max no. of iterations "))
p = int(input("Enter precision  "))
err=pow(10,-p)
itr=1
xp=x1
while (itr<=maxitr):
    x=newt_raph(xp,p)
    print(" After ", itr, "iterations ,  root=",x)
    if(abs(x-xp)< err):
        print("Value of root is ", x)
        exit()
    xp=x
    itr=itr+1
print("Increase maximum iterations")