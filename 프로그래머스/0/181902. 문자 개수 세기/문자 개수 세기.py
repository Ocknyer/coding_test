def solution(my_string):
    result = [0 for i in range(52)]
    alpha = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    
    for i in my_string:
        for j, v in enumerate(alpha):
            if i == v:
                result[j] += 1
                
    return result
    
    