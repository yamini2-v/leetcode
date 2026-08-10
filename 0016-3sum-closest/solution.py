class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        k = sorted(nums)
        c = float('inf')
        z = 0

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = k[i]+ k[l]+k[r]
                d = abs(s-target)
                if d < c:
                    c = d
                    z = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return z
