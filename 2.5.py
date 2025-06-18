# FIxed-Point Method
def f(x):
    return(2-x*x)
x0=float(input("Enter value of x0  "))
p=int(input("Enter allowed precision  "))
err=pow(10,-p)
itr=1
x=f(x0)
while (abs(x-x0)>err):
    print(" After ", itr , " iterations value of root is", round(x,p+1))
    x0=x
    x=f(x0)
    itr=itr+1
print("Value of root is", round(x,p+1))