d= {}

n=0

while n<=4 :
    name= input("enter your name:")
    languag= input("enter your languag:")
    d.update({name:languag})
    n+=1

print(d)
