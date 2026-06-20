class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l = [''] * len(s)
        for ch,i in zip(s,indices):
            l[i] = ch
        return ''.join(l)



        
