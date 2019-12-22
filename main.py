from methods.excel_import import importRotorCharacteristics, importCanalCoordinates, importRotorCoordinates

rotor_37_coordinates = importRotorCoordinates(
    '/Volumes/Bridge/Aviation /Bachelor/blade-geometry/Rotor_Coordinates.xlsx')
rotor_37_charateristics = importRotorCharacteristics(
    '/Volumes/Bridge/Aviation /Bachelor/blade-geometry/Rotor_Coordinates.xlsx')
canal_coordinates = importCanalCoordinates(
    '/Volumes/Bridge/Aviation /Bachelor/blade-geometry/Canal.xlsx')
