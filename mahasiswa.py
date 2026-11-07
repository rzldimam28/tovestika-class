class Mahasiswa:

    def __init__(self, nama):
        self.nama = nama
        self.nilai = []

    def tambah_nilai(self, n):
        self.nilai.append(n)

    def jumlah_nilai(self):
        hitung = 0
        for _ in self.nilai:
            hitung = hitung + 1
        return hitung

    def rata_rata(self):
        if self.jumlah_nilai() == 0:
            return 0
        return sum(self.nilai) / self.jumlah_nilai()

    def tertinggi(self):
        if self.jumlah_nilai() == 0:
            return None
        paling_besar = self.nilai[0]
        for n in self.nilai:
            if n > paling_besar:
                paling_besar = n
        return paling_besar

    def lulus(self):
        return self.rata_rata() >= 60

    def __str__(self):
        return self.nama + " (" + str(self.jumlah_nilai()) + " nilai)"