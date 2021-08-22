import numpy as np
import csv
import pickle

parks = "parks.csv"
species = "species.csv"

parkRows = {}
with open(parks, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    parkFields = next(csvreader)

    for row in csvreader:
        # {CODE: [everything else]}
        parkRows[row[0]] = row[1:]
        # row format: [CODE, NAME, STATE, SIZE(ACRES), LONGITUDE, LATITUDE]

speciesRows = []
parkAnimals = {}
with open(species, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    speciesFields = next(csvreader)

    for row in csvreader:
        speciesRows.append(row)
        # row format: [CODE, PARK NAME, CATEGORY, ORDER, FAMILY, SCIENTIFIC NAME, COMMON NAME, 
        # RECORD STATUS, OCCURENCE, NATIVENESS, ABUNDANCE, SEASONALITY, CONSERVATION STATUS]

# print(parkFields)
# print(parkRows)
# print(speciesFields)
# print(speciesRows[:100])

#rows of species of concern and endangered species
concernIdxs = [i for i, row in enumerate(speciesRows) if row[12] == "Species of Concern"]
# print(concernIdxs)
concernRows = [speciesRows[i] for i in concernIdxs]
# print(concernRows)

endangeredIdxs = [i for i, row in enumerate(speciesRows) if row[12] == "Endangered"]
# print(endangeredIdxs[:20])
endangeredRows = [speciesRows[i] for i in endangeredIdxs]
# print(endangeredRows[:20])
print(len(concernRows))
print(len(endangeredRows))

#State: [animal, status]
database = {}
for row in concernRows:
    code = row[0][:4]
    state = parkRows[code][1]
    info = row[2:7]
    info.append("Species of Concern")
    if state not in database:
        database[state] = info
    else:
        database[state].append(info)

for row in endangeredRows:
    code = row[0][:4]
    state = parkRows[code][1]
    info = row[2:7]
    info.append("Endangered")
    if state not in database:
        database[state] = info
    else:
        database[state].append(info)

#print(database["CA"][:20])
# database organized by state, len 27
print(len(database))
