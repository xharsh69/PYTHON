class complex:

    def __init__(self,r,i):
        self.r= r
        self.i = i

    def __add__(self, value1):

        return f"{self.r+value1.r}r+ {self.i+value1.i}i"
    
    def __mul__(self, value2 ):
        real = self.r * value2.r - self.i * value2.i
        imag = self.r * value2.i + self.i * value2.r
        return f"{real} + {imag}i"
         

c1= complex(2,3)
c2= complex(5,7)
print(c1+c2)
print(c1*c2)
