class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = str(nums[i])
            nums.append(int(s[::-1]))
        return len(set(nums))
        