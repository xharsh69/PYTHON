class calculator():
    def __init__(self,n):
        self.n= n

    def squar(self):
        print(self.n**2)

    def cube(self):
        print(self.n**3)

    def squarroot(self):
        print(self.n**1/2)
    
    @staticmethod
    def hello():
        print("hello there!")

c= calculator(4)
c.hello()
c.squar()
c.cube()
c.squarroot()