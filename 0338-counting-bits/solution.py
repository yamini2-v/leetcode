class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(0,n+1):
            s = bin(i)
            c = s.count('1')
            l.append(c)
        return l


        
