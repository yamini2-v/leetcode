class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        z = 0
        s = sum(nums)
        for num in nums:
            while num > 0:
                d = num % 10
                z += d
                num //= 10
        return abs(s-z)
        
        