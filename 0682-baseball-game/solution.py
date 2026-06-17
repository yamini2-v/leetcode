class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l =[]
        for s in operations:
            if s == '+':
                l.append(l[-1]+l[-2])
            elif s == 'D':
                l.append(l[-1]*2)
            elif s == 'C':
                l.pop()
            else:
                l.append(int(s))
        return sum(l)


        
