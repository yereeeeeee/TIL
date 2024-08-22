import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int n;
    static int[] a, maxTree, minTree;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int test = 1; test <= t; test++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            sb.append("#").append(test).append(" ");
            a = new int[n];
            maxTree = new int[4 * n];
            minTree = new int[4 * n];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }

            init(1, 0, n - 1);

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int query = Integer.parseInt(st.nextToken());
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());

                if (query == 0) {
                    update(1, 0, n - 1, left, right);
                } else if (query == 1) {
                    int max = queryMax(1, 0, n - 1, left, right - 1);
                    int min = queryMin(1, 0, n - 1, left, right - 1);
                    sb.append(max - min).append(" ");
                }
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    // 세그먼트 트리 초기화
    // node : 세그먼트 트리의 정점 번호
    // nodeLeft:  이 정점이 관리하는 연속 구간의 왼쪽 끝
    // nodeRight: 이 정점이 관리하는 연속 구간의 오른쪽 끝
    public static void init(int node, int nodeLeft, int nodeRight) {
        if (nodeLeft == nodeRight) {
            maxTree[node] = a[nodeLeft];
            minTree[node] = a[nodeLeft];
            return;
        }

        int mid = (nodeLeft + nodeRight) / 2;

        init(
                node * 2, // 왼쪽 자식
                nodeLeft,
                mid
        );

        init(
                node * 2 + 1, // 오른쪽 자식
                mid + 1,
                nodeRight
        );

        maxTree[node] = Math.max(maxTree[node * 2], maxTree[node * 2 + 1]);
        minTree[node] = Math.min(minTree[node * 2], minTree[node * 2 + 1]);
    }

    // 세그먼트 트리 갱신
    public static void update(int node, int nodeLeft, int nodeRight, int queryIndex, int value) {
        if (queryIndex < nodeLeft || nodeRight < queryIndex) { // 포함되지 않음
            return;
        }

        if (nodeLeft == nodeRight) {
            maxTree[node] = value;
            minTree[node] = value;
            return;
        }

        int mid = (nodeLeft + nodeRight) / 2;

        update(
                node * 2,
                nodeLeft,
                mid,
                queryIndex,
                value
        );

        update(
                node * 2 + 1,
                mid + 1,
                nodeRight,
                queryIndex,
                value
        );

        maxTree[node] = Math.max(maxTree[node * 2], maxTree[node * 2 + 1]);
        minTree[node] = Math.min(minTree[node * 2], minTree[node * 2 + 1]);
    }

    // 최대값 쿼리
    public static int queryMax(int node, int nodeLeft, int nodeRight, int queryLeft, int queryRight) {
        if (queryRight < nodeLeft || nodeRight < queryLeft) { // 이 정점이 쿼리랑 전혀 상관이 없다면
            return 0;
        }

        if (queryLeft <= nodeLeft && nodeRight <= queryRight) { // 이 정점이 쿼리에 완벽하게 포함된다면
            return maxTree[node];
        }

        int mid = (nodeLeft + nodeRight) / 2;
        int leftMax = queryMax(
                node * 2,
                nodeLeft,
                mid,
                queryLeft,
                queryRight
        );
        int rightMax = queryMax(
                node * 2 + 1,
                mid + 1,
                nodeRight,
                queryLeft,
                queryRight
        );

        return Math.max(leftMax, rightMax);
    }

    // 최소값 쿼리
    static int queryMin(int node, int nodeLeft, int nodeRight, int queryLeft, int queryRight) {
        if (queryLeft > nodeRight || queryRight < nodeLeft) {
            return Integer.MAX_VALUE;
        }

        if (queryLeft <= nodeLeft && nodeRight <= queryRight) {
            return minTree[node];
        }

        int mid = (nodeLeft + nodeRight) / 2;
        int leftMin = queryMin(
                node * 2,
                nodeLeft,
                mid,
                queryLeft,
                queryRight
        );
        int rightMin = queryMin(
                node * 2 + 1,
                mid + 1,
                nodeRight,
                queryLeft,
                queryRight
        );

        return Math.min(leftMin, rightMin);
    }

 
}