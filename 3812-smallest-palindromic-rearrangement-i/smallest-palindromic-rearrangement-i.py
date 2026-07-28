class Solution:
    def smallestPalindrome(self, s: str) -> str:
        l = []
        c = Counter(s)
        n = len(s)
        if n == 1:
            return s
        elif n>1:
            o = [k for k,v in c.items() if v%2 == 1]
            if len(o) > 1:
                return ''
            middle = o[0] if o else ''
            for ch in sorted(c.keys()):
                l.extend([ch]*(c[ch]//2))
            return ''.join(l)+ middle + (''.join(reversed(l)))


