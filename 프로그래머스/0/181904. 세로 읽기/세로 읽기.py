def solution(my_string, m, c):
    answer = ''
    
    sub = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    
    for i in sub:
        answer += i[c-1]
        
    return answer
        