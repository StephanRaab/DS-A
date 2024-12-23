// 9. Palindrome number

// Beats --> Runtime: 68% -- Memory: 71%
public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0) return false;

        int reverse = 0;
        int xCopy = x;

        while (x > 0) {
            reverse = (reverse * 10) + (x % 10);
            x = x / 10;
        }

        return reverse == xCopy;
    }
}