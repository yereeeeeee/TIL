import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_1423_윤예리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        long[] level = new long[n+1];
        level[0] = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            level[i] = Long.parseLong(st.nextToken());
        }

        long[] power = new long[n+1];
        power[0] = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            power[i] = Long.parseLong(st.nextToken());
        }

        int d = Integer.parseInt(br.readLine());

        long result = 0;
        for (int i = 1; i < n+1; i++) {
            result += level[i] * power[i];
            level[i] = Math.min(d, level[i]);
        }

        long[] dp = new long[d+1];
        Arrays.fill(dp, 0);
        for (int i = 1; i < n+1; i++) {
            while (level[i] > 0) {
                level[i] -= 1;

                for (int j = d; j >= 0; j--) {
                    for (int k = i+1; k < n+1; k++) {
                        if (k+j-i <= d) dp[k+j-i] = Math.max(dp[k+j-i], dp[j] + (power[k] - power[i]));
                    }
                }
            }

        }

        System.out.println(dp[d] + result);
    }
}
