# sorted 함수는 기본적으로 리스트, 튜플, 문자열, 집합 등 반복 가능한 객체를 정렬하여 새로운 정렬된 리스트를 반환하는 함수입니다. 기본적으로 오름차순 정렬 

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))