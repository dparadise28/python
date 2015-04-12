import cmath
'''cmath is The special math package for complex numbers
   the symbol j stands for the sqrt(-1) (i.e. i)
'''
# Discrete fourier transform
def dft(x):
    t = []
    N = len(x)
    for k in range(N):
        a = 0
        for n in range(N):
            a += x[n]*cmath.exp(-2j*cmath.pi*k*n*(1/N))
        t.append(a)
    return t
# Inverse discrete fourier transform
def idft(t):
    x = []
    N = len(t)
    for n in range(N):
        a = 0
        for k in range(N):
            a += t[k]*cmath.exp(2j*cmath.pi*k*n*(1/N))
        a /= N
        x.append(a)
    return x

def f(x):
   y= cmath.sin(.2*x)+ cmath.sin(.3*x)
   return y

