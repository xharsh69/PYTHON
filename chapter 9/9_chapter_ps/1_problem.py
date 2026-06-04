


with open("poem.txt","r") as f:
    data= f.read()

print(data.count("twinkle"))
# print(data)

if "tw inkle" in data :
    print("the word twinkle is persent this data" )
else:
    print("the word twinkle is  not persent this data" )