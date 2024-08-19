def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]  # 각 자리의 가중치 계산 (5^4 + 5^3 + 5^2 + 5^1 + 1)
    
    position = 0
    
    for i in range(len(word)):
        position += vowels.index(word[i]) * weights[i] + 1
    
    return position