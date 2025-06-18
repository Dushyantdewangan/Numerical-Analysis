# Solution of Laplace Equation
import numpy as np
from scipy import linalg
import math
x=float(input("Enter length in x axis "))
y=float(input("Enter length in y axis "))
h=float(input("Enter value of h "))
k=float(input("Enter value of k "))
bc=np.zeros((int(x//h)+1)*(int(y//k)+1)).reshape(int (y//k)+1,int (x//h)+1)
print("Enter Grid Values for ")
for i in range(int(y/k)+1):
    for j in range(int(x/h)+1):
        s=str(i)+str(j)+"  "
        bc[i , j]=float(input(s))
uk=int(input(" Enter no of Unknown grid points "))
val=np.zeros(uk*(uk)).reshape(uk,uk)
valn=np.zeros(uk)
for i in range(uk):
    val [i,i]=-4
for i in range(1,int(y/k)):
    for j in range(1,int(x/h)):
            row=int(bc[i,j])-1
            a,b=i-1,j
            if (a==0 or a==x)or(b==0 or b==y):
              valn[row]=valn[row]-bc[a,b]
            else :
                val [row,int(bc[a,b])-1]=1
            a,b=i,j-1
            if (a==0 or a==x)or(b==0 or b==y):
                 valn[row]=valn[row]-bc[a,b]
            else :
                val[row,int(bc[a,b])-1]=1
            a,b=i,j+1
            if (a==0 or a==x)or(b==0 or b==y):
                valn[row]=valn[row]-bc[a,b]
            else :
              val[row, int(bc[a,b])-1]=1
            a,b=i+1,j
            if (a==0 or a==x)or(b==0 or b==y):
                valn[row]=valn[row]-bc[a,b]
            else :
                val[row, int(bc[a,b])-1]=1
            sol = linalg.solve(val , valn)
a=0
for i in range(1,int(y/k)):
    for j in range(1,int(x/h)):
        bc[i,j]=sol [a]
        a=a+1
print(" Solution is ")
print(bc)