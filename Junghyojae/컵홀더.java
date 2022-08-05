package Junghyojae;

import java.util.Scanner;

public class 컵홀더 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        String person = sc.next();
        int cnt = 0;
        for (int i = 0; i < total; i++) {
            if (person.charAt(i) == 'S') {
                cnt++;
            }
        }
        int max = cnt + ((total - cnt) / 2) + 1;
        if (total <= max) {
            System.out.println(total);
        } else {
            System.out.println(max);
        }
    }
}
