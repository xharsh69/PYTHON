class calculator():
    def __init__(self,n):
        self.n= n

    def squar(self):
        print(self.n**2)

    def cube(self):
        print(self.n**3)

    def squarroot(self):
        print(self.n**1/2)


c= calculator(4)
c.squar()
c.cube()
c.squarroot()