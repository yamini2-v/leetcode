class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c = Counter(nums1)
        l = []
        for num in nums2:
            if c[num] > 0:
                l.append(num)
                c[num] -= 1
        return l

