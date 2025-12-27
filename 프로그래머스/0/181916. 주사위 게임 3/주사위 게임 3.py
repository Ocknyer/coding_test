def solution(a, b, c, d):
    freq = {}
    for x in [a,b,c,d]:
        freq[x] = freq.get(x, 0) + 1
    
    count = sorted(freq.values(), reverse = True)
    
    if count == [4]:
        p = next(iter(freq))
        return 1111 * p
    if count == [3, 1]:
        p = next(k for k, v in freq.items() if v == 3)
        q = next(k for k, v in freq.items() if v == 1)
        return (10 * p + q) ** 2
    if count == [2, 2]:
        pair = [k for k, v in freq.items() if v == 2]
        p, q = pair[0], pair[1]
        return (p + q) * abs(p - q)
    if count == [2, 1, 1]:
        singles = [k for k, v in freq.items() if v == 1]
        q, r = singles[0], singles[1]
        return q * r
    if count == [1, 1, 1, 1]:
        return min(a, b, c, d)