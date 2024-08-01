def solution(d, budget):
    answer = 0
    chk = 0
    d.sort()
    for i in range(len(d)):
        chk += d[i]
        if chk <= budget:
            answer += 1
        else:
            break;
    return answer

