class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)//2):
            s=min(nums)
            l=max(nums)
            a=(s + l) / 2
            res.append(a)
            nums.remove(s)
            nums.remove(l)
        return len(list(set(res)))
        
