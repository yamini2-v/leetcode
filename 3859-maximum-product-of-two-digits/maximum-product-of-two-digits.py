class Solution:
    def maxProduct(self, n: int) -> int:
        k = 0
        l = [int(x) for x in str(n)]
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                p = l[i] * l[j]
                k = max(k,p)
        return k


        