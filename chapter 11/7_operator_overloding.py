class number:
    def __init__(self,n):
        self.n= n

    def __add__(self, sum):
        return self.n + sum.n
    
    def __mul__(self, mul):
        return self.n * mul.n


n= number(22)
m= number(28)

print(n+m)
print(n*m)
        