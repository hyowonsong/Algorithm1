def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # while문을 써주기(progresses 계속 돌아가고 100보다 크거나 같다)
        while progresses and progresses[0] >= 100:      
            cnt += 1
            # 해당 작업과 작업 속도를 리스트에서 제거
            progresses.pop(0)
            speeds.pop(0)

        # 만약 오늘 기능이 배포되었다면 결과 리스트에 추가(이거 체크!)
        if cnt:
            answer.append(cnt)
    
    return answer
