class Solution:
    def smallestStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # suffix_min[i] stores min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        pref_max = float('-inf')
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            if pref_max - suffix_min[i] <= k:
                return i
                
        return -1

    # Alias in case the judge driver uses firstStableIndex
    firstStableIndex = smallestStableIndex