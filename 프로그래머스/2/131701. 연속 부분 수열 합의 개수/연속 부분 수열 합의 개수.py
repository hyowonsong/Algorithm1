# 연속 부분 수열 합의 개수

def solution(elements):
    answer = 0  
    cycle = elements + elements  # 리스트를 두 번 이어붙여 주기적인 패턴을 만듦
    # [7,9,1,1,4,7,9,1,1,4]
    s = set()  # 중복된 합을 방지하기 위한 집합(set)을 초기화

    for i in range(len(elements)):  # 리스트의 각 원소에 대해 반복
        for j in range(len(elements)):  # 리스트의 각 원소에 대해 반복
            s.add(sum(cycle[i:i+j]))  # 현재 위치에서부터 j개의 원소를 선택한 부분 수열의 합을 집합에 추가

    return len(s)  # 중복을 제외한 부분 수열 합의 개수를 반환