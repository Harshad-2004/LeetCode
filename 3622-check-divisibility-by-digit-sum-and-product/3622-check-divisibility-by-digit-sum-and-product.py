class Solution(object):
    def checkDivisibility(self, n):

        original = n
        digit_sum = 0
        digit_product = 1

        while n > 0:
            digit = n % 10

            digit_sum += digit
            digit_product *= digit

            n = n // 10

        total = digit_sum + digit_product

        return original % total == 0