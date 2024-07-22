import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_1717_윤예리 {

    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        parent = new int[n+1];
        for (int i = 0; i < n + 1; i++) {
            parent[i] = i;
        }

        int m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            if (Integer.parseInt(st.nextToken()) == 0) {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                union(a, b);
            }
            else {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if (find(a) == find(b)) System.out.println("YES");
                else System.out.println("NO");
            }
        }

    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x == y) return;
        else if (x < y) parent[y] = x;
        else parent[x] = y;
    }

    static int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }
}
