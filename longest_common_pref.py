from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        min_i = len(strs[0]) if len(strs) > 0 else 0
        for s in strs:
            min_i = min(min_i, len(s))
        
        common_pref = ''
        while i < min_i:
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return common_pref
            common_pref += char
            i += 1

        return common_pref
        
solution = Solution()
res = solution.longestCommonPrefix(["flower","flow","flight"])
print(res)
