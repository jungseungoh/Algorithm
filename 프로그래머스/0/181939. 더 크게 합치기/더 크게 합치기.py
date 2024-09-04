def solution(a, b):
    r1 = int(str(a)+str(b))
    r2 = int(str(b)+str(a))
    if r1 >= r2:
        answer = r1
    else:
        answer = r2
    return answer