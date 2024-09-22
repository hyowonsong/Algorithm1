// 가장 큰 정사각형 찾기
public class Solution {
    // board 에서 1로 구성된 가장 큰 정사각형을 찾아 넓이는 반환

    // 1. 우선 board 가 다음과 같이 1*1 인 경우 1이면 1 아니면 0
    // 2. 1행만 있다고 하면 가장 큰 정사각형의 한 변의 길이는 1
    // 3. 다음 정사각형을 만들기 위해서는 최소 2*2 + 양옆, 대각선 1이어야
    // 4. 왼쪽, 위쪽, 왼쪽-위 대각선을 보고 모두 1이면 대각선을 만든다.
    // 결론 : board 를 메모이제이션처럼 활용하면서 나감
    // board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1])+1 (단, i,j>0)

    public int solution (int[][] board){
        // 1. 주어진 2차원 보드의 행과 열의 개수를 변수에 저장
        int row = board.length;
        int col = board[0].length;

        // 2. 각 행과 열을 순회하며 최적의 정사각형을 찾기
        for (int i = 1; i<row; i++){
            for (int j = 1; j<col; j++){
                // 3. 현재 위치의 값이 1인 경우를 확인합니다.
                if (board[i][j] == 1) {
                    // 4. 현재 위치에서 위, 왼쪽, 대각선 왼쪽 위의 값들을 가져옵니다.
                    int up = board[i - 1][j];
                    int left = board[i][j - 1];
                    int upLeft = board[i - 1][j - 1];
                    // 5. 현재 위치의 값을 이전 위치들의 값들 중
                    // 가장 작은 값에 1을 더한 값으로 업데이트 합니다.
                    board[i][j] += Math.min(up, Math.min(upLeft, left));
                }
            }
        }

        int answer = 0;
        // 6. 보드에서 가장 큰 값(최대 정사각형의 한 변의 길이)을 찾습니다.
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                answer = Math.max(answer, board[i][j]);
            }
        }

        // 7. 최대 정사각형의 넓이를 반환합니다.
        return answer * answer;
    }

}