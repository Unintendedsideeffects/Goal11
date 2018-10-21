import csv
import distance

def extractSettlements (pathFile, coordinatesPoint, radius):
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        coordinates = []
        validRows = []

        for row in csv_reader:
            coordinates = [float(row["LAT"]),float(row["LONG"])]
            if distance.distance(coordinatesPoint,coordinates,radius):
                validRows.append(row)

    return validRows
                
def getSettlementsByName(pathFile, name):
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        for row in csv_reader:
            if row["NAME"] == name:
                return row

def getSettlementsByPcode(pathFile, Pcode):
    with open(pathFile) as csv_file:

        csv_reader = csv.DictReader(csv_file, delimiter = ",")

        for row in csv_reader:
            if row["NAME"] == name:
                return row



#rows = extractSettlements("Settlements.csv", [-4.764447,13.614718],50)
#print(rows)

getSettlementsByName("Settlements.csv","Madimba")