# 일곱 난쟁이

heights = []
for i in range(9):
    heights.append(int(input()))
    heights.sort()

# 전체 키의 합
total = sum(heights)

# 두 명의 난쟁이를 찾기
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if total - heights[i] - heights[j] == 100:
            # i와 j를 제외한 나머지 일곱 난쟁이의 키 출력
            for k in range(9):
                if k != i and k != j:
                    print(heights[k])
            found = True
            break
    if found:
        break