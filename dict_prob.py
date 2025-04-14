n=int(input())
un_dict={}
distinct_words=0
for _ in range(n):
    data=input()
    
    if data in un_dict:
        un_dict[data]+=1
    else:
        un_dict[data]=1
        distinct_words+=1
        
print(distinct_words)
print(*un_dict.values())
