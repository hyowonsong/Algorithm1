def solution(elements):
    answer = 0  
    cycle = elements + elements 
    s = set() 

    for i in range(len(elements)):  # 리스트의 각 원소에 대해 반복
        for j in range(1, len(elements) + 1):  # 연속된 부분 수열의 길이에 대해 반복
            s.add(sum(cycle[i:i+j])) 
    return len(s)  