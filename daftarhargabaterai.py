import csv

baterai = []

with open('baterai.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        baterai.append(row)

labels = baterai.pop(0)
print(f'{labels[0]} \t {labels[1]} \t\t {labels[2]} \t {labels[3]}')
print("-"*70)
for data in baterai:
    print(f'{data[0]} \t {data[1]} \t {data[2]} \t\t{data[3]}')