import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        return math.comb(n + k - 1, 2 * k) % MOD