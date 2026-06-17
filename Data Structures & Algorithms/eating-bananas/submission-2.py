class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = max(1, sum(piles) // h)
        high = max(piles)
        res = high
        
        while low <= high:
            k = (low + high) // 2
            total = 0
            
            for p in piles:
                total += (p + k - 1) // k
                
            if total <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
                
        return res