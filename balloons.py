"""Find maximum number of 'balloon' words that can be formed from given text."""

def remove_element(arr, element):
    return [x for x in arr if x != element]

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Count the occurrences of each character in the text
        char_count = {}
        for char in text:
            if char in 'balloon':
                char_count[char] = char_count.get(char, 0) + 1

        # Calculate the maximum number of "balloon" words that can be formed
        max_balloons = float('inf')
        for char in 'balloon':
            if char in char_count:
                if char == 'l' or char == 'o':
                    max_balloons = min(max_balloons, char_count[char] // 2)
                else:
                    max_balloons = min(max_balloons, char_count[char])
            else:
                return 0  # If any character is missing, we can't form "balloon"

        return max_balloons
    

s = Solution()

# fix issues for this:
res = s.maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw")
print(res)


