class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        tot = 0
        s = set(nums)
        for i in s:
            c = nums.count(i)
            tot += c * (c-1) // 2 
        return tot
        
