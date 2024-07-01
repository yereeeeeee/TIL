import java.util.Scanner;

public class 새로운_불면증_치료법 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        for (int i=0; i<n; i++) {
            int[] check = new int[10];
            long num = sc.nextLong();

            boolean flag = true;
            while (flag) {
                int sum = 0;
                for (int c:check){
                    sum += c;
                }
                if (sum == 10) {
//                    System.out.println(result);
                    break;
                }

                String str = Long.toString(num);
                char[] arr = str.toCharArray();
                for (int k=0; k< arr.length; k++) {

                }

            }
        }

    }
}
