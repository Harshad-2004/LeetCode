from bisect import bisect_left
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store (l, r, weight, original_index)
        items = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        # Sort by right endpoint r
        items.sort(key=lambda x: (x[1], x[0], x[3]))
        
        # Pre-extract right endpoints for binary search
        rights = [item[1] for item in items]
        
        # dp[i][k] stores (weight, tuple_of_indices)
        # We can optimize space to dp[k], but with n <= 50,000, 
        # dp table of size (n + 1) * 5 is fast and straightforward.
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        def is_better(w1: int, idx1: tuple, w2: int, idx2: tuple) -> bool:
            if w1 != w2:
                return w1 > w2
            return idx1 < idx2

        global_best_weight = 0
        global_best_indices = ()

        for i in range(1, n + 1):
            l, r, w, orig_idx = items[i - 1]
            
            # Find the latest interval j whose right endpoint < l
            # bisect_left gives first index with right >= l, so p - 1 is the last with right < l
            p = bisect_left(rights, l)
            
            for k in range(1, 5):
                # Option 1: Do not include interval i
                best_w, best_idx = dp[i - 1][k]
                
                # Option 2: Include interval i
                if k == 1:
                    take_w = w
                    take_idx = (orig_idx,)
                else:
                    prev_w, prev_idx = dp[p][k - 1]
                    if prev_w > 0:
                        take_w = prev_w + w
                        # Insert orig_idx in sorted order
                        take_idx = tuple(sorted(prev_idx + (orig_idx,)))
                    else:
                        take_w, take_idx = 0, ()
                
                if take_w > 0 and is_better(take_w, take_idx, best_w, best_idx):
                    best_w, best_idx = take_w, take_idx
                
                dp[i][k] = (best_w, best_idx)
                
                if is_better(best_w, best_idx, global_best_weight, global_best_indices):
                    global_best_weight = best_w
                    global_best_indices = best_idx
                    
        return list(global_best_indices)