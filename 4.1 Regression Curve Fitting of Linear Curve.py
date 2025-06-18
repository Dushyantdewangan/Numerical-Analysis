def f(a, b, x):
    return (a + b * x)

import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter the number of terms: "))
XY = 0
Xsquare = 0
Y = 0
X = 0
x = np.zeros(n)
y = np.zeros(n)

for i in range(0, n):
    x[i], y[i] = map(float, input("Enter elements: ").split())
    XY = x[i] * y[i] + XY
    Xsquare = Xsquare + x[i] * x[i]
    X = X + x[i]
    Y = Y + y[i]

if (n * Xsquare - X * X == 0):
    print("The value of given data cannot be fitted as linear curve")
    exit()
else:
    b = ((n * XY - X * Y) / (n * Xsquare - X * X))
    a = (Y / n) - ((b * X) / n)
    print("The values of a and b for the following equation y = a + bx are:", a, b)

    g = a + b * x
    h = (g - a) / b

    xu = float(input("Enter the value of x for which the value of y is unknown: "))
    yu = f(a, b, xu)
    print("The value of y is:", yu)

    k = "y = bx + a"

    plt.plot(x, y, label='actual data plot')
    plt.scatter(x, y)
    plt.plot(h, g)
    plt.scatter(h, g, label='curve-fit')
    plt.yscale('linear')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Least-square curve fitting of data set')
    plt.text(5, 10, k, color='r', fontsize=10)
    plt.legend()
    plt.show()
