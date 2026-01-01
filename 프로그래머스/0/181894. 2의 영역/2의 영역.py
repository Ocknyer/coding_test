def solution(arr):
    first = arr.index(2) if 2 in arr else -1
    last = len(arr) - 1 - arr[::-1].index(2) if 2 in arr else -1
    return arr[first:last+1] or [-1]
