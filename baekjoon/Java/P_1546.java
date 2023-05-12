import java.util.Scanner;

public class P_1546 {
    public static void main(String[] args) {
        // Input
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int grades[] = new int[N];
        for (int i=0; i < N; i++) {
            grades[i] = sc.nextInt();
        }
        
        int max = 0, sum = 0;
        for (int i=0; i < grades.length; i++) {
            if (max < grades[i]) max = grades[i];
            sum += grades[i];
        }
        System.out.println(sum * 100.0 / max / N);
    }
}