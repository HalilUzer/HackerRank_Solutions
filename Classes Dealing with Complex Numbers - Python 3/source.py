

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        result = Complex(self.real + no.real, self.imaginary + no.imaginary)
        return result
        
        
        
    def __sub__(self, no):
        result = Complex(self.real - no.real, self.imaginary - no.imaginary)
        return result
        
        
    def __mul__(self, no):
        real = (self.real * no.real) - (self.imaginary * no.imaginary) 
        imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        result = Complex(real, imaginary)
        return result
        
        

    def __truediv__(self, no):
        x=no.real**2+no.imaginary**2
        a=(self.real*no.real+self.imaginary*no.imaginary)/x
        b=(-no.imaginary*self.real+self.imaginary*no.real)/x
        return Complex(a, b)

    def mod(self):
        result = Complex(math.sqrt((self.real ** 2) + (self.imaginary ** 2)), 0)
        return result
        

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

