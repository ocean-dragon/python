from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        p1, p2, total, maxV = 0, 0, 0, 0

        while p2 < len(nums):
            cur = p2 - p1 + 1  # 当前组已遍历的个数
            if nums[p1] == nums[p2]:
                if cur >= total:  # 对比每组最大的遍历个数
                    maxV = nums[p1]
                    total = cur
            else:
                p1 = p2
            p2 += 1

        return maxV

    def majorityElement02(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement03(self, nums: List[int]) -> int:
        winner = 0
        votes = 0

        # moore投票法：多票胜者(即众数)=+1，其他=-1
        # 推论1：所有元素和 > 0
        # 推论2：票数置零时，前面的抵消数中，众数的个数要么为0要么为一半
        for num in nums:
            # 当前无票数时，默认当前为胜者
            if votes == 0: winner = num
            # 记录当前胜者的票数
            if winner == num:
                votes += 1
            else:
                votes -= 1
        return winner


s = Solution()
nums = [6, 5, 5]  # [2, 4, 6, 4, 1, 53, 46, 7, 6]
x = s.majorityElement03(nums)
print(x)
