l = ["harsh", 34,"singh","khushi",'golu','raja',69]

for i in l:
    print(i)
    if i == "golu":
        break # exit the loop right now:
else:
    print("done")

for i in l:
    
    if i == 34:
        continue # skip the itration:
    print(i)
else:
    print("done")

for i in range(100):
    pass

print("excute")