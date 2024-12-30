def solution(elements):
    cycle = elements + elements
    s = set()

    for i in range(len(elements)):
        # j는 연속 부분 수열의 길이를 의미 (1부터 elements 길이까지)
        for j in range(1,len(elements)+1):
            s.add(sum(cycle[i:i+j]))
    return len(s)