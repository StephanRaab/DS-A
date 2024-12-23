// 344. Reverse String

// using built in method
public class Solution {
    public void ReverseString(char[] s) {
        Array.Reverse(s);
    }
}

// using tuples and make sure to only loop through half
public class Solution {
    public void ReverseString(char[] s) {
        int len = s.Length;

        for (i = 0; i < len/2; i++){
            (s[i], s[len -1 -i]) = (s[len -1 -i], s[i]);
        }
    }
}