import methods.geometrical_calculations as gc
import numpy as np
import matplotlib.pyplot as plt

first_point = np.array([[0, 0], [1, 2], [2, 4]])
second_point = np.array([[0, 0], [1, 1], [2, 2]])

fig = plt.figure()
linear_function_1 = gc.twoPointsLinearFunction(first_point[0, :], first_point[1, :])
linear_function_2 = gc.twoPointsLinearFunction(second_point[0, :], second_point[1, :])
x = np.linspace(-10, 10, 100)
plt.plot(x, linear_function_1(x), '-', x, linear_function_2(x), '--')

bisectors = gc.averageDegreeBiscetorEquation(linear_function_1, linear_function_2, 'larger')
plt.plot(x, bisectors(x), color='b')
plt.show()
