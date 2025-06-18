# Multiple roots by Newton's Method
import math
import numpy as np
def f(x,n,a):
   sum=0
   for i in range(n+1):
      sum=sum+a[i]*pow(x, i)
   return sum
def df(x,n,a):
  d=np.zeros(n)
  for i in range(n-1,-1,-1):
    d[i]=(i+1)*a[i+1]
  sum=0
  for i in range(n):
      sum=sum+d[i]*pow(x, i)
  return sum
def newt_raph(x1,p,n,a):
    x=x1-(f(x1,n,a)/df(x1,n,a))
    x=round(x,p+1)
    return x
def deflate(a,n,r):
     b=np.zeros(n+1)
     for i in range(n,-1,-1):
         b[i-1]=a[i]+r*b[i]
     return b
n=int(input("Enter degree of polynomial"))
a=np.zeros(n+1)
b=np.zeros(n+1)
r=np.zeros(n+1)
print("Input poly coeff . in order fron a(0) t0 a(n)")
for i in range(n+1):
    a[i]=float(input())
b=a
x0=int(input("Enter initial guess of root" ))
p=8
maxitr=100
err=pow(10,-p)
n1=n
while n1>1:
    itr=1
    xp=x0
    while(itr<=maxitr):
        x=newt_raph(xp,p,n1,b)
        if(abs(x-xp)< err):
           break
        xp=x
        itr=itr+1
    r[n1-1]=x
    b=deflate(b,n1,x)
    x0=x
    n1=n1-1
    itr=1
r[0]=-b[0]/b[1]
print("Roots are")
for i in range(n):
    print(r[i])