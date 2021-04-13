#剑指 Offer 03. 数组中重复的数字
#找出数组中重复的数字。
#在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#输入：
#[2, 3, 1, 0, 2, 5, 3]
#输出：2 或 3
#

#1.字典 优势：速度快 缺点：内存消耗大

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i in a:
                return i
            else:
                a[i] = 1

#2.原地排序 优势：空间小


#3.排序后看相邻元素是否有相同


#4.哈希



