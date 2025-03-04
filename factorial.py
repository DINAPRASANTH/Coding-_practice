def factorial(n):
    c=1
    
    for i in range(1,n+1):
        c*=i
        
    return c
    
n=int(input())
    
print(factorial(n))
