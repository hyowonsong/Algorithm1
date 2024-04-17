# 두개 뽑아서 더하기

def solution(numbers):
    answer = []
    set_numbers = set(numbers)
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
            answer.sort()
    return sorted(list(set(answer)))