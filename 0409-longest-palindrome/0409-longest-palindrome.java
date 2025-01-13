import java.util.*;

class Solution {
    public int longestPalindrome(String s) {
          int[] count = new int[128];
        for (char c : s.toCharArray()) {
            count[c]++;
        }
        int length = 0;
        for (int c : count) {
            length += c / 2 * 2;
            if (c % 2 == 1 && length % 2 == 0) {
                length++;
            }
        }
        return length;
    }
}   