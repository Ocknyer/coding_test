def solution(binomial):
    # return eval(binomial)
    
    a, op, b = binomial.split()
    
    a, b = int(a), int(b)
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b