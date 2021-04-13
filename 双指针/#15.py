#2021.2.24
#给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = dict()
        a = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        b = sorted([nums[i], nums[j], nums[k]])
                        if b not in ans.values():
                            ans[a] = b
                            a += 1
        return sorted(list(ans.values()))
    def threeSum2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []
        for k in range(n - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]: continue
            i = k + 1
            j = n - 1
            while i < j:
                tmp = nums[k] + nums[i] + nums[j]
                if tmp < 0:
                    i += 1
                elif tmp > 0:
                    j -= 1
                else:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1

nums = [-2,0,0,2,2]
solution = Solution()
print(solution.threeSum2(nums))