class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l = []
        l.append(first)
        for i in range(len(encoded)):
             l.append(encoded[i] ^ l[i])
        return l

        
