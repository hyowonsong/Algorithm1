# 점프와 순간 이동
# 한 번에 K칸을 앞으로 점프, (현재까지 온 거리)*2에 해당하는 위치로 순간이동
# 순간이동을 하면 건전지 사용량 줄지 X, K칸을 점프하면 K만큼의 건전지 사용량
# 아이언 슈트를 착용하고 거리가 N만큼 떨어진 장소로

# 처음 무조건 점프 다음 계속 순간이동1,2,4,8,16,32,64,128,256,512,1024,2048,4096 이후 4칸 점프=건전지 5 사용
# 이걸 반대로 생각
# 2를 계속 나눠

def solution(n):
    answer = 1
    while n>1:
        answer += n%2       # 맨 처음 나머지 생기면 answer에서 더해줘
        n = n//2            # 몫만 챙겨
    return answer
print(solution(5000))