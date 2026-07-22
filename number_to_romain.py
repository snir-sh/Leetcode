class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = ['I', 'V', 'X' , 'L', 'C', 'D', 'M']
        index = 0
        result = ''

        if num < 1 or num > 3999:
            return result

        while num > 0:
            digit = num % 10
            num = num // 10
            
            if digit == 4:
                result = numerals[index] + numerals[index+1] + result
            elif digit >= 1 and digit < 4:
                result = numerals[index] * digit + result
            elif digit == 5:
                result = numerals[index+1] + result
            elif digit > 5 and digit < 9:
                result = numerals[index+1] + numerals[index] * (digit - 5) + result
            elif digit == 9:
                result = numerals[index] + numerals[index+2] + result

            index = index + 2
        return result


solution = Solution()
res = solution.intToRoman(3749)
print(res)
