def solution(my_string, queries):
    answer = my_string
    
    for i, j in queries:
        answer = answer[:i] + answer[i:j+1][::-1] + answer[j+1:]

    return answer