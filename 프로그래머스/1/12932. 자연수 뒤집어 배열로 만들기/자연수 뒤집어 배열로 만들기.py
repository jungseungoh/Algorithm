def solution(n):
    str_n = str(n) #문자열 변환
    a = str_n[::-1]  # 문자열 뒤집기
    
    answer = []
    for x in a:
        answer.append(int(x))
    return answer
