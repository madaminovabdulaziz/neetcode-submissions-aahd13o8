class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cpy = nums.copy()
        ans = nums + cpy
        return ans

        