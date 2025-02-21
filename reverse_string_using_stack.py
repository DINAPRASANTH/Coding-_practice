def reverse(s):
    tp=[]
    ct=''
    for i in s:
        tp.append(i)
    while tp:
        ct+=tp.pop()
        
    return ct
    
s=input()
print(reverse(s))



