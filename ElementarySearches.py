# Elementary searching Prof. B.Shaw 10 7 13 Math 4320
import random,string
import time


def rword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
def sequentialSearch(alist, item):
    pos = 0
    found = False
    start= time.time()
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return found,end-start,pos
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    start= time.time()
    
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
                
    end = time.time()
    
    return found,end-start,midpoint
L = []
k = int(input('Enter the size of the words '))
n = int(input('Enter the list size '))

for i in range(n+1):
    L.append(rword(k))
    
x=L[random.randrange(0,n)]
print(x)

print(sequentialSearch(L,x))

L.sort()

print(binarySearch(L,x))


