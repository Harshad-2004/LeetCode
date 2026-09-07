class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        
        # last_added[c] tracks the number of new subsequences added 
        # when character c was last processed.
        last_added = {}
        
        for char in s:
            # new_added is (total + 1) minus duplicates from previous occurrences of char
            new_added = (total + 1 - last_added.get(char, 0)) % MOD
            total = (total + new_added) % MOD
            last_added[char] = (last_added.get(char, 0) + new_added) % MOD
            
        return total