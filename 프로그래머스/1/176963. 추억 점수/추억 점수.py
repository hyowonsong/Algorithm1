def solution(name, yearning, photo):
    answer = []
    for match in photo:
        score = 0
        for i in match:
            if i in name:
                score += yearning[name.index(i)]
        answer.append(score)
    return answer