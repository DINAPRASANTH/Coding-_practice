def zo(n):
    alphabets=[]
    numbers=[]
    c=''
    for i in range(len(n)-1):
        if n[i].isalpha():
            alphabets.append(n[i])
        if n[i].isdigit():
            if n[i].isdigit() and n[i+1].isdigit():
                numbers.append(n[i]+n[i+1])
            else:
               numbers.append(n[i]) 
               
    for i in range(len(alphabets)):
        c+=alphabets[i]*int(numbers[i])
        
    return c





n=input()
print(zo(n))
