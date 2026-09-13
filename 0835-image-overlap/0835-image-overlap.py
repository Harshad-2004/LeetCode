class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        # Try every possible translation
        for dr in range(-(n - 1), n):
            for dc in range(-(n - 1), n):

                overlap = 0

                # Check every cell
                for r in range(n):
                    for c in range(n):

                        nr = r + dr
                        nc = c + dc

                        # Check if translated cell is inside the matrix
                        if (0 <= nr < n and
                            0 <= nc < n and
                            img1[r][c] == 1 and
                            img2[nr][nc] == 1):

                            overlap += 1

                max_overlap = max(max_overlap, overlap)

        return max_overlap