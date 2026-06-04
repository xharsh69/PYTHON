m1= int(input("enter your math marks:"))
m2= int(input("enter your phy marks:"))
m3= int(input("enter your che marks:"))

total_persentage = (m1+m2+m3)/3

if total_persentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >=33:
    print("you'r pass:", total_persentage)
else:
    print("you'r fail, try to next year:", total_persentage)

