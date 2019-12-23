import numpy as np
import math
from methods.equations_solver import linearCramerRoots


def linearFunctionsIntersections(function_one, function_two):
    A = np.array([-function_one[0], 1], [-function_two[0], 1])
    B = np.array([function_one[1]], [function_two[1]])
    return linearCramerRoots(A, B)

def vectorCalculation(first_point, second_point):
    delta_x = second_point[0] - first_point[0]
    delta_y = second_point[1] - first_point[1]
    modulo = math.sqrt(delta_x**2+delta_y**2)
    return np.array([delta_x, delta_y, modulo])


def scalarProductVector(vector_1, vector_2):
    product = vector_1[0]*vector_2[0]+vector_1[1]*vector_2[1]
    return product


def degreeBetweenVectors(vector_1, vector_2):
    scalar_product = scalarProductVector(vector_1, vector_2)
    cosinus_degree = scalar_product/(vector_1[2]*vector_2[2])
    degree = math.acos(cosinus_degree)
    return degree


def averageDegreeBiscetorEquation(linear_one, linear_two):
    # dc  - directional coefficient
    bisector_dc_smaller_angle = math.tan((math.atan(linear_one[0]) + math.atan(linear_two[0])) / 2)
    intersection_point = linearFunctionsIntersections(linear_one, linear_two)
    bisector_coefficient_smaller_angle = intersection_point[1] - intersection_point[0]*bisector_dc_smaller_angle
    vector_one = vectorCalculation(intersection_point, np.array([intersection_point[0]+1,
                                                        (intersection_point[0]+1)*linear_one[0]+linear_one[1]]))
    vector_two = vectorCalculation(intersection_point, np.array([intersection_point[0]+1,
                            (intersection_point[0]+1)*bisector_dc_smaller_angle+bisector_coefficient_smaller_angle]))
    smaller_degree = degreeBetweenVectors(vector_one, vector_two)
    if smaller_degree > math.pi/2:
        smaller_degree = smaller_degree-math.pi/2
        bisector_dc_smaller_angle = -1/bisector_dc_smaller_angle
    bisector_dc_larger_angle = -1/bisector_dc_smaller_angle
    bisector_coefficient_larger_angle = intersection_point[1] - intersection_point[0]*bisector_dc_larger_angle
    larger_degree = smaller_degree+math.pi/2
    return np.array([[bisector_dc_smaller_angle, bisector_coefficient_smaller_angle, smaller_degree],
                     [bisector_dc_larger_angle, bisector_coefficient_larger_angle, larger_degree]])





