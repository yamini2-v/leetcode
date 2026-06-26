class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        l = []
        for i in s:
            if i == '1':
                l.append('0')
            else:
                l.append('1')
        p =  ''.join(l)
        return int(p,2)
            

        
