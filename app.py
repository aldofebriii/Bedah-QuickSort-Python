import numpy as np

#Status Bertanya
ask = True

#Menerima User Input
def acceptUserInput():
    #Init Unsorted List
    unsortedList = []
    try:
        print('Silahkan masukan panjang array/list Saudara')
        listLength = input('Angka Minimal 3 .. / Jika ingin keluar silahkan tulis q..')
        if listLength == 'q' or listLength == 'Q':
            global ask
            ask = False
            quit()
        listLength = int(listLength)
        if listLength < 3:
            print('Minimal data yang harus dimasukan adalah 3\n')
            return acceptUserInput()
        print('Apakah Saudara ingin List Random dari kami ? (Y/N)\n')
        askUser = True
        while askUser:
                jawabanUser = input('Y/N..?')
                if(jawabanUser == 'Y' or jawabanUser =='y'):
                    unsortedList = list(np.random.randint(512, size= listLength))
                    print('====================\n',unsortedList,'\n====================\n')
                    import tampilan
                    tampilan.main(unsortedList)
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
                        import tampilan
                        tampilan.main(unsortedList)
                        print('====================\n',unsortedList,'\n====================\n')
                        unsortedList = []
    except ValueError:
        acceptUserInput()

while ask:
    acceptUserInput()