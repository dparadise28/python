import random
import time
import string
#The string class is needed for the next function

def rword(k):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(k))



class HashTable:
    def __init__(self,size):
        self.slots = [None] * size
        self.data = [None] * size
    def store(self,item,data):
      
      hashvalue = self.hashfunction(item,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = item
        self.data[hashvalue] = data
      else:
        nextslot = self.rehash(hashvalue,len(self.slots))
        while self.slots[nextslot] != None:
          nextslot = self.rehash(nextslot,len(self.slots))

        self.slots[nextslot]=item
        self.data[nextslot]=data
       
       
    def search(self,item):
      start=time.clock()
      startslot = self.hashfunction(item,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == item:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      end=time.clock()
      return data,end-start
    #very useful overloaded get and set "magic" methods
    def __getitem__(self,item):
        return self.search(item)

    def __setitem__(self,item,data):
        self.store(item,data)
    #def hashfunction(self,item,size):
    #         return item%size
    def hashfunction(self,astring,size):
        sum = 0
        for pos in range(len(astring)):
            sum = sum + ord(astring[pos])

        return sum%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def __str__(self):
        print( self.slots)
        print (self.data)
 

H = HashTable(5591)

for i in range(1000):
     H[rword(5)]=rword(12)
