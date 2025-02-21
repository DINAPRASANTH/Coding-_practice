

def delmid(s):
    mid=len(s)//2
    ct=[]
    
    for i in range(len(s)):
        if i!=mid:
            ct.append(s[i])
            
    return ct
    
s=list(map(int,input().split()))
print(delmid(s)) 

