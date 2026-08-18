class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        n = len(nums)
        m = 0
        if k == n:
            return max(nums)
        elif k == 1:
            for k,v in c.items():
                if v == 1:
                    m = max(m,k)
            if m == 0:
                return -1
            return m
        else:
            if c[nums[0]] == 1 and c[nums[n-1]] == 1:
                return max(nums[0],nums[n-1])
            elif c[nums[0]] == 1:
                return nums[0]
            elif c[nums[n-1]] == 1:
                return nums[n-1]
            else:
                return -1
