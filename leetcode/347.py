class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        prev = {}

        for num in nums:
            if num in prev:
                prev[num] += 1
            else:
                prev[num] = 1

        sort = sorted(prev, key=lambda x: prev[x], reverse=True)
        res = sort[:k]
        return res