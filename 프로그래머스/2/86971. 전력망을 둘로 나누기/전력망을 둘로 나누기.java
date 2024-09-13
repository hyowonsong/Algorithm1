import java.util.ArrayList;

// 전력망을 둘로 나누기
// n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결
// 이 전선 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할

// 최소를 구하라고 하지 않았기 때문에 깊이 우선 탐색 사용
public class Solution {
    private static boolean[] visited;
    private static ArrayList<Integer>[] adjList;
    private static int N, answer;

    public static int solution(int n, int[][] wires){
        N = n;
        answer = n-1;

        // 전선의 연결 정보를 저장할 인접 리스트 초기화
        adjList = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            adjList[i] = new ArrayList<>();
        }

        // 전선의 연결 정보를 인접 리스트에 저장
        for (int[] wire : wires) {
            adjList[wire[0]].add(wire[1]);
            adjList[wire[1]].add(wire[0]);
        }

        visited = new boolean[n + 1];

        // 깊이 우선 탐색 시작
        dfs(1);

        return answer;
    }

    private static int dfs(int now) {
        visited[now] = true;

        // 자식 노드의 수를 저장하고 반환할 변수 선언
        int sum = 0;
        // 연결된 모든 전선을 확인
        for (int next : adjList[now]) {
            if (!visited[next]) {
                // (전체 노드 - 자식 트리의 노드 수) - (자식 트리의 노드 수) 의 절대값이 가장 작은 값을 구함
                //  두 트리로 나눴을 때 두 트리 간의 노드 수 차이를 계산
                // 전력망이 9개의 송전탕빙ㄹ 경우 그 중 하나의 전선을 끊어 자식 트리의 크기가 cnt=3 이라고 합시다.
                // 이 경우 두 트리의 송전탑 수 차이는 |9-3-3| = |9-3*2| = |9-6| = 3
                // 이러한 차이를 여러 번 계산하면서 두 전력망의 송전탑 수 차이가 최소가 됩니다.
                int cnt = dfs(next); // 자식 트리가 가진 노드의 수
                answer = Math.min(answer, Math.abs(N - cnt * 2));
                // 자식 노드의 수를 더함
                sum += cnt;
            }
        }
        // 전체 자식 노드의 수에 1(현재 now 노드)을 더해서 반환
        return sum + 1;
    }
}