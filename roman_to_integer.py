class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and (s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']):
                result += self.get_value(s[i:i+2])
                i += 2
            else:
                result += self.get_value(s[i])
                i += 1
        return result


    def get_value(self, substr):
        if substr == 'I':
            return 1
        elif substr == 'V':
            return 5
        elif substr == 'X':
            return 10
        elif substr == 'L':
            return 50
        elif substr == 'C':
            return 100
        elif substr == 'D':
            return 500
        elif substr == 'M':
            return 1000
        elif substr == 'IV':
            return 4
        elif substr == 'IX':
            return 9
        elif substr == 'XL':
            return 40
        elif substr == 'XC':
            return 90
        elif substr == 'CD':
            return 400
        elif substr == 'CM':
            return 900
        else:
            return len(substr) * self.get_value(substr[0])
        
solution = Solution()
res = solution.romanToInt("IIV")


print(res)