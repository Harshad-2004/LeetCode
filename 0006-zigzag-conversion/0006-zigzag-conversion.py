class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if single row or string length is smaller than numRows, no zigzag occurs
        if numRows == 1 or numRows >= len(s):
            return s

        # Store characters for each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False

        # Traverse each character in s
        for char in s:
            rows[curr_row] += char
            
            # Reverse direction when reaching the top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down
            curr_row += 1 if going_down else -1

        # Join all rows to form the final string
        return ''.join(rows)