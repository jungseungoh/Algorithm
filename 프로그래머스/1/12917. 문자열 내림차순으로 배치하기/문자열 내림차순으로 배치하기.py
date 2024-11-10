def solution(s):
    s_list = list(s)              # 문자열 -> 리스트 변환
    s_list.sort(reverse=True)     # 리스트 내림차순 정렬
    
    return ''.join(s_list)        # 정렬된 리스트를 다시 문자열로 결합