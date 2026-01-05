def solution(str_list):
    for i, ch in enumerate(str_list):
        if ch == 'l':
            return str_list[:i]
        if ch == 'r':
            return str_list[i+1:]
    return []