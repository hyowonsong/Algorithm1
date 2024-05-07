def solution(dartResult):
    scores = []
    num = ''
    for char in dartResult:
        if char.isdigit():
            num += char
        elif char == 'S':
            scores.append(int(num))
            num = ''
        elif char == 'D':
            scores.append(int(num) ** 2)
            num = ''
        elif char == 'T':
            scores.append(int(num) ** 3)
            num = ''
        elif char == '*':
            if len(scores) > 1:
                scores[-2] *= 2
            scores[-1] *= 2
        elif char == '#':
            scores[-1] *= -1
    return sum(scores)
