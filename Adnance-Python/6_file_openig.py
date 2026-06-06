
with (
    open("file1.txt",'r') as f1,
    open("file2.txt",'w') as f2
): 
    data = f1.read()
    f2.write(data)