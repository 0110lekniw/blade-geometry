import numpy as np
from methods.equations_solver import linearCramerRoots


def linearInterpolation(x, y):
    number_of_points = x.shape[0]
    coefficients = np.empty((number_of_points-1, 2))
    for i in range(0, number_of_points-1):
        coefficients[i, 0] = (y[i+1]-y[i])/(x[i+1]-x[i])
        coefficients[i, 1] = y[i] - x[i]*coefficients[i, 0]
    return coefficients


def quadraticInterpolation(x, y):
    number_of_points = x.shape[0]
    coefficients = np.empty((number_of_points-1, 3))
    a0 = (y[1] - y[0]) / (x[1] - x[0])


    for i in range(0, number_of_points-1):
        if i == 0:
            n = 1
        else:
            n = i
        A = np.empty((3, 3))
        for row in range(2):
            for column in range(3):
                A[row, column] = x[i + row*1] ** (2 - column)
        A[2, 0] = 2*x[n]
        A[2, 1] = 1
        A[2, 2] = 0
        print(A)
        B = np.array([[y[i]], [y[i+1]], [a0]])

    # Calculating Coefficients of quadratic functions
        coefficients[i] = linearCramerRoots(A, B)
        a0 = coefficients[i, 0]*2*x[i+1]+coefficients[i, 1]
    return coefficients

