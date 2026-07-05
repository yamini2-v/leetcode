class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = list(s)
        l = 0
        r = len(s)-1
        while l < r:
            if n[l] != n[r]:
                if ord(n[l]) > ord(n[r]):
                    n[l] = n[r]
        
                else:
                    n[r] = n[l]
            l += 1
            r -= 1
        return ''.join(n)
                
