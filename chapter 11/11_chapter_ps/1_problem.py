class twoDvector:

    def __init__(self,i,j):
        self.i = i
        self.j= j
    
    def show(self):
        print(f"this is my 2D vector: {self.i}i+ {self.j}j")
    

class threeDvector(twoDvector):
    
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k= k

    def show(self):
        print(f"this is my 3D vector: {self.i}i+ {self.j}j+ { self.k}k")



a= twoDvector(2,3)
a.show()

b= threeDvector(5,6,7)
b.show()

    