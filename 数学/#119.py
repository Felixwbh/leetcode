#给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = list()
        for i in range(rowIndex+1):
            b = list()
            for j in range(0, i+1):
                if j == 0 or j == i:
                    b.append(1)
                else:
                    b.append(a[i-1][j-1]+a[i-1][j])
            a.append(b)
        return a[rowIndex]




nums = 3
solution = Solution()
print(solution.getRow(nums))