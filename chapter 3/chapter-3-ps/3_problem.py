# detect duble space 

st= "i am very happy with my  work"

print(st.find("  "))

u_st = st.replace("  " , " ")

print(u_st)

print(u_st.find("  "))
