# Bisection method
import math
def f(x):
    return (x*x*x -4*x -9)
def bisect (a,b,p):
    x=(a+b)/2
    x=round(x,p+1)
    return x
a=int(input("Enter value of interval a "))
b=int(input("Enter value of interval b "))
maxitr = int(input("Enter max no. of iterations "))
p = int(input("Enter precision  "))
err=pow(10,-p)
itr=1
xp=b
while (itr<=maxitr):
    x=bisect(a,b,p)
    if (f(a)*f(x)<0):
        b=x
    else:
        a=x
    print("After", itr , "iterations , root = ", x)
    if(abs(x-xp)< err):
        print("Value of root is ", x)
        exit()
    xp=x
    itr=itr+1
print("Increase maximum iterations")