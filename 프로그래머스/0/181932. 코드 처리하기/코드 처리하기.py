def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = int(not mode)
            
        if mode == 0:
            if i % 2 == 0 and code[i] != '1':
                answer += code[i]
        else:
            if i % 2 == 1 and code[i] != '1':
                answer += code[i]
        
    return 'EMPTY' if answer == '' else answer