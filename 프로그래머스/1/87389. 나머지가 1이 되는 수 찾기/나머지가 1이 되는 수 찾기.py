def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 1:
            answer.append(i)
    answer.sort()   
    return answer[0]