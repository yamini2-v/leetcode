class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = []
        count = 0
        result = []
        for num in grid:
            for i in num:
                if i in l:
                    count += 1
                    if count == 1:
                        result.append(i)
                l.append(i)
        n = len(l)
        for i in range(1,n+1):
            if i not in l:
                result.append(i)
        return result

       
        