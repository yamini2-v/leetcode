class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_sum = sum(ord(x) for x in t)
        s_sum = sum(ord(x) for x in s)
        return(chr(t_sum - s_sum))
