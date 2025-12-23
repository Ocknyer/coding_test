def solution(a, d, included):
    acc = a
    answer = 0
    
    for i in included:
        if i:
            answer += acc
        acc += d
        
    return answer
            
            
            
            
            
            