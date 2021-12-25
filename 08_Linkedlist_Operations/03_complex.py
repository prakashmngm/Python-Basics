'''
a + ib ; a = real part, b = imag part

Create a class representing a complex number.
Write a method to print the complex number.

Addition and subtraction of complex numbers

Multiplication of Complex Nos : 
(x + y) * ( p + q ) = x * ( p+q)  + y * (p+q) 
                           = xp + xq + yp + yq

(a + ib) * ( x + iy) = ax + i(ay) + i(bx) + i2by
                           = (ax-by)   + i(ay+bx)


'''

class Complex:
    def __init__(self,real,imag):
        self.real_num = real
        self.imag_num = imag
    def printComplexNumber(self):
        print(str(self.real_num)+'+'+'i'+'('+str(self.imag_num)+')')
    def addition(self,c2):
        real3 = self.real_num+c2.real_num
        imag3 = self.imag_num+c2.imag_num
        c3 = Complex(real3,imag3)
        return c3
    def subtraction(self,c2):
        real3 = self.real_num-c2.real_num
        imag3 = self.imag_num-c2.imag_num
        c3 = Complex(real3,imag3)
        return c3
    def multiplication(self,c2):
        real3 = (self.real_num*c2.real_num)-(self.imag_num*c2.imag_num)
        imag3 = (self.real_num*c2.imag_num)+(self.imag_num*c2.real_num)
        c3 = Complex(real3,imag3)
        return c3
    
c1 = Complex(3,2)
c2 = Complex(4,5)
c3 = c1.addition(c2)
c4 = c1.subtraction(c2)
c3.printComplexNumber()
c4.printComplexNumber()
c5 = c3.addition(c4)
c5.printComplexNumber()
c6 = c1.multiplication(c2)
c6.printComplexNumber()
c7 = c1.multiplication(c3)
c7.printComplexNumber()
