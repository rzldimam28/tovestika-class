# Lengkapi class di bawah ini.
# Baca README.md untuk aturannya.


# class Mahasiswa:

    # buat method init yg menerima 1 parameter, nama
    # buat juga daftar nilai kosong, lalu simpan ke variable self.nilai

class Mahasiswa:
    def __init__(self, nama) :
        self.nama = nama
        self.nilai = []

    def tambah_nilai(self, n):
        # masukkan n ke daftar nilai
        self.nilai.append(n)
        

    def jumlah_nilai(self):
        # berapa banyak nilai yang sudah masuk
        # dilarang menggunakan len()
        jumlah = 0
        for n in self.nilai:
            jumlah += 1
        return jumlah

    def rata_rata(self):
        # daftar kosong harus mengembalikan 0, bukan error
        if self.jumlah_nilai() == 0 :
            return 0
        total = 0
        for n in self.nilai :
            total += n
        return total / self.jumlah_nilai()
    

    def tertinggi(self):
        # daftar kosong harus mengembalikan None
        # dilarang memakai max()
        if self.jumlah_nilai() == 0:
            return None
        paling_tinggi = self.nilai [0]
        for n in self.nilai:
            if n > paling_tinggi:
                paling_tinggi = n
        return paling_tinggi
        

    def lulus(self):
        # True kalau rata-rata 60 ke atas
        return self.rata_rata() >= 60

    def __str__(self):
        # contoh: "Budi (3 nilai)"
        return self.nama + " (" + str (self.jumlah_nilai())+ " nilai)"