class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+2*i for i in range(n)]
        t = 0
        for j in nums:
            s = j ^ t
            t = s
        return t



        
