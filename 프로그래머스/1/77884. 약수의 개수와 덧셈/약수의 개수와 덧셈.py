def solution(left, right):
    res=0
    for i in range(left, right+1):
        cnt=0
        for j in range(1, i+1):
            if i % j == 0:
                cnt+=1
                
        if cnt % 2==0:
            res+=i
        else:
            res-=i
    return res
            
        