import numpy as np
ask = True
def ganti(item, kiri, kanan):
    #Menggant elemet di list[i], list[j] = list[j], list[i]
    item[kiri], item[kanan] = item[kanan], item[kiri]
    return None

def partisi(item, kiri, kanan):
    i = kiri
    j = kanan
    titikTengah = item[(kiri + kanan) // 2]
    print('Elemet Kiri ', item[i])
    print('ElementKanan', item[j])
    print('Pembanding', titikTengah)
    print('Nilai i ', item[i])
    print('Nilai j', item[j])
    while i <= j:
        while item[i] < titikTengah:
            i+= 1
        while item[j] > titikTengah:
            j-= 1
        if(i <= j):
            ganti(item, i, j)
            i+= 1
            j-= 1
    return i

def quickSort(item, kiri, kanan):
    if(len(item) > 1):
        key = partisi(item, kiri, kanan)
        print(item)
        if(key - 1 > kiri ):
            quickSort(item, kiri, key - 1)
        if(key < kanan ):
            quickSort(item, key  , kanan)
    return item

def acceptUserInput():
    unsortedList = []
    print('Silahkan masukan panjang array/list Saudara')
    listLength = input('Minimal 3 .. / Jika ingin keluar silahkan tulis q..')
    if listLength == 'q' or listLength == 'Q':
        quit()
    listLength = int(listLength)
    if listLength < 3:
        print('Minimal data yang harus dimasukan adalah 3')
        return acceptUserInput()
    print('Apakah Saudara ingin List Random dari kami ? (Y/N)')
    askUser = True
    while askUser:
        jawabanUser = input('Y/N..?')
        if(jawabanUser == 'Y' or jawabanUser =='y'):
            unsortedList = list(np.random.randint(100, size= listLength))
            print('====================\n',unsortedList,'\n====================\n')
            quickSort(unsortedList, 0, len(unsortedList) - 1)
            print('====================\n',unsortedList,'\n====================\n')
            unsortedList = []
            askUser = False
        elif(jawabanUser == 'N' or jawabanUser == 'n'):
            askAngka = True
            while askAngka:
                for x in range(listLength):
                    try:
                        print('Silahkan masukan angka yang ', x + 1)
                        angka = int(input())
                        if angka == None:
                            raise ValueError
                        unsortedList.insert(len(unsortedList), angka)
                        askUser = False
                        askAngka = False
                    except ValueError:
                        print('Data yang Saudara masukan salah, silahkan ulang \n')
                        acceptUserInput()
                print('====================\n',unsortedList,'\n====================\n')
                quickSort(unsortedList, 0, len(unsortedList) - 1)
                print('====================\n',unsortedList,'\n====================\n')
                unsortedList = []

while ask:
    acceptUserInput()
    
    
# testList = [42,9,23,8,2,6,5,1,14,39,17,29,28,32,41,5]

# quickSort(testList, 0, len(testList))