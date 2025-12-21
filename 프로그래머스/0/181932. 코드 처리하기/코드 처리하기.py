def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = int(not mode)
        else:
            if i % 2 == mode:
                answer += code[i]
        
    return answer or 'EMPTY'