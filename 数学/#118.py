#给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = list()
        for i in range(numRows):
            b = list()
            for j in range(0, i+1):
                if j == 0 or j == i:
                    b.append(1)
                else:
                    b.append(a[i-1][j-1]+a[i-1][j])
            a.append(b)
        return a




nums = 5
solution = Solution()
print(solution.generate(5))