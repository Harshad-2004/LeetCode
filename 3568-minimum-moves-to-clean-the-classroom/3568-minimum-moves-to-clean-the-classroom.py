from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_map = {}
        
        # Identify start position and assign bit indexes to litter items
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start_r, start_c = r, c
                elif ch == 'L':
                    litter_map[(r, c)] = len(litter_map)
                    
        num_litters = len(litter_map)
        if num_litters == 0:
            return 0
        
        target_mask = (1 << num_litters) - 1
        
        # best_energy[r][c][mask] stores the maximum remaining energy seen so far
        best_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        # Queue stores: (r, c, current_energy, mask, moves)
        queue = deque([(start_r, start_c, energy, 0, 0)])
        best_energy[start_r][start_c][0] = energy
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, curr_e, mask, moves = queue.popleft()
            
            # If we don't have enough energy to make a move, continue
            if curr_e <= 0:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = curr_e - 1
                    
                    # If reset area, restore full capacity
                    if classroom[nr][nc] == 'R':
                        next_e = energy
                    
                    # Check if picking up litter
                    next_mask = mask
                    if (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])
                    
                    # Check if all litters are collected
                    if next_mask == target_mask:
                        return moves + 1
                    
                    # Push to queue if we found a state with strictly better energy
                    if next_e > best_energy[nr][nc][next_mask]:
                        best_energy[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_e, next_mask, moves + 1))
                        
        return -1