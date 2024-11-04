def solution(arr):
    answer = 0
    hap = 0
    for x in arr:
        hap+=int(x)
    answer = hap/len(arr)
    return answer