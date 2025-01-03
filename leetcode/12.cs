// 12. Roman numerals to integers

//this needs to be omptimizeds....

public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> nums = new Dictionary<char,int>{
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int l = 0;
        int runningTotal = 0;
        int length = s.Length;

        for (int r = 1; r < length; r++){
            if (nums[s[l]] < nums[s[r]]){
                runningTotal -= nums[s[l]];
            } else {
                runningTotal += nums[s[l]];
            }
            l++;
        }
        runningTotal += nums[s[l]];

        return runningTotal;
    }
}