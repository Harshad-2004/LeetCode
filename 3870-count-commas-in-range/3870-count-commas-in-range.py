class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        threshold = 1000
        
        # Each threshold of 10^(3k) adds 1 extra comma to all numbers >= threshold
        while threshold <= n:
            total_commas += (n - threshold + 1)
            threshold *= 1000
            
        return total_commas