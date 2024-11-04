def solution(s):
    p_cnt=0
    y_cnt=0
    for x in s.upper():
        if x == 'P':
            p_cnt+=1
        elif x == 'Y':
            y_cnt+=1
    return p_cnt==y_cnt

# 'p'개수 == 'y'개수 : True
# 'p'개수 != 'y'개수 : False
# 'p' && 'y' 하나도 없으면 항상 True
# 대소문자 구분 X