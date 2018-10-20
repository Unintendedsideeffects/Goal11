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
            distance = R*cmath.acos(cmath.sin(coordinatesPoint[0])*cmath.sin(coordinates[0]) + cmath.cos(coordinatesPoint[0])*cmath.cos(coordinates[0])*cmath.cos(coordinatesPoint[1]-cmath.cos(coordinates[1])))
        
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