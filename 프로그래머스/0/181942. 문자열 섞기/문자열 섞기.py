def solution(str1, str2):
    res = ""
    for i in range(len(str1)):
        res += str1[i] + str2[i]
    return res