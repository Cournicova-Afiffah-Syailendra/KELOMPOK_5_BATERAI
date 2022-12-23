class Baterai():
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga
        self.laku = int(input("Berapa jumlah baterai yang anda beli :"))
    def tampil(self):
        print(f"Baterai Merk {self.merk} dengan harga Rp. {self.harga} terjual {self.laku} biji")

baterai_terjual = Baterai("Versi ABC", 13000)

baterai_terjual.tampil()