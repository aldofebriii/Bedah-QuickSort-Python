import time
class QuickSort():
    #Kelas untuk memulai
    def __init__(self, item):
        self.item = item
    
    #Update tampilan, import didalam fungsi biar tidak terjadi cycling
    def updateTampilan(self, element1, element2):
        import tampilan
        tampilan.update(self, element1, element2)

    #Mulai
    def mulai(self, kiri, kanan):
        self.startTime = time.time()
        self.algoritma(kiri, kanan - 1)
        waktuEksekusi = time.time() - self.startTime
        return self.item, waktuEksekusi

    #Swap elemen i dengan elemen J
    def ganti(self,kiri, kanan):
        #Menggant elemet di list[i], list[j] = list[j], list[i]
        self.item[kiri], self.item[kanan] = self.item[kanan], self.item[kiri]
        self.updateTampilan(self.item[kiri], self.item[kanan])
        return None
    #Partisi Element, untuk mendapatkan titik tengah

    def partisi(self, kiri, kanan):
        i = kiri
        j = kanan
        titikTengah = self.item[(kiri + kanan) // 2]
        print('--------------\n')
        print('Element Kiri ', self.item[i])
        print('ElementKanan', self.item[j])
        print('Pembanding', titikTengah)
        print('Nilai i ', self.item[i])
        print('Nilai j', self.item[j])
        while i <= j:
            while self.item[i] < titikTengah:
                i+= 1
            while self.item[j] > titikTengah:
                j-= 1
            if(i <= j):
                self.ganti(i, j)
                i+= 1
                j-= 1
        return i

    #Membagi Element menjadi 2 terus menurus
    def algoritma(self, kiri, kanan):
        if(len(self.item) > 1):
            key = self.partisi(kiri, kanan)
        print(self.item)
        if(key - 1 > kiri ):
            self.algoritma(kiri, key - 1)
        if(key < kanan ):
            self.algoritma(key, kanan)
    
    
class PureQuickSort(QuickSort):
    def __init__(self, item):
        super().__init__(item)

    def mulai(self, kiri, kanan):
        self.startTime = time.time()
        self.algoritma(kiri, kanan - 1)
        waktuEksekusi = time.time() - self.startTime
        return self.item, waktuEksekusi

    def partisi(self, kiri, kanan):
        i = kiri
        j = kanan
        titikTengah = self.item[(kiri + kanan) // 2]
        print('--------------\n')
        print('Element Kiri ', self.item[i])
        print('ElementKanan', self.item[j])
        print('Pembanding', titikTengah)
        print('Nilai i ', self.item[i])
        print('Nilai j', self.item[j])
        while i <= j:
            while self.item[i] < titikTengah:
                i+= 1
            while self.item[j] > titikTengah:
                j-= 1
            if(i <= j):
                self.ganti(i, j)
                i+= 1
                j-= 1
        return i
    def ganti(self,kiri, kanan):
        #Menggant elemet di list[i], list[j] = list[j], list[i]
        self.item[kiri], self.item[kanan] = self.item[kanan], self.item[kiri]
        return None

    def algoritma(self, kiri, kanan):
        if(len(self.item) > 1):
            key = self.partisi(kiri, kanan)
        print(self.item)
        if(key - 1 > kiri ):
            self.algoritma(kiri, key - 1)
        if(key < kanan ):
            self.algoritma(key, kanan)
