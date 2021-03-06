#2021.2.23
#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
#你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#你可以按任意顺序返回答案。
#示例 1：
#输入：nums = [2,7,11,15], target = 9
#输出：[0,1]
#解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[num] = i

nums = [2,11,7,3,5]
target = 9
solution = Solution()
print(solution.twoSum2(nums,target))