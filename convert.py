import cmath

def layerNumberFromName(name):
        layers = getListOfLayers()
        return layers.index(name)
def layerNameFromIndex(index):
        layers = getListOfLayers()
        return layers.get(index)

def convertDecimalToRadians(coordinates):
    radianCoordinates = []
    radianCoordinates[0] = (coordinates[0]*cmath.pi)/180
    radianCoordinates[1] = (coordinates[1]*cmath.pi)/180

    return radianCoordinates

def convertRadiansToDecimal(coordinates):
    decimalCoordinates = []
    decimalCoordinates[0] = (coordinates[0]*180)/cmath.pi
    decimalCoordinates[1] = (coordinates[1]*180)/cmath.pi

    return decimalCoordinates
