def solution(my_string, overwrite_string, s):
    answer = ''
    a = my_string[0:s]
    #b = my_string[s:s+len(overwrite_string)]
    c = my_string[s+len(overwrite_string):]
    
    return(f"{a}{overwrite_string}{c}")