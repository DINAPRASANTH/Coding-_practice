def rep(n,k):
    d={}
    c=[]
    for i in n:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        if d[i]<=k:
            c.append(i)
                
                
    return c
        
                
n=list(map(int,input().split()))
k=int(input('enter no of times'))
print(rep(n,k))
