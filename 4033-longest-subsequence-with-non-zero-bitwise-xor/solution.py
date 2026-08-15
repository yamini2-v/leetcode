class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all(num == 0 for num in nums):
            return 0
        t = 0
        for num in nums:
            t = t ^ num
        if t != 0:
            return len(nums)
        else:
            return len(nums)-1
        
