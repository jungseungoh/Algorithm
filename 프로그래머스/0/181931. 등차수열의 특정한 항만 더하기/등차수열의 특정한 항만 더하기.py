def solution(a, d, included):
    s=[]
    for i in range(1,len(included)+1):
        m = a+(i-1)*d
        s.append(m)
    res = list(zip(s, included))
    sum=0
    for x in res: 
        if x[1]:
            sum+=x[0]
    return sum