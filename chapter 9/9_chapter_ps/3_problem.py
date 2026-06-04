def g_t(n):
    tebal =""
    for i in range(1,11):
        tebal += f"{n}x{i} ={n*i}\n"
    with open(f"tebals/tebal_{n}.txt" ,"w") as f:
        f.write(str(tebal))





for i in range(2,21):
    g_t(i)
    
    


