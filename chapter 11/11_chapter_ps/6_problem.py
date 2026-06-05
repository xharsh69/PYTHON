class vector:

    def __init__(self,x,y,z):
        self.x= x
        self.y= y 
        self.z= z
        self.l = [x,y,z] 

    def __len__(self):
        return len(self.l)
    

s= vector(2,3,4)
print(len(s))
        
        