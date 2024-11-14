# 숫자 배열 회전
# 2차원 배열 arr를 90도씩 회전시키는 함수를 구현

def rotate(arr):
    arrR = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrR[i][j] = arr[N-1-j][i]
    return arrR

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    print(f'#{test_case}')
    for i in range(N):
        print(f'{"".join(map(str, arr1[i]))} {"".join(map(str, arr2[i]))} {"".join(map(str, arr3[i]))}')