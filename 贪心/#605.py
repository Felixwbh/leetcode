#假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
#给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。
#另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。


from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed2 = [0] + flowerbed + [0]
        i = 1
        tmp = 0
        while i <= len(flowerbed) :
            if flowerbed2[i] == flowerbed2[i + 1] == flowerbed2[i - 1] == 0:
                tmp += 1
                i += 2
            else:
                i += 1
        if tmp >= n:
            return True
        else:
            return False






flowerbed = [0,0,1,0,1]
n = 2
solution = Solution()
print(solution.canPlaceFlowers(flowerbed, n))