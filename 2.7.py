# Complex roots by Baristow Method
import cmath
import numpy as np
def b_i(a,n,u,v):
    b=np.zeros(n+1)
    b[n]=a[n]
    b[n-1]=a[n-1]+u*b[n]
    for i in range(n-2,-1,-1):
        b[i]=a[i]+u*b[i+1]+v*b[i+2]
    return b
def c_i(b,n,u,v):
    c=np.zeros(n+1)
    c[n]=0
    c[n-1]=b[n]
    for i in range(n-2,-1,-1):
        c[i]=b[i+1]+u*c[i+1]+v*c[i+2]
    return c
n=int(input( "Enter degree of polynomial  " ))
a=np.zeros(n+1)
b=np.zeros(n+1)
c=np.zeros(n+1)
print(" Input poly coeff . in order fron a(0) t0 a(n) " )
for i in range(n+1):
    a[i]=float(input())
b=a
u0=float(input( "Enter initial values of U0 " ))
v0=float(input( "Enter initial values of V0 " ))
n1=n
while n1>2:
   b=b_i(a,n1,u0,v0)
   c=c_i(b,n1,u0,v0)
   D=c[1]*c[1]-c[0]*c[2]
   du=-(b[1]*c[1]-b[0]*c[2])/D
   dv=-(b[0]*c[1]-b[1]*c[0])/D
   u=u0+du
   v=v0+dv
   b1=a[1]+u*b[2]+v*b[3]
   b0=a[0]+u*b[1]+v*b[2]
   if(b1==0 and b0==0):
     ar=1
     br=-u
     cr=-v
     x1=(-br+cmath.sqrt(br*br-4*ar*cr))/2*ar
     x2=(-br-cmath.sqrt(br*br-4*ar*cr))/2*ar
     print("Roots are ",x1,x2)
     n1=n1-2
     for i in range(n1,-1,-1):
         a[i]=b[ i+2]
   u0=u
   v0=v
if(n1==2):
  u=-a[1]/a[2]
  v=-a[0]/a[2]
  x1=(-br+cmath.sqrt(br*br-4*ar*cr))/2*ar
  x2=(-br-cmath.sqrt(br*br-4*ar*cr))/2*ar
  print(x1,x2)
else:
   x=-a[0]/a[1]
   print(x)