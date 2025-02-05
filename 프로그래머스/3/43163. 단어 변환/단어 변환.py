# 단어 변환
# 한 단계씩 변환해 나가면서 동시에 여러 경로를 탐색한다. 
# 처음으로 target을 찾는 순간이 곧 가장 짧은 변환 과정(가장 짧은 변환 과정을 찾기 때문에 BFS)

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
        words_to_remove = []  # 방문할 단어를 기록할 리스트
        
        for word in words:
            diff_count = 0

            for i in range(len(current_word)):
                # 현재 단어와 비교하여 한 글자만 다를 경우
                if current_word[i] != word[i]:
                    diff_count += 1
                # 한 글자 초과 다르면 break
                if diff_count > 1:
                    break
                
            # 한 글자만 다른 경우
            if diff_count == 1:
                queue.append((word, current_count + 1))
                words_to_remove.append(word)  # 방문한 단어를 기록
        
        # 이미 방문한 단어는 다시 방문하지 않기 위해 제거
        for word in words_to_remove:
            words.remove(word)
    
    # 변환할 수 없는 경우, 0 반환
    return 0