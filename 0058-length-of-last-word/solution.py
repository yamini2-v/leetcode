class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = s.split()
        return len(p[-1])
        
