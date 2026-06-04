with open("poem.txt","r") as f:
    c1= f.read()


with open("python_2.O.txt","r") as f:
    c2= f.read()

if (c1==c2):
    print('yas both file are same')
else:
    print("no both file are not same")