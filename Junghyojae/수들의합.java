package Junghyojae;

import java.util.Scanner;

public class 수들의합 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long s = sc.nextLong();
        long total = 0;
        int cnt = 0;
        for (int i = 1; ; i++) {
            total += i;
            if (s < total) {
                cnt = i - 1;
                break;
            }
        }
        System.out.println(cnt);

    }
}
