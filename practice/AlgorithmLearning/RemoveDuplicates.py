from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for idxV in range(1, len(nums)):
            if nums[idx] < nums[idxV]:
                idx += 1
                nums[idx] = nums[idxV]

        return idx + 1


s = Solution()
nums = [1,1,2]#[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
cnt = s.removeDuplicates(nums)
print(cnt,nums)
