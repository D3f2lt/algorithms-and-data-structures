### Bubble Sort ###
## Author: D3f2lt ##

import time

def bubble_sort(L):
    """L is a list of items"""
    for i in range (len(L)-1):
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L[:]

##t0=time.time()
##L = [4,9,7,1,3,6,5]
##print bubble_sort(L)
##t1=time.time()
##print 'Bubble sort time required:', t1-t0
