"""this function finds all the fibonacci numbers below 
the max peram, appends them to a list, prints them, and tells
you the time it took to run the program"""

from time import *

start=clock()

def fib_list(max):
	x, y, list=0, 1, []
	while x < max:
		list, x, y = list+[x], x+y, x
	return list
print(fib_list(400000), "\nTime: {}".format(clock()-start))
