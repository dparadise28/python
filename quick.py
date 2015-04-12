import random
import time

def quickSort(alist):
    #We include some timing
    start = time.clock()
    quickSortHelper(alist,0,len(alist)-1)
    end = time.clock()
    return end-start

def quickSortHelper(alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
                alist[leftmark] < pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] > pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark]= \
                         alist[rightmark],alist[leftmark]

    alist[first],alist[rightmark]= \
                   alist[rightmark],alist[first]

    return rightmark
while(True):
    k = int(raw_input("Enter list size(-1 to break) "))
    if k == -1:
        break
        
    x = random.sample(range(10000000),k)

    print quickSort(x)





