li=[-1,2,3]


ls=[]
rs=[]
temp=0
for i in li:
    temp+=i
    ls.append(temp)

temp=0
for i in range(len(li)-1,-1,-1):
    temp+=li[i]
    rs.append(temp)
print(ls,rs)
ans=0
for i in range(len(ls)):
    ans=max(ans,ls[i],rs[i])
print(ans)
