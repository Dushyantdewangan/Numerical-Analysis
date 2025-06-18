def f(x,y):
    return ((2*y)/x)
def heun(x0,y0,n,h):
    x=x0
    y=y0
    i=1
    print("Heun's Method:")
    print("%2d %2.6f %2.6f" %(i,x,y))
    while x<=n:
        y = y + h*(f(x,y)+f(x+h,y+h*f(x,y)))/2
        x = x+h
        i = i +1
        print("%2d %2.6f %2.6f" %(i,x,y))
x0 = float(input("Enter initial value of x: "))
y0 = float(input("Enter initial value of y: ")) 
x = float(input("Enter final value of x: "))
n = float(input("Enter step size: "))
h = (x-x0)/n
heun(x0,y0,x,h)