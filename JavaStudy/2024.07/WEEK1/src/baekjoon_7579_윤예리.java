import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_7579_윤예리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] memory = new int[n];
        for (int i = 0; i < n; i++) {
            memory[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int[] cost = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
            sum += cost[i];
        }

        int[][] dp = new int[n][sum+1];
        int result = Integer.MAX_VALUE;

        for (int i = 0; i < sum+1; i++) {
            if (i<cost[0]) {
                dp[0][i] = 0;
            } else {
                dp[0][i] = memory[0];
            }
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < sum+1; j++) {

                // cost가 다 떨어졌다? 이전 dp 써야지 뭐...
                if (j < cost[i]) {
                    dp[i][j] = dp[i-1][j];
                } else {
                    // 앱 끈 dp, 안 끈 dp 비교해서 max 값 저장
                    dp[i][j] = Math.max(dp[i-1][j-cost[i]] + memory[i], dp[i-1][j]);
                }

                // 메모리 여유 생기면 result랑 비교
                if (dp[i][j] >= m) {
                    result = Math.min(result, j);
                }

            }

        }

        if (m > 0) System.out.println(result);
        else System.out.println(0);
    }
}
