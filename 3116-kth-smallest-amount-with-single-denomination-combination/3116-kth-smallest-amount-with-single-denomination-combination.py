class Solution(object):
    def findKthSmallest(self, coins, k):

        # Find GCD
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Find LCM
        def lcm(a, b):
            return a // gcd(a, b) * b

        # Count how many valid amounts are <= x
        def count(x):
            total = 0
            n = len(coins)

            # Check every subset of coins
            for mask in range(1, 1 << n):

                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                        bits += 1

                        # No need to continue if LCM is already too large
                        if multiple > x:
                            break

                if multiple > x:
                    continue

                value = x // multiple

                if bits % 2 == 1:
                    total += value
                else:
                    total -= value

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left