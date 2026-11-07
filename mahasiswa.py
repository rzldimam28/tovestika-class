# Lengkapi class di bawah ini.
# Baca README.md untuk aturannya.


class Mahasiswa:
    def __init__(self, nama) :
        self.nama = nama 
        self.nilai = []
        
    # buat method init yg menerima 1 parameter, nama
    # buat juga daftar nilai kosong, lalu simpan ke variable self.nilai

    def tambah_nilai(self, n):
        self.nilai.append(n)
        # masukkan n ke daftar nilai
        

    def jumlah_nilai(self):
        jumlah = 0
        for n in self.nilai:
            jumlah += 1
        return jumlah
        # berapa banyak nilai yang sudah masuk
        # dilarang menggunakan len()

    def rata_rata(self):
        # daftar kosong harus mengembalikan 0, bukan error
        if self.jumlah_nilai() == 0:
            return 0 
        total = 0
        for n in self.nilai:
            total += n
        return total / self.jumlah_nilai()

    def tertinggi(self):
        # daftar kosong harus mengembalikan None
        # dilarang memakai max()
        if self.jumlah_nilai() == 0:
            return None
        nilai_tertinggi = self.nilai [0]
        for n in self.nilai:
            if n > nilai_tertinggi:
                nilai_tertinggi = n 
        return nilai_tertinggi

    def lulus(self):
        # True kalau rata-rata 60 ke atas
        return self.rata_rata() >= 60

    def __str__(self):
        # contoh: "Budi (3 nilai)"
        return self.nama + " (" + str (self.jumlah_nilai())+ " nilai)"