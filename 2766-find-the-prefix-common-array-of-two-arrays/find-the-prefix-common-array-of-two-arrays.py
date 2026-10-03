class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        l = [0]*n
        for i in range(n):
            c = A[:i+1]
            d = B[:i+1]
            p = Counter(c + d)
            for (k,v) in p.items():
                if v == 2:
                    l[i] = l[i]+1
        return l
                    


        