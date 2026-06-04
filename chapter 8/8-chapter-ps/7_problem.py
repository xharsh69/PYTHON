

def rmv(l, word):
    n=[]
    for i in l:
        if  i !=word:
            n.append(i)
    return n
        

l= ["harsh","rajhansh","khushi","rahul","raja","komal" , "sh"]

 
print(rmv(l,"sh"))
    