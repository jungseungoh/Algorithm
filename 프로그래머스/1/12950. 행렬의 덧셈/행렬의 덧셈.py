def solution(arr1, arr2):
    result = []
    
    for row1, row2 in zip(arr1, arr2):
        summed_row = []
        
        for a, b in zip(row1, row2):
            summed_row.append(a + b)  
            
        result.append(summed_row)
    
    return result
