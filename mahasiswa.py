# Lengkapi class di bawah ini.
# Baca README.md untuk aturannya.


class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.nilai = []

    # buat method init yg menerima 1 parameter, nama
    # buat juga daftar nilai kosong, lalu simpan ke variable self.nilai

    def tambah_nilai(self, n):
        self.nilai.append(n)

        # masukkan n ke daftar nilai

    def jumlah_nilai(self):
        hitung = 0
        for i in self.nilai:
            hitung += 1
        return hitung
        
        # berapa banyak nilai yang sudah masuk
        # dilarang menggunakan len()

    def rata_rata(self):
        if not self.nilai:
             return 0
        total = 0
        for n in self.nilai:
            total += n
        return total / self.jumlah_nilai()

        # daftar kosong harus mengembalikan 0, bukan error

    def tertinggi(self):
        if not self.nilai:
            return None
        tertinggi = self.nilai[0]
        for n in self.nilai:
            if n > tertinggi:
                tertinggi = n
        return tertinggi

        # daftar kosong harus mengembalikan None
        # dilarang memakai max()

    def lulus(self):
        return self.rata_rata() >= 60

        # True kalau rata-rata 60 ke atas

    def __str__(self):
        return self.nama + " (" + str(self.jumlah_nilai()) + " nilai)"
        
        # contoh: "Budi (3 nilai)"