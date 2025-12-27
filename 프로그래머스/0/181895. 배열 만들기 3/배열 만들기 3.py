def solution(arr, intervals):
    answer = []
    for i,j in intervals:
        answer.append(arr[i:j+1])
        
    return [x for sub in answer for x in sub]