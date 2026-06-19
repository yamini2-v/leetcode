class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for num in nums1:
            s = nums2.index(num)
            found = -1
            for j in range(s+1, len(nums2)):
                if nums2[j] > num:
                    found = nums2[j]
                    break
            l.append(found)
        return l

        
