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

print()

class Baterai():
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga
        self.laku = int(input("Berapa jumlah baterai yang anda beli : "))
        
    def tampil(self):
        print(f"Baterai Merk {self.merk} dengan harga Rp. {self.harga} dibeli sebanyak {self.laku} biji")
        pembayaran = self.laku*self.harga
        bayar = print("Anda harus membayar sebanyak Rp. {}".format(pembayaran))

baterai_terjual = Baterai("Energizer", 20000)

baterai_terjual.tampil()
