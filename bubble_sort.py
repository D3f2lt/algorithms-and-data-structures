"""
       Author: PyDev
       Description: Bubble Sort implementation
"""
def bubble_sort(list_object):
    """as the name implies list_object: is a list object"""
    swap = False
    while not swap:
        swap = True
        for index in range(1, len(list_object)):
            if list_object[index-1] > list_object[index]:
                swap = False
                list_object[index], list_object[index-1] = list_object[index-1], list_object[index]
    
    return list_object

if __name__ == "__main__":
    ls = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print ("after sorting", bubble_sort(ls))