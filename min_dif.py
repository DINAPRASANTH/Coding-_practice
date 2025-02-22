def min_dif(s1):
    ct=sorted(s1)
    m=[]
    min_dif=float('inf')
    for i in range(len(ct)-1):
        min_dif=min(min_dif,ct[i+1]-ct[i])
    
    for i in range(len(ct)-1):
        if ct[i+1]-ct[i] == min_dif:
            m.extend([ct[i],ct[i+1]])
            
    return m
    
    
s=int(input())
s1=list(map(int,input().split()))
if s==len(s1):
    print(min_dif(s1))
else:
    print('enter valid number of numbers')
