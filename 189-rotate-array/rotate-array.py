class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        l = nums[-k:]
        r = nums[:-k]
        nums[:] = l+r
        """
        Do not return anything, modify nums in-place instead.
        """
        