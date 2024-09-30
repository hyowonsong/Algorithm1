from collections import deque
 
for _ in range(10):
    t = int(input()) 
    q = deque(map(int, input().split())) 
 
    while True:
        for i in range(1, 6):
            num = q.popleft()  # 큐에서 첫 번째 숫자 꺼냄
            num -= i  # 해당 숫자를 i만큼 감소시킴
            
            if num <= 0:  # 숫자가 0 이하로 떨어지면 0으로 설정하고 종료
                q.append(0)
                break
            q.append(num)  # 감소한 숫자를 큐의 맨 뒤로 보냄
            
        if q[-1] == 0:  # 큐의 마지막 숫자가 0이면 종료
            break
 
    # 결과 출력
    print(f"#{t}", *q)