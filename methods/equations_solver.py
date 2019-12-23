import numpy as np
import math
import cmath

def quadraticRealRoots(a, b, c):
    roots = 0
    if a == 0:
        print("Not a quadratic equation")
    differentiator = b**2 - 4*a*c
    if differentiator == 0:
        roots = -b/(2*a)
    elif differentiator > 0:
        root_1 = (-b-math.sqrt(differentiator))/(2*a)
        root_2 = (-b+math.sqrt(differentiator))/(2*a)
        roots = [root_1, root_2]
    elif differentiator < 0:
        print("No roots in the set of real numbers ")
    return roots


def quadraticRoots(a, b, c):
    coefficients = np.array([a, b, c])
    for i in range(coefficients.shape[0]):
        if not isinstance(coefficients[i], complex):
            coefficients[i] = complex(coefficients[i], 0)
    differentiator = coefficients[1]**2-coefficients[0]*coefficients[2]*4
    root_1 = (-coefficients[1] - cmath.sqrt(differentiator)) / (2 * coefficients[0])
    root_2 = (-coefficients[1] + cmath.sqrt(differentiator)) / (2 * coefficients[0])
    roots = [root_1, root_2]
    return roots


def linearCramerRoots(left_hand_side_matrix, right_hand_side_matrix):
    roots = np.zeros((left_hand_side_matrix.shape[0]))
    main_determination = round(np.linalg.det(left_hand_side_matrix), 10)
    for column in range(left_hand_side_matrix.shape[1]):
        root_matrix = np.array(left_hand_side_matrix)
        root_matrix[:, column] = right_hand_side_matrix[:, 0]
        root_determination = round(np.linalg.det(root_matrix), 10)
        roots[column] = root_determination / main_determination
    return roots

