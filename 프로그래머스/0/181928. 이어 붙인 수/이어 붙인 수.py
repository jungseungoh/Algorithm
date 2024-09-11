def solution(num_list):
    odd_digits = ''.join([str(i) for i in num_list if i % 2 == 1])  
    even_digits = ''.join([str(i) for i in num_list if i % 2 == 0])  
    
    return int(odd_digits) + int(even_digits)


