def solution(arr, queries):
    answer = []
    
    for s,e,k in queries:
        answer.append(min((i for i in arr[s:e+1] if i > k), default = -1))
        
    return answer