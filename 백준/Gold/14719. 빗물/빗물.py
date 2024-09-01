# 입력 받기
H, W = map(int, input().split())
heights = list(map(int, input().split()))

def calculate_rainwater(H, W, heights):
    if W == 0:
        return 0
    
    left = 0  # 왼쪽 포인터
    right = W - 1  # 오른쪽 포인터
    left_max = heights[left]  # 왼쪽 최대 높이
    right_max = heights[right]  # 오른쪽 최대 높이
    total_water = 0  # 총 빗물 양
    
    while left <= right:
        if left_max <= right_max:
            if heights[left] < left_max:
                total_water += left_max - heights[left]  # 물이 고일 수 있는 양 계산
            else:
                left_max = heights[left]  # 새로운 왼쪽 최대 높이 갱신
            left += 1  # 왼쪽 포인터를 오른쪽으로 이동
        else:
            if heights[right] < right_max:
                total_water += right_max - heights[right]  # 물이 고일 수 있는 양 계산
            else:
                right_max = heights[right]  # 새로운 오른쪽 최대 높이 갱신
            right -= 1  # 오른쪽 포인터를 왼쪽으로 이동
    
    return total_water

# 빗물의 총량 계산 및 출력
print(calculate_rainwater(H, W, heights))