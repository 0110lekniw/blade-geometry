import methods.geometrical_calculations as gc
import numpy as np
import matplotlib.pyplot as plt
import math

first_point = np.array([[0, 0], [1, 2], [2, 4]])
second_point = np.array([[-1, 10], [1, -10], [2, -20]])

fig = plt.figure(figsize=(10, 10))
linear_function_1 = gc.twoPointsLinearFunction(first_point[0, :], first_point[1, :])
linear_function_2 = gc.twoPointsLinearFunction(second_point[0, :], second_point[1, :])
x = np.linspace(-10, 10, 100)
plt.plot(x, linear_function_1(x), '+', x, linear_function_2(x), '+')

# bisectors = gc.averageDegreeBisectorEquation(linear_function_1, linear_function_2, 'larger')
# plt.plot(x, bisectors(x), color='b')

degree = math.pi/2
first_points_turned = gc.turnAroundPoint(first_point, degree, np.array([0, 0]))
second_points_turned = gc.turnAroundPoint(second_point, degree, np.array([0, 0]))
linear_function_3 = gc.twoPointsLinearFunction(first_points_turned[0, :], first_points_turned[1, :])
linear_function_4 = gc.twoPointsLinearFunction(second_points_turned[0, :], second_points_turned[1, :])

plt.plot(x, np.zeros((x.shape[0],1)), color='k')
plt.plot(np.zeros((x.shape[0],1)), x, color='k')
plt.plot(x, linear_function_3(x), '-', x, linear_function_4(x), '-')
plt.scatter(first_point[:, 0], first_point[:, 1], color="k")
plt.scatter(first_points_turned[:, 0], first_points_turned[:, 1], color="g")
plt.scatter(second_point[:, 0], second_point[:, 1], color="r")
plt.scatter(second_points_turned[:, 0], second_points_turned[:, 1], color="y")
plt.show()