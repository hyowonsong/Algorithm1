class Solution {
    public int[] solution(int brown, int yellow) {
        // 1. 세로 길이는 3에서 시작
        // 2. A+B가 세로 길이로 나누어 떨어지면 현재 세로 길이로 사각형을 만들 수 있다는 뜻이므로 사각형 조건 만족
        // 2-1. 카펫 형태로 격자를 배치할 수 있는지 확인하고 배치할 수 있으면 사각형의 [가로 길이, 세로 길이] 를 반환하고 종료
        // 3. 반환한 세로 길이가 sqrt(B+Y) 보다 작다면 과정 1부터 반복

        // 격자의 총 개수
        int totalSize = brown + yellow;

        // 세로 길이의 범위는 3부터 sqrt(B+Y)
        int sqrt = (int)Math.sqrt(brown + yellow);
        for(int vertical = 3; vertical<=sqrt; vertical++){
            // 사각형이 맞는지 체크
            if (totalSize % vertical == 0){
                // 사각형의 가로 길이
                int horizontal = (int)(totalSize /vertical);
                // 카펫 형태로 만들 수 있는지 확인
                if(brown == (horizontal + vertical -2) * 2){
                    return new int[]{horizontal, vertical};
                }
            }
        }
        // 만약 답을 찾지 못했다면 빈 리스트
        return new int[]{};
    }
}