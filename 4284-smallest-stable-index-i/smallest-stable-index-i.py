class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        s = []
        for i in range(n):
            m = max(nums[0:i+1])
            o = min(nums[i:n])
            g = m - o
            if g <= k:
                s.append(i)
                
        return min(s) if s else -1


        