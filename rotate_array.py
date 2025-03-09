def displace(k,s):
    p=s[k:]
    for i in range(k):
        p.append(s[i])
        
    return p
    
    
    
    
k=int(input('enter the number of steps'))
s=list(map(int,input().split()))
print(displace(k,s))

def displace(k, s):
    n = len(s)
    k = k % n  # Handle cases where k > n
    p = s[-k:] + s[:-k]  # Take the last k elements and the rest
    return p

k = int(input('Enter the number of steps: '))
s = list(map(int, input().split()))
print(displace(k, s))
