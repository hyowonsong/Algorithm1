def solution(strings, n):
    answer = []
    new_answer = []
    strings.sort()
    
    for i in strings:
        new_answer.append(i[n])
        new_answer.sort()
    
    for i in new_answer:
        for string in strings:
            if string[n] == i and string not in answer:
                answer.append(string)
    return answer