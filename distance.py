import cmath

def distance(firstPoint, secondPoint, distanceMax = None):
    #  TODO conversion if in grades
            R =  6372.795477598

            latA = (firstPoint[0]*cmath.pi)/180
            lonA = (firstPoint[1]*cmath.pi)/180

            latB = (secondPoint[0]*cmath.pi)/180
            lonB = (secondPoint[1]*cmath.pi)/180

            distance = R*cmath.acos(cmath.sin(latA)*cmath.sin(latB) + cmath.cos(latA)*cmath.cos(latB)*cmath.cos(lonA-cmath.cos(lonB)))
            distance = float(distance.real)
           
            if distanceMax != None:
             return (distance <= distanceMax)
            elif distanceMax == 'Default':
             return (distance <= 50)