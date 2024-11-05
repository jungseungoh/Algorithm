def solution(x):
    str_x = str(x)
    hap = 0
    
    for c in str_x:
        hap += int(c)
    
    if x % hap == 0:
        return True
    else:
        return False