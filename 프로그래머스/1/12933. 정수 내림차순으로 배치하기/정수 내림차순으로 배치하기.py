def solution(n):
    #n = 118372
    str_n = str(n) # 정수 -> 문자열             "118372"
    a = list(str_n)  # 각 자릿수를 리스트에 담기  ['1', '1', '8', '3', '7', '2']
    a.sort(reverse=True) # 내림차순             ['8', '7', '3', '2', '1', '1']
    answer = ''.join(a)  #                     "873211"
    return int(answer)   #                      873211