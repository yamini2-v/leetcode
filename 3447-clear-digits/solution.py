class Solution:
    def clearDigits(self, s: str) -> str:
        l =[]
        for i in s:
            if i.isalpha():
                l.append(i)
            elif i.isdigit():
                l.pop()
        return ''.join(l)

        
