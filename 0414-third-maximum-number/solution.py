class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        l = list(s)
        m = sorted(l)
        if len(m) >= 3:
            s = len(m) - 3
            return m[s] 
        else:
            return max(m)

        
