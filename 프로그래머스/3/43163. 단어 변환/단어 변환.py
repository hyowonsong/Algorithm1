from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words_set = set(words)
    queue = deque([(begin, 0)])
    visited = set([begin])
    
    while queue:
        current_word, level = queue.popleft()
        
        if current_word == target:
            return level
        
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in words_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))
    
    return 0