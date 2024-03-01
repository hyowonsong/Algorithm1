def solution(name, yearning, photo):
    answer = []
    for match in photo:
        score = 0
        for n in match:
            if n in name:
                score += yearning[name.index(n)]
        answer.append(score)
    return answer