import csv
import distance

pathFile = "Settlements.csv"

def extractSettlements (coordinatesPoint, radius):
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        coordinates = []
        validRows = []

        for row in csv_reader:
            coordinates = [float(row["LAT"]),float(row["LONG"])]
            if distance.distance(coordinatesPoint,coordinates,radius):
                validRows.append(row)

    return validRows

def extractSettlementsNames(coordinatesPoint, radius):
    names = []
    rows = extractSettlements(coordinatesPoint, radius)
    for row in rows:
        names.append(row['NAME'])
    return names

def getNearest(coordinatesPoint):
    nearest = None
    minDist = -1

    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        coordinates = []

        for row in csv_reader:
            coordinates = [float(row["LAT"]),float(row["LONG"])]
            dist = distance.distance(coordinatesPoint,coordinates)
            if minDist==-1:
                minDist = dist
                nearest = row
            elif dist<minDist:
                minDist= dist
                nearest = row

    return nearest

def getSettlementsByName(name):
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        for row in csv_reader:
            if row["NAME"] == name:
                return row
                
def getCoordinatesByName(name):
    # Just take the first one, no reason for duplicates
    row = getSettlementsByName(name)
    return  [float(row["LAT"]),float(row["LONG"])]



def getSettlementsByPcode(Pcode):
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        for row in csv_reader:
            if row["ï»¿PCode"] == Pcode:
                return row

#rows = extractSettlements([-4.764447,13.614718],150)
#for row in rows:
#    print(row["NAME"])

#getSettlementsByName("Madimba")
#getSettlementsByPcode("CG010100015")
#getNearest([-4.764447,13.614718])