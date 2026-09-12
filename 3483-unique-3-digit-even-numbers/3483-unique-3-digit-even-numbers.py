from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        freq = Counter(digits)
        valid_count = 0
        
        # Check all 3-digit even numbers from 100 to 998
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            cand_freq = Counter([d1, d2, d3])
            
            if all(freq[d] >= cand_freq[d] for d in cand_freq):
                valid_count += 1
                
        return valid_count