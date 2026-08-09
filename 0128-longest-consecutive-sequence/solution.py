class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        z = len(nums)
        if z == 0:
            return 0
        
        s = sorted(set(nums))
        count = 1
        m = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1] + 1:
                count += 1
                m = max(m,count)
            else:
                count = 1
                
        return m


        
