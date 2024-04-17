def solution(array, commands):
    answer = []
    
    for i in commands:
        part = array[i[0]-1:i[1]]
        part.sort()
        answer.append(part[i[2]-1])
    return answer