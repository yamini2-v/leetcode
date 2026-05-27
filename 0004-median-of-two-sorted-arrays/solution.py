class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = sorted(nums1 + nums2)
        l = len(n)
        if l % 2 == 0:
            y = (n[l//2 - 1]+n[l//2])/2
            return y
        else :
            x = n[l //2]
            return x


        
