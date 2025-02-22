from collections import defaultdict

m=defaultdict(str)
s=list(map(str,input().split(" ")))

for i in s:
    s1=""
    s2=""
    
    for j in i:
        if '0'<=j<='9':
            s1+=j
        else:
            s2+=j
            
    m[int(s1)]=s2
    
for i in sorted(m.keys()):
    print(m[i],end=" ")
