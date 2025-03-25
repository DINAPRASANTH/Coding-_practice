word='stress'
d={}
for i in word:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
        
for j in d:
    if d[j]==1:
        print(j)
        break
