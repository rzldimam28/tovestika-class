# Lengkapi class di bawah ini.
# Baca README.md untuk aturannya.


class Mahasiswa:
    def __init__(self, nama) :
        self.nama = nama 
        self.nilai = []


    def tambah_nilai(self, n):
        self.nilai.append(n)


    def jumlah_nilai(self):
        jumlah = 0
        for n in self.nilai:
            jumlah += 1
        return jumlah


    def rata_rata(self):
        if self.jumlah_nilai() == 0:
            return 0
        total = 0
        for n in self.nilai:
            total += n
        return total / self.jumlah_nilai()

    
    def tertinggi(self):
        if self.jumlah_nilai() == 0:
            return None
        teratas = self.nilai [0]
        for n in self.nilai:
            if n > teratas:
                teratas = n
        return teratas

     
    def lulus(self):
        return self.rata_rata() >= 60


    def __str__(self):
        return self.nama + " (" + str (self.jumlah_nilai())+ " nilai)"