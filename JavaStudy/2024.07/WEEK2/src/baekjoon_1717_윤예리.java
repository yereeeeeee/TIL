import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class baekjoon_1717_윤예리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] ladder = new int[101];
        for (int i = 0; i < 101; i++) {
            ladder[i] = i;
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            ladder[x] = y;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            ladder[u] = v;
        }

        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        int[] visited = new int[101];
        visited[1] = 1;

        while (!q.isEmpty()) {
            int x = q.poll();

            if (x == 100) {
                System.out.println(visited[x]-1);
                return;
            }

            for (int k = 1; k < 7; k++) {
                int nx = x + k;
                if (nx <= 100 && visited[nx] == 0) {
                    q.add(ladder[nx]);
                    visited[nx] = visited[x] + 1;
                }
            }
        }


    }
}
