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

print(parkFields)
print(parkRows)
print(speciesFields)
print(speciesRows[:100])
