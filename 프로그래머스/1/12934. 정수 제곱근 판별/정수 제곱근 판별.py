def solution(n):
    lt, rt = 1, n
    while lt<=rt:
        mid = (lt+rt)//2
        square = mid * mid
        
        if square == n:
            return (mid+1)**2
        elif square < n:
            lt = mid+1
        else:
            rt = mid -1
    return -1