def paren(s):
    ct=[]
    for i in range(len(s)):
        if s[i] in '{[(':
            ct.append(s[i])
        else:
            if len(ct)==0:
                return False
            if ((ct[-1]=='[' and s[i]==']') or (ct[-1]=='(' and s[i]==')') or (ct[-1]=='{' and s[i]=='}')):
                ct.pop()
            else:
                return False
                
    return len(ct)==0
    
s=input()
print(paren(s))


#This code is used to check wether the given parenthesis is valid or not.
