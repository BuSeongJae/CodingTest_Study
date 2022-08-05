package Junghyojae;

import java.util.Scanner;

public class 거스름돈 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int[] change = {500, 100, 50, 10, 5, 1};
        int money = 1000 - t;
        int cnt = 0;
        int idx = 0;
        for (; ; ) {
            if (money - change[idx] < 0) {
                idx++;
                continue;
            }
            money -= change[idx];
            cnt++;
            if (money == 0) {
                break;
            }
        }
        System.out.println(cnt);
    }
}

