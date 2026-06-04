with open("python.txt",'r') as f:
    lines = f.readlines()

line_no =0

for line in lines:
    if "Python" in line:
        print(f"yas python is persent in this line:{line_no}")
    line_no+=1
    break

else:
    print("python is not persent in this line")








# # print(c.count("Python"))

# if 'Python' in c:
#     print("python is persent in this file")

# else:
#     print("python is not persent in this file")