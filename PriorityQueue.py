class PriorityQueue:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i > 0:
            if self.heapList[i] < self.heapList[i/2]:
               tmp = self.heapList[i/2]
               self.heapList[i/2] = self.heapList[i]
               self.heapList[i] = tmp
            i = i/2
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)            

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            child = i * 2
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc


    def minChild(self,i):
        if i*2 > self.currentSize:
            return -1
        else:
            if i*2 + 1 > self.currentSize:
                return i*2
            else:
                if self.heapList[i*2] < self.heapList[i*2+1]:
                    return i*2
                else:
                    return i*2+1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.percDown(1)
        return retval
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1




'''
#test1
pq = PriorityQueue()

choice = 1
while (not choice ==0):
 if (not choice == 0):
    x = input("Enter a number:  ")
    pq.insert(x)
    choice = input("More ???    ")
              

while(pq.currentSize > 0):
      x = pq.delMin()
      print( x)

#test 2

L = ['45','smith','gold','JunK','aardvark']

pq = PriorityQueue()

pq.buildHeap(L)

while(pq.currentSize > 0):
      x = pq.delMin()
      print( x)
'''

