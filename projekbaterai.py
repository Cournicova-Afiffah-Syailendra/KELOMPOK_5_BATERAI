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


from tkinter import *

root = Tk()
root.title("Perhitungan Pada Baterai")
root.config(background="lightyellow")

l1 = Label(text="Pilih Salah Satu", bg="lightyellow", font="Normal 25")
l1.grid(row=0, column=0,columnspan=4, padx=20, pady=30)

pilihan = 0

def Harga():
    global pilihan
    pilihan = 1
    l2.config(text="Harga Baterai")
    l3.config(text="Jumlah Beli")
    l4.config(text="X")
    l5.config(text="Anda Harus Membayar Sebanyak :")
    l6.config(text="")

def Kapasitas():
    global pilihan
    pilihan = 2
    l2.config(text="Kuat Arus (Ah)")
    l3.config(text="Tegangan (Volt)")
    l4.config(text="X")
    l5.config(text="Kapasitas baterai anda adalah :")
    l6.config(text="")

def Arus():
    global pilihan
    pilihan = 2
    l2.config(text="Daya (Watt)")
    l3.config(text="Tegangan (Volt)")
    l4.config(text="/")
    l5.config(text="Kuat Arus Baterai anda adalah :")
    l6.config(text="")

def total():
    global pilihan
    if pilihan == 1:
        rumus = int(e1.get()) * int(e2.get())
        l6.config(text="Rp.{}".format(rumus))
    if pilihan == 2:
        rumus = int(e1.get()) * int(e2.get())
        l6.config(text="{} Wh".format(rumus))
    if pilihan == 2:
        rumus = int(e1.get()) / int(e2.get())
        l6.config(text="{} Ampere".format(rumus))

    e1.delete(0, END)
    e2.delete(0, END)


b1 = Button(text="Harga Total", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=10, command=Harga)
b1.grid(row=1, column=0)

b2 = Button(text="Kapasitas", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=10, command=Kapasitas)
b2.grid(row=1, column=1, columnspan=2)

b3 = Button(text="Arus", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", width=10, command=Arus)
b3.grid(row=1, column=3)

l2 = Label(text="", bg="lightyellow", font="Normal 15")
l2.grid(row=2, column=0, pady=(40,0))

l3 = Label(text="", bg="lightyellow", font="Normal 15")
l3.grid(row=2, column=2, pady=(40,0))

e1 = Entry(bd=5, relief=RIDGE, font="Normal 15", width=10)
e1.grid(row=3, column=0)

l4 = Label(text=" ", font="Normal 15", bg="lightyellow")
l4.grid(row=3, column=1)

e2 = Entry(bd=5, relief=RIDGE, font="Normal 15", width=10)
e2.grid(row=3, column=2)


b4 = Button(text="Hitung", activebackground="lightblue", bd=5, relief=RIDGE, font="Normal 15", command=total)
b4.grid(row=3, column=3)

l5 = Label(text=" ", font="Normal 20", bg="lightyellow")
l5.grid(row=4, column=0, columnspan=4, pady=40)

l6 = Label(text=" ", font="Normal 20", bg="lightyellow")
l6.grid(row=5, column=0, columnspan=4, pady=10, padx=10)
root.mainloop()


class Baterai():
    def __init__(self, merk, harga, ukuran, jumlah, bentuk, kapasitas):
        self.merk = merk
        self.harga = harga
        self.ukuran = ukuran
        self.jumlah = jumlah
        self.bentuk = bentuk
        self.kapasitas = kapasitas
        
    def tampil(self):
        print(f"Baterai Merk {self.merk} dengan harga Rp. {self.harga} dibeli sebanyak {self.jumlah} buah")
        pembayaran = self.harga * self.jumlah
        bayar = print("Anda harus membayar sebanyak Rp. {}".format(pembayaran))

bat1 = Baterai("Energizer", 20000, "AA", 2, "Tabung", 2000)
bat2 = Baterai("ABC", 13000, "AA", 3, "Tabung", 10000)
bat1.tampil()
bat2.tampil()