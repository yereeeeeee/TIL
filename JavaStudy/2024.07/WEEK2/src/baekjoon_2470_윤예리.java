import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public interface baekjoon_2470_윤예리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int start = 0;
        int end = (n-1);

        int[] answer = new int[2];

        while (start < end) {

            int target = arr[start] + arr[end]; // 현재 계산하는 값

            if (target == 0) break;
            else if (target < 0) { // 값이 0 보다 작다?
                int next_target = arr[start+1] + arr[end]; // 다음 계산할 값 확인

                if (Math.abs(target) < Math.abs(next_target)) break; // 더 안 좋은 값을 가진다? 코드 종료
                else start += 1; // 아니라면 start + 1 해주고 한 번 더 보기
            }
            else {
                int next_target = arr[start] + arr[end-1];

                if (Math.abs(target) < Math.abs(next_target)) break;
                else end -= 1;
            }
        }


        System.out.print(arr[start]);
        System.out.print(" ");
        System.out.print(arr[end]);
    }
}
