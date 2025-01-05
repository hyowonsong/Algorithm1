def solution(s, skip, index):
    answer = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    not_skip = ""
    
    for i in alphabet:
        if i not in skip:
            not_skip += i

    for i in s:
        new = (not_skip.index(i)+ index)%len(not_skip)
        answer.append(not_skip[new])
    
    return ''.join(answer)