import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stone weights to negative values to simulate a max-heap
        stones = [-stone for stone in stones]
        
        # Heapify the list to create a heap
        heapq.heapify(stones)
        
        while len(stones) > 1:
            # Extract the two heaviest stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first != second:
                # If the stones are not equal, push the difference back onto the heap
                heapq.heappush(stones, first - second)
        
        # If there are no stones left, return 0. Otherwise, return the weight of the last remaining stone
        return -stones[0] if stones else 0

        