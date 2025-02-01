def solution(s):
    # 리스트로 만들면서 각 문자들을 전부 하나,하나로 만들어 버림
    s1 = list(s)
    s1.sort()
    s1.reverse()
    
    return str("".join(s1))