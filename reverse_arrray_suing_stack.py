def numarr(s):
    ct=[]
    for i in range(len(s),0,-1):
        ct.append(s[i-1])
    
    return ct
    
s=list(map(int,input().split()))
print(numarr(s))
        
