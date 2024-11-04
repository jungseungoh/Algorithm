def solution(n):
    answer = 0
    str_n = str(n)
    for x in str_n:
        answer+=int(x)

    return answer