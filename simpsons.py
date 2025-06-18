import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2  # Example function to integrate

# Initialize arrays for storing results
t = np.zeros(1000)
s = np.zeros(1000)
s3 = np.zeros(1000)
ni = np.arange(6, 6006, 6)

# Input lower and upper limits
x0 = float(input("Enter lower limit: "))
xn = float(input("Enter upper limit: "))

i = 0
n = 6

while n <= 6000:
    h = (xn - x0) / n
    t[i] = f(x0) + f(xn)
    s[i] = t[i]
    s3[i] = t[i]
    x = x0
    n1 = 0

    while x < xn - h:
        n1 += 1
        x += h
        t[i] += 2 * f(x)
        if n1 % 3 == 0:
            s3[i] += 2 * f(x)
        else:
            s3[i] += 3 * f(x)
        if n1 % 2 == 0:
            s[i] += 2 * f(x)
        else:
            s[i] += 4 * f(x)

    # Finalize results for this iteration
    s[i] = s[i] * h / 3
    t[i] = t[i] * h / 2
    s3[i] = s3[i] * 3 * h / 8

    n += 6
    i += 1

# Plotting the results
plt.title("Comparison of Numerical Integration Methods")
plt.plot(ni, t[:len(ni)], c='r', label='Trapezoidal')
plt.plot(ni, s[:len(ni)], c='g', label="Simpson's 1/3")
plt.plot(ni, s3[:len(ni)], c='b', label="Simpson's 3/8")
plt.xlabel('No. of subintervals')
plt.ylabel('Result')
plt.legend()
plt.grid()
plt.show()