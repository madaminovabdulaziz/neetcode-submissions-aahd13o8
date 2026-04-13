class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        myMap = {}

        for char in range(len(s)):
            myMap[s[char]] = myMap.get(s[char], 0) + 1
            myMap[t[char]] = myMap.get(t[char], 0) - 1

        return all(val == 0 for val in myMap.values())
        