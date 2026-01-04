def solution(arr, queries):
    for i,query in enumerate(queries):
        s,e = query
        for j in range(s,e+1):
            arr[j] += 1
    
    return arr