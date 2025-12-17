def solution(my_string, overwrite_string, s):
    answer = ''
    a = my_string[0:s]
    c = my_string[s+len(overwrite_string):]
    
    return a + overwrite_string + c