def ganti(item, kiri, kanan):
    #Menggant elemet di list[i], list[j] = list[j], list[i]
    item[kiri], item[kanan] = item[kanan], item[kiri]
    return None

def partisi(item, kiri, kanan):
    titikTengah = item[(kiri + kanan) // 2]
    print('Acuan Kiri' , kiri)
    print('Acuan Kanan', kanan)
    print('Titik Tengah/Acuan ', titikTengah )
    i = kiri
    j = kanan - 1
    while(i < j):
        while(item[i] < titikTengah):
            i+= 1
        while(item[j] > titikTengah):
            j-= 1
        
        if(i < j):
            ganti(item, i, j)
    return i

def quickSort(item, kiri, kanan):
    key = partisi(item, kiri, kanan)
    print(item)
    if(key > kiri):
        quickSort(item, kiri, key)
    if(key + 1 < kanan ):
        quickSort(item, key + 1, kanan)
    return item

testList = [5,3,7,6,2,9]
quickSort(testList, 0, len(testList))