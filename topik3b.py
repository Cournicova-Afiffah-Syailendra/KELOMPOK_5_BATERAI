import csv

baterai = []

with open('baterai.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        baterai.append(row)

print(baterai)