# Trapezoidal, Simpson's 1/3, and Simpson's 3/8 rule
def f(x):
    return (x**2)

x0 = float(input("Enter lower limit: "))
xn = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals (must be even for Simpson's 1/3): "))

# Step size
h = (xn - x0) / n

# Trapezoidal Rule
t_sum = f(x0) + f(xn)
for i in range(1, n):
    x = x0 + i * h
    t_sum += 2 * f(x)
trapezoidal_result = (h / 2) * t_sum

# Simpson's 1/3 Rule
s1_sum = f(x0) + f(xn)
for i in range(1, n):
    x = x0 + i * h
    if i % 2 == 0:
        s1_sum += 2 * f(x)
    else:
        s1_sum += 4 * f(x)
simpsons_13_result = (h / 3) * s1_sum

# Simpson's 3/8 Rule
if n % 3 == 0: 
    s3_sum = f(x0) + f(xn)
    for i in range(1, n):
        x = x0 + i * h
        if i % 3 == 0:
            s3_sum += 2 * f(x)
        else:
            s3_sum += 3 * f(x)
    simpsons_38_result = (3 * h / 8) * s3_sum
else:
    simpsons_38_result = "Not applicable (n must be a multiple of 3)"

# Output results
print("Solution of integral using Trapezoidal Rule:", trapezoidal_result)
print("Solution of integral using Simpson's 1/3 Rule:", simpsons_13_result)
print("Solution of integral using Simpson's 3/8 Rule:", simpsons_38_result)
