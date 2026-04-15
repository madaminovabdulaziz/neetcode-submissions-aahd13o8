class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myMap = dict()
        for num in nums:
            myMap[num] = myMap.get(num, 0) +1
        
        return max(myMap, key=myMap.get)
        