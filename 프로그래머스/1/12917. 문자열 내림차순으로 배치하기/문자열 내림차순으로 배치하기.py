def solution(s):
    s1 = list(s)
    s1.sort()
    s1.reverse()
    
    return str("".join(s1))