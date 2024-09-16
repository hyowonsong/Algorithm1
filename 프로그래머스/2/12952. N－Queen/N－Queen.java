// N-퀸 문제(입력값은 n, 출력값은 int )
public class Solution {
    // N*N 체스판에 N개 배치했을 때 서로를 공격할 수 없는 위치에 놓을 수 있는 방법
    // 퀸은 대각선으로만 공격 가능
    // 완전 탐색만으로는 시간이 오래걸림 -> 따라서 백트레킹
    // 여왕이 추가될 때마다 행이나, 대각선 방향에 겹치는 여왕이 있으면 더 탐색하지 않기

    // 아래의 각 숫자들은 퀸이 각 행에서 어느 열에 위치하는지를 나타냄
    // 예를 들어, 숫자 2,1,1,3 은 첫 번째 행에 퀸이 2열, 두번째 행에 1열
    // 세 번째 행에 1열, 네 번째 행에 3열에 놓여 있다는 것을 의미합니다.

    // 2,1,1,3의 경우 유망 함수를 통과하는 조건은 2,1,1,3이 N퀸 조건에 맞는 경우

    private static int N;
    // 각 열에 퀸이 놓였는지 여부를 확인하는 배열
    private static boolean[] width;
    // 좌측 상단에서 우측 하단으로 내려가는 대각선을 확인하는 배열, 대각선 번호는 (행 + 열)로 구분
    private static boolean[] diagonal1;
    // 우측 상단에서 좌측 하단으로 내려가는 대각선을 확인하는 배열, 대각선 번호는 (행-열+N)로 구분
    private static boolean[] diagonal2;

    public int solution(int n){
        N = n;
        width = new boolean[n];
        diagonal1 = new boolean[n*2];
        diagonal2 = new boolean[n*2];
        int answer = getAns(0);
        return answer;
    }

    // 1. 퀸을 놓은 모든 가능한 경우를 탐색하는 재귀 함수
    private static int getAns(int y){
        int ans = 0;
        // 2. 모든 행에 대해서 퀸의 위치가 결정되었을 겨우
        if (y==N){
            // 3. 해결 가능한 경우의 수를 1 증가시킴
            ans++;
        }
        // 퀸을 모두 배치 하지 않았다면 다음 행에 퀸을 놓을 위치 찾아야
        else {
            // 4. 현재 행에서 퀸이 놓일 수 있는 모든 위치를 시도
            for(int i=0; i<N; i++){
                // 5. 해당 위치에 이미 퀸이 있는 경우, 대각선상에 퀸이 있는 경우 스킵
                if(width[i] || diagonal1[i+y] || diagonal2[i-y+N])
                    continue;

                // 6. 해당 위치에 퀸을 놓음
                width[i] = diagonal1[i+y] = diagonal2[i-y+N] = true;
                
                // 7. 다음 행으로 이동하여 재귀적으로 해결 가능한 경우의 수 찾기
                ans += getAns(y+1);
                
                // 8. 해당 위치에 놓인 퀸을 제거함
                // 재귀가 끝나면 퀸을 배치한 상태로 다시 돌려놓는다. 
                // 현재 위치에서 퀸을 놓을 수 없으면 다시 제거하여 다른 경로 탐색
                width[i] = diagonal1[i+y] = diagonal2[i-y+N] = false;
            }
        }
        return ans;
    }
}