import csv
import cmath
import datetime

def Extract(pathFile, coordinatesPoint, distanceMax, yearsAgo):
        
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        coordinates = []
        validRows = []
        R = 6372.795477598
        now = datetime.datetime.now()

        for row in csv_reader:
            coordinates = [float(row["LATITUDE"]),float(row["LONGITUDE"])]
            year = int(row["YEAR"])

            latA = (coordinatesPoint[0]*cmath.pi)/180
            lonA = (coordinatesPoint[1]*cmath.pi)/180

            latB = (coordinates[0]*cmath.pi)/180
            lonB = (coordinates[1]*cmath.pi)/180

            distance = R*cmath.acos(cmath.sin(latA)*cmath.sin(latB) + cmath.cos(latA)*cmath.cos(latB)*cmath.cos(lonA-cmath.cos(lonB)))
        
            if float(distance.real) <=distanceMax and now.year - year < yearsAgo:
                validRows.append(row)

    return validRows

print ("START")
events=Extract(pathFile = "ConflictData.csv",coordinatesPoint = [32.1736,36.1940],distanceMax=100,yearsAgo=10)
for event in events:
    print("------------")
    print(event)
    print("------------")

print("END")