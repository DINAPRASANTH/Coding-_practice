def non_rep(n):
    d={}
    c='There is no non-repeating letters'
    n=n.lower()
    for i in n:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            
    for j in d:
        if d[j]==1:
            return j
            break
        
    return c
            
n=input()
print(non_rep(n))
