from typing import List

class Solution:
    """Find insert position for target in sorted array."""
def searchInsert(self, nums: List[int], target: int) -> int:
        l_index = 0
        r_index = len(nums) - 1

        while l_index <= r_index:
            mid = (l_index + r_index) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r_index = mid - 1
            else:
                l_index = mid + 1
        
        return l_index
    
s = Solution()
print(s.searchInsert([1, 2, 3, 5, 6], 1))


                    # index = len(nums) // 2

        # while index >= 0 and index < len(nums):
        #     if nums[index] == target:
        #         return index
        #     if target > nums[index]:
        #         index = index + (len(nums) - index) // 2
        #     else:
        #         index = index - (len(nums) - index) //2
        # return index