#2021.2.26
#给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
#函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
#你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。


from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp < target:
                i += 1
            elif tmp > target:
                j -= 1
            else:
                return [i+1, j+1]
        return None

nums = [-1,0]
target = -1
solution = Solution()
print(solution.twoSum(nums, target))