class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = set(nums)
        i = 1
        while True:
            s = k*i
            if s not in n:
                return s
            i += 1

        