class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(2):
            for j in nums:
                new_list.append(j)
        return new_list