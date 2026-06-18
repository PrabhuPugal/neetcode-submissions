import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements={}
        for i in nums:
            elements[i] = elements.get(i, 0) + 1

        heap_structure = []

        for num, freq in elements.items():
            heap_structure.append((freq, num))
        heapq.heapify(heap_structure)

        while len(heap_structure) > k:
            heapq.heappop(heap_structure)

        return [num for freq, num in heap_structure]


        

