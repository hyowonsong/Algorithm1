from collections import deque

def solution(begin, target, words):
    # 변환할 수 없는 경우, 0 반환
    if target not in words:
        return 0
    
    # BFS를 위한 큐 초기화
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    
    while queue:
        current_word, current_count = queue.popleft()
        
        # 현재 단어가 타겟 단어와 같다면 변환 횟수 반환
        if current_word == target:
            return current_count
        
        # 단어 리스트를 순회하며 한 글자 차이나는 단어를 찾음
        for word in words:
            if sum([current_word[i] != word[i] for i in range(len(current_word))]) == 1:
                queue.append((word, current_count + 1))
                
        # 이미 방문한 단어는 다시 방문하지 않기 위해 제거
        words = [word for word in words if word != current_word]
    
    # 변환할 수 없는 경우, 0 반환
    return 0
