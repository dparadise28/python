import random
import time
def qsort1(list):
    """
    Quicksort using list comprehensions
    >>> qsort1<<docstring test numeric input>>
    <<docstring test numeric output>>
    >>> qsort1<<docstring test string input>>
    <<docstring test string output>>
    """
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater


size = int(input("Enter the list size "))

x=random.sample(range(100000),size)
#I used this code instead to implement the array copying
# y = x[:] did not seem to work
y =[]
y.extend(x)

start = time.clock()
qsort1(x)
end = time.clock()
print("qsort1 time ",end-start)

start = time.clock()
y.sort()
end = time.clock()
print( "qsort of python time ",end-start)

