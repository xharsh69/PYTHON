# read lines

f= open("about_me.txt","r")

# data = f.readlines() # read all lines
# data= f.readline() # read 1st line
# print(data , type(data))

# data= f.readline() # read 2nd line
# print(data , type(data))


data = f.readline()

while(data != ""):
    print(data)
    data = f.readline()

f.close()