from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    for word in goal:
        # cards1의 맨 앞 단어와 일치하면 제거
        if cards1 and cards1[0] == word:
            cards1.popleft()
        # cards2의 맨 앞 단어와 일치하면 제거
        elif cards2 and cards2[0] == word:
            cards2.popleft()
        # 두 카드 뭉치에 해당 단어가 없으면 "No" 반환
        else:
            return "No"
    
    # 모든 단어를 올바르게 사용했다면 "Yes" 반환
    return "Yes"