class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l = []
        for i,num in enumerate(nums):
            s = 0
            z = num
            while z > 0:
                d = z%10
                s += d
                z = z//10
            if s == i:
                return i
        return -1
        