class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for b in s:
            if b.islower():
                res.append(b)
            elif b == '*':
                if res:
                    res.pop(-1)
            elif b == '#':
                res.extend(res)
            elif b == '%':
                res.reverse()
        return ''.join(res)
        