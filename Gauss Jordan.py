def gaussjordan():
    import numpy as np
    n = int(input("Enter the number of variables:"))
    A = np.zeros((n, n + 1))
    X = np.zeros(n)
    print("Enter the coefficient of augumented matrix: ")
    for i in range(n):
        for j in range(n+1):
            A[i][j] = float(input('A['+str(i)+']['+str(j)+']='))
        print(A)
        for i in range(n):
            if A[i][j] == 0.0:
                print("Divide by zero detected!")
                break
            for j in range(n):
                if i != j:
                    r = A[j][i] / A[i][i]
                    for k in range(n+1):
                        A[j][k] = A[j][k] - r * A[i][k]
    print("The diagonal matrix is: ")
    print(A)
    print("\n The values of the variables are:")
    for i in range(n):
        X[i]= A[i][n] / A[i][i]
    for i in range(n):
        print("X%d = %0.2f" %(i, X[i]), end="\n")

gaussjordan()