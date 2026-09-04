class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        
        # If the minimum element is odd, all elements can be made odd
        if min_val % 2 == 1:
            return True
        
        # If the minimum element is even, all elements must already be even
        return all(x % 2 == 0 for x in nums1)