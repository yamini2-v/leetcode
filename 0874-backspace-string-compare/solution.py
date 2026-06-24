class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m = []
        n = []
        for ch in s:
            if ch == '#' and len(m)>0:
                m.pop()
            elif ch != '#':
                m.append(ch)
        for c in t:
            if c == '#' and len(n)>0:
                n.pop()
            elif c != '#':
                n.append(c)
        return m == n


        
