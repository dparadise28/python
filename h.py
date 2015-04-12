import pickle
#slopes and yint's of the lines of a cube
slope_yint={'0':[-1/4,5], '1':[-1/4,-5], '2':[-1/4,3], '3':[-1/4,-7],
            '4':[9.75,55], '5':[9.75,33.7], '6':[9.75,-46], '7':[9.75,-68],
            '8':[-1.3,-11.3], '9':[-1.3,-.16], '10':[-1.3,-.58],
            '11':[-1.3,10.38]}
#intervals under which to graph the slopes and yint's
interval={'0':[-5,5], '1':[-6,4], '2':[-3,7], '3':[-4,6], '4':[-6,-5.05],
          '5':[-4.07,-3.07], '6':[4.1,5], '7':[6.1,7.05], '8':[-5.9,-4.08],
          '9':[-4.9,-3.05], '10':[4.07,6.05], '11':[5.15,7.1]}
#dictionaries appended to a list for pickling
lines_domains=[slope_yint,interval]
cubepickle=open('cube.p','wb')
pickle.dump(lines_domains,cubepickle)
cubepickle.close()

from turtle import *
from random import *
from pickle import *
from math import *
setworldcoordinates(-7,-9,9,7)
pencolor('darkblue')
bgcolor("darkred")
pensize(2)
"""This function graphs the lines of a cube using the slope,
y-intercept, and interval specified"""
def cube_graph(m,b,start,stop):
    pu(); goto(start, m*start+b); pd()
    while start < stop:
        start+=0.1
        goto(start, m*start+b)
#this function graphs a function in the cube
def rand_f(start,stop):
    y=uniform(0,1)*sin(3*start)/start+uniform(0,start-1)*cos(2*start)
    pu(); goto(start, y); pd()
    while start < stop:
        start+=0.09
        y=uniform(0,start)*sin(3*start)/start+uniform(0,start-1)*cos(2*start)
        goto(start, y)
#extract's dict's from the file
infile=open("cube.p","rb")
y=load(infile)
#assigns the variables the respective object in the extracted list 
slope_yint=y[0]
interval=y[1]
#loops through both dictionaries and graphs the lines of the cube
for m_b_i,(function,inter) in enumerate(zip(slope_yint,interval)):
    slope=slope_yint[function][0]
    yint=slope_yint[function][1]
    start=interval[inter][0]
    stop=interval[inter][1]
    
    cube_graph(slope,yint,start,stop)
bgcolor("black")
pencolor('red')
rand_f(-5,6)
