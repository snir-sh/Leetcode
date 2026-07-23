class Solution:
    """Convert integer to Roman numeral."""
def intToRoman(self, num: int) -> str:
        numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        result = ''
        index = 0

        while num > 0:
            digit = num % 10
            num //= 10

            one = numerals[index]

            five = numerals[index + 1] if index + 1 < len(numerals) else ''
            ten = numerals[index + 2] if index + 2 < len(numerals) else ''

            if digit <= 3:
                part = one * digit
            elif digit == 4:
                part = one + five
            elif digit <= 8:
                part = five + one * (digit - 5)
            else:  # digit == 9
                part = one + ten

            result = part + result
            index += 2

        return result
