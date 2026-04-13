class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set()
        for num in nums:
            checker.add(num)
        
        if len(checker) == len(nums):
            return False
        return True