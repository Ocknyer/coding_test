def solution(numLog):
    answer = ''
    
    # for i in range(len(numLog) - 1):
    #     log = numLog[i+1] - numLog[i]
    #     if log == 1:
    #         answer += 'w'
    #     elif log == -1:
    #         answer += 's'
    #     elif log == 10:
    #         answer += 'd'
    #     elif log == -10:
    #         answer += 'a'
    
    key = dict(zip([1,-1,10,-10],['w','s','d','a']))
            
    for i in range(1, len(numLog)):
        answer += key[numLog[i] - numLog[i - 1]]
        
    return answer