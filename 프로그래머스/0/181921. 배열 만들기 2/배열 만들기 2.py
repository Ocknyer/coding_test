def solution(l, r):
    return [i for i in range(l, r+1) if set(str(i)) <= {'0', '5'}] or [-1]