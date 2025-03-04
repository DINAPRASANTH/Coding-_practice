
name='i love 6 guys @ torronto'
lc=0
spc=0
num=0
space=0

for i in name:
    if i.isalpha():
        lc+=1
    elif i.isdigit():
        num+=1
    elif i==' ':
        space+=1
    else:
        spc+=1
        
print(lc)
print(num)
print(space)
print(spc)
