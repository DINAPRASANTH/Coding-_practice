def s1ins2(s1,s2):
    set_s2=set(s2)
    removed_str=''
    
    for i in s1:
        if i not in set_s2:
            removed_str+=i
            
    return removed_str
    
s1=input()
s2=input()
print(s1ins2(s1,s2))
        
