class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-count,word) for word,count in count.items()]
        heapq.heapify(heap)
        return[heapq.heappop(heap)[1] for i in range(k)]
