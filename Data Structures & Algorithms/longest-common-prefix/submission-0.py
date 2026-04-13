class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        short = min(strs, key=len)
        m = len(short)
        for i in range(m):
            for word in strs:
                if short[i] != word[i]:
                    return prefix
            
            prefix = short[:i+1]
        
        return prefix