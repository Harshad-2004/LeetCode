class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        ans = 0
        
        limit_div = 214748364
        limit_mod = 7 if sign == 1 else 8
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            if ans > limit_div or (ans == limit_div and digit > limit_mod):
                return 0
            
            ans = ans * 10 + digit
            
        return sign * ans