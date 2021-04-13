import time
import pygame
import sort



#Melakukan Setinggan py game mengatur warna dan dimensi
dimensions = [1024, 512]
pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color(255,255,255))

#init untuk mendapatkan instace dari class 
def init(item):
    quicksort = sort.QuickSort(item)
    return quicksort

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

#Update Tampilan, fungsi ini dipanggil dari dalam class QuickSort yang diimport.
def update(quicksort, element1=None, element2=None, display=display): 
    display.fill(pygame.Color(255,255,255))
    pygame.display.set_caption("Tampilan QuickSort | Time: {:.3f}  | Status: Sorting...".format(time.time() - quicksort.startTime))
    k = int(dimensions[0]/len(quicksort.item))
    for i in range(len(quicksort.item)):
        colour = (84, 209, 167)
        if element1 == quicksort.item[i]:
            colour = (207,73,66)
        elif element2 == quicksort.item[i]:
            colour = (25,19,209)
        left = i*k
        tinggi = dimensions[1] - quicksort.item[i]
        pygame.draw.line(surface = display, color= colour, start_pos=(left,dimensions[1]), end_pos=(left,tinggi),width=k)
    checkQuit()
    pygame.display.update()     

def tetapTerbuka(display, waktuEksekusi):
    pygame.display.set_caption("Tampilan QuickSort | Time: {:.3f}  |  Status: Done!".format(waktuEksekusi))
    while True:
        checkQuit()
        pygame.display.update()

def main(item):
    try:
        quicksort = init(item)
        waktuEksekusi = quicksort.mulai(0, len(quicksort.item))[1]
        tetapTerbuka(display, waktuEksekusi)
        return None
    except:
        pass
    

