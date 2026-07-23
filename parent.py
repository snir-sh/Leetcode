class Solution:
    """Check if parentheses are valid and properly balanced."""
def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
    
        opens = []

        for x in s:
            if x in ['(', '[', '{']:
                opens.append(x)
            elif x not in ['(', '[', '{']:
                last = opens[-1] if len(opens) > 0 else None
                match = (x == ')' and last == '(') or (x == ']' and last == '[') or (x == '}' and last == '{')
                if match:
                    opens = opens[:-1]
                else:
                    return False
        return len(opens) == 0
    
s = Solution()
res = s.isValid("()[]}")
print(res)
