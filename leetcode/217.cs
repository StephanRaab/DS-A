public bool ContainsDuplicate(int[] nums) {
    HashSet<int> hs = new(nums.Length);

    for(int i = 0; i < nums.Length; i++ ){
        if (!hs.Add(nums[i])) return true;
    }
    return false;
}