class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        shift = 31

        while shift >= 0:
            if dividend >= (divisor << shift):
                print(dividend)
                print(divisor << shift)
                print(shift)
                dividend -= divisor << shift
                result += 1 << shift

            shift -= 1

        return -result if negative else result

s = Solution()
print(s.divide(23, 4))  # Output: 3

