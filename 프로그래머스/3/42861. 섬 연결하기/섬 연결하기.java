// 섬 연결하기
// N개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
// 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용 return

import java.util.Arrays;

// 1. costs 길이는 ((n-1)*n) / 2 이하
// 2. 임의의 i 에 대해 costs[i][0] 와 costs[i][1] 에는 다리가 연결되는 두 섬의 번호
// 3. costs[i][2] 에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용
// 4. 같은 연결은 두 번 주어지지 않습니다.
// 5. 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다.
import java.util.Arrays;

public class Solution {
    private static int[] parent;

    private static int find(int x) {
        // x가 속한 집합의 루트 노드 찾기
        if (parent[x] == x)
            return x;
        // 경로 압축: x의 부모를 루트로 설정
        return parent[x] = find(parent[x]);
    }

    private static void union(int x, int y) {
        // 두 집합을 하나의 집합으로 합치기
        int root1 = find(x);
        int root2 = find(y);
        parent[root2] = root1;
    }

    public int solution(int n, int[][] costs) {
        // 비용을 기준으로 다리를 오름차순 정렬
        Arrays.sort(costs, (o1, o2) -> Integer.compare(o1[2], o2[2]));

        // parent 배열 초기화
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        int answer = 0; // 최소 신장 트리의 총 비용
        int edges = 0; // 연결된 다리의 수

        for (int[] edge : costs) {
            // ❻ n - 1개의 다리가 연결된 경우 모든 섬이 연결됨
            if (edges == n - 1)
                break;

            // 현재 다리가 연결하는 두 섬이 이미 연결되어 있는지 확인
            if (find(edge[0]) != find(edge[1])) {
                // 두 섬을 하나의 집합으로 연결함
                union(edge[0], edge[1]);
                // 현재 다리의 건설 비용을 비용에 추가
                answer += edge[2];
                // 사용된 다리의 수 1증가
                edges++;
            }
        }

        return answer;
    }

}