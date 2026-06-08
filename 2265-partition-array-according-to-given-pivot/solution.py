class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less= []
        high = []
        equ = []
        for num in nums:
            if num > pivot:
                high.append(num)
            elif num < pivot:
                less.append(num)
            elif num == pivot:
                equ.append(num) 
        return less + equ + high   

        
