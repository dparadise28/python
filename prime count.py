from math import *

def prime(upto):
    count, psum, x, y=0, 2, 1, 2
    while y!=upto:
        y+=1
        count=0
    
        for i in range(2,ceil(sqrt(y))+1):
            if y%i==0:
                count+=1
                break

        if count==0:
            x+=1
            psum+=y

    return psum

a=int(input("What number would you like to go up to: "))
print("the sum of all the prime numbers upto and including {0} is {1}".format(a, prime(a)))
