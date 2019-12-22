import pandas as pd
import numpy as np
import math

# import coordinates of rotor blade and create numpy array
profiles_number = np.array(pd.ExcelFile(
    '/Volumes/Bridge/Aviation /Bachelor/blade-geometry/Rotor_Coordinates.xlsx').sheet_names).shape[0]

rotor_characteristic = np.zeros((6, profiles_number))
rotor_coordinates = np.zeros((24, 6, profiles_number))

for i in range(profiles_number):
    data = pd.read_excel(
        '/Volumes/Bridge/Aviation /Bachelor/blade-geometry/Rotor_Coordinates.xlsx', sheet_name=i).to_numpy()

    # Defining characteristic values:
    #   0 = radius of profile;
    #   1 = radius of the leading edge;
    #   2 = radius of the trailing edge;
    #   3 - x distance between beginning of the profile and stocking point;
    #   4 - y distance between beginning of the profile and stocking point;
    #   5 - angle of turn of coordinates around stocking point

    pressure_side_coordinates = np.array([data[7:, 0], data[7:, 1]]).transpose()
    suction_side_coordinates = np.array([data[7:, 0], data[7:, 2]]).transpose()

    rotor_characteristic[:5, i] = data[:5, 1]
    rotor_characteristic[5, i] = data[5, 1] * (math.pi / 180)

    rotor_coordinates[:pressure_side_coordinates.shape[0], :2, i] = pressure_side_coordinates[:, :]
    rotor_coordinates[:pressure_side_coordinates.shape[0], 3, i] = data[0, 1]
    rotor_coordinates[:suction_side_coordinates.shape[0], 3:5, i] = suction_side_coordinates[:, :]
    rotor_coordinates[:pressure_side_coordinates.shape[0], 5, i] = data[0, 1]

Canal_Coordinates = pd.read_excel('/Volumes/Bridge/Aviation /Bachelor/blade-geometry/Canal.xlsx').to_numpy()



