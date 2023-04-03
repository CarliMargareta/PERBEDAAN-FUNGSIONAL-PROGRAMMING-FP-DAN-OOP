# buat class mobil
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def tampil_mobil(self):
        print("Mobil merk", self.merk, "warna", self.warna)

# buat objek dari class Mobil
mobil1 = Mobil("Toyota", "Hitam")
mobil1.tampil_mobil()