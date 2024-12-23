// 1. Two Sum

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> pairs = new Dictionary<int,int>();

        for (int i = 0; i < nums.Length; i++){
            int num = nums[i];

            if (pairs.ContainsKey(target - num)){
                return new int[] {pairs[target - num], i};
            }

            // store current number and index in dict
            pairs[num] = i;
        }

        return new int[0];
    }
}