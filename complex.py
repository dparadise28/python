import math

class Complex:
    def __init__(self,real,imag):
    	self.r=real
    	self.i=imag

    def __repr__(self):
        if self.i!=0 and self.r!=0:
            if self.i>0 and self.i!=1:
                return('%r+%ri')%(self.r,self.i)
            if self.i<0 and self.i!=-1:
                return('%r%ri')%(self.r,self.i)
            if self.i==1:
                return('%r+i')%(self.r)
            if self.i==-1:
                return('%r-i')%(self.r)
        elif self.i==self.r==0:
            return('0')
        elif self.i==0:
            return('%r')%(self.r)
        elif self.r==0:
            if self.i==1:
                return('i')
            else:
                return('%ri')%(self.i)
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        return Complex(-self.r,-self.i)

    def __eq__(self,x):
        if self.r==x.r and self.i==x.r:
            return True
        else:
            return False

    def __add__(self,x):
        new=Complex(self.r+x.r,self.i+x.i)
        return new
        
    def __sub__(self,x):
        return self+(-x)

    def __mul__(self,x):
        return Complex(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)

    def abs(self):
        return float(math.sqrt(self.r**2+self.i**2))

    def div(self,x):
        re=(self.r*x.r+self.i*x.i)/(Complex.abs(x)**2)
        im=(self.r*x.i-self.i*x.r)/(Complex.abs(x)**2)

        return Complex(re,im)

    def conjugate(self):
        return Complex(self.r,-self.i)

    def real(self):
        return self.r

    def imag(self):
        return self.i

    def theta(self):
        return math.atan(self.i*1.0/self.r)

    def r(self):
        return Complex.abs(self)

    def pow(self,power):
        r=Complex.r(self)
        theta=Complex.theta(self)

        return Complex(r**power*math.cos(8*theta),r**power*math.cos(8*theta))

    def reciprocal(self):
        Self=Complex.conjugate(self)
        re=Self.r/(Complex.abs(self)**2)
        im=Self.i/(Complex.abs(self)**2)
        
        return Complex(re,im)
