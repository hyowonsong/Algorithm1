from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N+1))

result = []  

while queue:
    # K-1번 만큼 왼쪽으로 회전 (사람을 한 칸씩 옮기는 효과)
    queue.rotate(-(K-1))
    # K번째 사람을 제거하고 결과 리스트에 추가
    result.append(queue.popleft())

# 요세푸스 순열을 형식에 맞게 출력
print("<" + ", ".join(map(str, result)) + ">")