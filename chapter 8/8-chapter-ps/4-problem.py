n=int(input("enter the number:"))

def sumn(n):
    if n==1 :
        return 1
    
    s= n+sumn(n-1)
    return s

print(sumn(n))

