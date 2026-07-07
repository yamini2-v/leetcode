class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum = 0
        l = str(n)
        s = []
        for i in l:
            if i != '0':
                s.append(i)
        n = ''.join(s)
        if n == '':
            return 0
        for x in n:
            sum += int(x)



        return sum * int(n)

        
