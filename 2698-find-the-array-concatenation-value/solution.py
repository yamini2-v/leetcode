class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        s = 0
        while l < r:
            tot = int(str(nums[l]) + str(nums[r]))
            s += tot
            l += 1
            r -= 1
        if l == r:
            s += nums[r]
        return s


        
