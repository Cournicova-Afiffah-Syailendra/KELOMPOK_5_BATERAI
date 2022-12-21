import csv

with open('baterai.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    print(csv_reader)
    for row in csv_reader:
        print(row)
