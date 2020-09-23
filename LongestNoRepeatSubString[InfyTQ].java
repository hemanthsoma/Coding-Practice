/*

input:
manager

Output:
nager

input:
abcdabcdabcd

Output:
abcd


input:
abababbaab

Output:
-1

*/

import java.util.*;
public class Subst {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next(), maxWord = "", newWord = "";
        int l = word.length(), i, j, max = 0;
        for (i = 0; i < l; i++) {
            newWord = word.substring(i);
            for (j = i + 1; j < l; j++)
                if (newWord.indexOf(word.charAt(j)) + i != j)
                    break;
            if (j - i > max) {
                max = j - i;
                maxWord = word.substring(i, j);
            }
        }
        int t = maxWord.length();
        if (t>=3){
              System.out.println(maxWord);
        }
        else
        {
              System.out.println("-1");
        }
     }
}
