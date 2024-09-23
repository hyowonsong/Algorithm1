class Solution {
    // 기지국의 최적 위치는 1부터 탐색을 진행할 때 location + w
    // 전파 범위는 양쪽이고, 왼쪽부터 최대한 전파 범위를 채워야 하기 때문
    // 그런 다음에는 다음 설치를 위해 location + w*2 + 1만큼 이동해서 탐색 다시 진행

    public int solution(int n, int[] stations, int w){
        int answer = 0;
        int location = 1; // 현재 탐색하는 아파트 위치
        int idx = 0; // 설치된 기지국의 인덱스

        // 현재 탐색 중인 아파트 위치가 n을 넘지 않는 한 반복
        while (location<=n){
            // 설치된 기지국의 전파 범위 안에 현재 위치가 있는 경우
            if (idx < stations.length && location >= stations[idx]-w){
                // 현재 아파트 위치가 기지국의 전파 범위 안에 있으면
                location = stations[idx] + w + 1;
                // 다음 기지국을 탐색하도록 기지국 인덱스를 증가
                idx ++;
            }
            // 기지국 전파 범위 밖인 경우
            else{
                // 기지국을 설치하고 해당 범위를 넘어감
                location += 2*w+1;
                answer ++;
            }
        }
        return answer;
    }
}