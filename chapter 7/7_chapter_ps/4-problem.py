n = int(input("enter the number:"))

for i in range(n):
    if n%2== 0:
        print("numer is not prime:")
        break
else:
    print('number is prime')