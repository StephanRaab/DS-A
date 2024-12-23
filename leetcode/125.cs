// 125. valid palindrome

// runtime: beats 68% -- memory: beats 51%
public class Solution {
    public bool IsPalindrome(string s) {    
        int l = 0;
        int r = s.Length -1;

        while(l < r) {
            while (l < r && !char.IsLetterOrDigit(s[l])) l++;
            while (l < r && !char.IsLetterOrDigit(s[r])) r--;

            if (char.ToLower(s[l]) != char.ToLower(s[r])) {
                return false;
            }

            l++;
            r--;
        }

        return true;
    }
}

// runtime: beats 34% -- memory: beats 34%
public class Solution {
    public bool IsPalindrome(string s) {    
        string fix = new string(s.ToLower().Where(char.IsLetterOrDigit).ToArray());
        return fix.SequenceEqual(fix.Reverse());
    }   
}