#2021.2.25
#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。


from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        for k in range(n - 2):

            if k > 0 and nums[k] == nums[k - 1]: continue
            i = k + 1
            j = n - 1
            while i < j:
                tmp = nums[k] + nums[i] + nums[j]
                if tmp < target:
                    i += 1
                elif tmp > target:
                    j -= 1
                else:
                    ans = tmp
                    return target
                s = tmp
                if abs(s - target) < abs(ans - target):
                    ans = s
        return ans

nums = [1,1,1,1]
target = -100
solution = Solution()
print(solution.threeSumClosest(nums, target))