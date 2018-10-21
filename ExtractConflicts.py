import csv
import cmath
import datetime
import distance


pathFile = "ConflictData.csv"

def extract(coordinatesPoint, distanceMax = 'default', yearsAgo = 'default'):
       
    if distanceMax == 'default':
        distanceMax = 50
    if yearsAgo == 'default':
        yearsAgo = 25
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        coordinates = []
        validRows = []
        now = datetime.datetime.now()

        for row in csv_reader:
            coordinates = [float(row["LATITUDE"]),float(row["LONGITUDE"])]
            year = int(row["YEAR"])

            if distance.distance(coordinatesPoint,coordinates,distanceMax) and now.year - year < yearsAgo:
                validRows.append(row)

    return validRows

def numberConflicts(coordinatesPoint, distanceMax = 'Default', yearsAgo = 'Default'):
    return len(extract(coordinatesPoint, distanceMax, yearsAgo))

# print ("START")
#print(numberConflicts(coordinatesPoint = [32.1736,36.1940],distanceMax=150,yearsAgo=10))
# for event in events:
#     print("------------")
#     print(event)
#     print("------------")

# print("END")
