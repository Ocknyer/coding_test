def solution(a, b, c):
    set = len({a, b, c})
    
    sum = a + b + c
    sum_square = a**2 + b**2 + c**2
    sum_pow = a**3 + b**3 + c**3
    
    if set == 1:
        return sum * sum_square * sum_pow
    elif set == 2:
        return sum * sum_square
    elif set == 3:
        return sum