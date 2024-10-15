# 중복 되면 안되는 숫자 출력(조합)
from itertools import combinations

# 9명의 난쟁이의 숫자를 입력받습니다.
numbers = [int(input()) for _ in range(9)]

# 모든 조합에서 합이 100인 조합을 찾습니다.
for comb in combinations(numbers, 7):
    if sum(comb) == 100:
        # 합이 100인 경우, 난쟁이의 숫자를 정렬하여 출력합니다.
        for number in sorted(comb):
            print(number)
        break 