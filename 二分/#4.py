#2021.2.26
#给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。


from typing import List
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find(rhalf,tmp1,tmp2):
            for i in range(rhalf):
                while tmp1 + tmp2 < rhalf:
                    if tmp2 >= len(nums2):
                        tmp3 = nums1[tmp1]
                        tmp1 += 1
                    elif tmp1 >= len(nums1):
                        tmp3 = nums2[tmp2]
                        tmp2 += 1
                    elif nums1[tmp1] <= nums2[tmp2]:
                        tmp3 = nums1[tmp1]
                        tmp1 += 1
                    else:
                        tmp3 = nums2[tmp2]
                        tmp2 += 1
            return tmp3
        half = (len(nums1)+len(nums2))/2
        tmp1 = tmp2 = tmp3 = tmp4 = 0
        rhalf = math.ceil(half)
        if half != rhalf:
            return find(rhalf,tmp1,tmp2)
        else:
            return (find(rhalf,tmp1,tmp2)+find(rhalf+1,tmp1,tmp2))/2


nums2 = []
nums1 = [0,1,2,3,4]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))