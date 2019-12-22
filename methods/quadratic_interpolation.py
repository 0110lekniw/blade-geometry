import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 5, 7, 8, 9, 12])
y = np.array([0, -3, 6, -10, 20, -3, 49])
number_of_points = x.shape[0]
a0 = (y[1] - y[0]) / (x[1] - x[0])
b0 = y[1] - x[1] * a0
fig = plt.figure()
x_prim = np.linspace(x[0], x[1], 10)
plt.plot(x_prim, x_prim * a0 + b0)
coefficients = np.empty((number_of_points, 3))

for i in range(1, number_of_points-1):
    A = np.empty((3, 3))

    for row in range(2):
        for column in range(3):
            A[row, column] = x[i + row*1] ** (2 - column)
    A[2, 0] = 2*x[i]
    A[2, 1] = 1
    A[2, 2] = 0
    print(A)

    detW = round(np.linalg.det(A), 10)
    B = np.array([[y[i]], [y[i+1]], [a0]])


# Calculating Coefficients of quadratic functions

    for column in range(3):
        A_prim = np.array(A)
        A_prim[:, column] = B[:, 0]
        detA = round(np.linalg.det(A_prim), 10)
        coefficients[i, column] = detA / detW
    print(coefficients)
    print(x[i+1])
    a0 = coefficients[i, 0]*2*x[i+1]+coefficients[i, 1]
    x_bis = np.linspace(x[i],x[i+1],100)
    plt.plot(x_bis, x_bis**2*coefficients[i, 0]+x_bis*coefficients[i, 1]+coefficients[i, 2])

plt.show()
