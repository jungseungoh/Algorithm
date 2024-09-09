def solution(num_list):
    a,b=1, 0
    for x in num_list:
        a*=int(x)
        b+=int(x)
    if a < b**2:
        return 1
    else:
        return 0