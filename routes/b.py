p=[2,3,6,10,11]
k=9
j=0
i=1
k=k-len(p)
ans=0
for _ in range(k):
    while(j<len(p) and p[j]==i):
        j+=1
        i+=1
    ans+=i
    i+=1
print(ans)
