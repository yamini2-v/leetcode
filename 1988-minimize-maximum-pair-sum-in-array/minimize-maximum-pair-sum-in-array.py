class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        l = 0
        r = len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            n = max(s,n)
            l += 1
            r -= 1
        return n


        