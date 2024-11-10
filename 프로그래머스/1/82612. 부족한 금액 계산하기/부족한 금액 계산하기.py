def solution(price, money, count):
    using=[]
    for i in range(1, count+1):
        i = i * price
        using.append(i)
    
    hap=0
    for x in using:
        hap+=x
    if hap > money:
        return hap - money
    else:
        return 0