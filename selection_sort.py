### Selection Sort ###
## Author: D3f2lt ##
#Algorithm:
#1)Loop through the list. Assume the first element is the smallest item
#2)Take this assumption and loop through the elements to sort
#3)If L[j] < smallest_element, swap the items
#4)then repaet till you reach the end of the list


import time # for calculating time required to insturct computer

def selection_sort(L):
    """L is a list"""
    len_list = len(L)
    for i in range(0, len_list-1):
        minIndex = i
        for j in range(i+1, len_list):
            if L[j] < L[minIndex]:
                minIndex = j
        if minIndex != i:
            L[i], L[minIndex] = L[minIndex], L[i]
    return L[:]

##t0=time.time()
##L = [4,9,7,1,3,6,5]
####L = [1,3,5,4,2,6]
##print 'before', L
##print selection_sort(L)
##t1=time.time()
##print 'Selecetion sort time required: ', t1-t0
