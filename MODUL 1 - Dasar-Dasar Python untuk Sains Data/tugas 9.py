from datetime import datetime


class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_informasi(self):
        return f"Judul       : {self.judul}\nPenulis     : {self.penulis}\nTahun Terbit: {self.tahun_terbit}"

    def hitung_usia(self):
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - self.tahun_terbit
        return usia


buku1 = Buku("Data Science for Dummies", "Lorraine Daston", 2015)
buku2 = Buku("Python Programming", "John Doe", 2017)
buku3 = Buku("Data Science for Dummies", "Lorraine Daston", 2015)

for buku in [buku1, buku2, buku3]:
    print(buku.tampilkan_informasi())
    print(f"Usia buku   : {buku.hitung_usia()} tahun")
    print("-" * 40)
