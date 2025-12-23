def solution(arr, queries):
    
    # for i in queries:
        # arr[i[0]],arr[i[1]] = arr[i[1]],arr[i[0]]
    
    for i,j in queries:
        arr[i],arr[j] = arr[j],arr[i]
    
    return arr
        