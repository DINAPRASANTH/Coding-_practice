if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
        
    score_record=sorted(record,key= lambda x:x[1])
    
    scores=sorted(set(x[1] for x in score_record ))
    
    second_low=scores[1]
    
    names=[x[0] for x in score_record if x[1]==second_low]
    
    for name in sorted(names):
        print(name)
