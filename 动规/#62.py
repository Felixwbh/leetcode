# 2021.3.8
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 问总共有多少条不同的路径？

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l =[[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                l[i][j] = l[i-1][j] + l[i][j-1]
        return l[m-1][n-1]


m = 7
n = 3
solution = Solution()
print(solution.uniquePaths(m, n))
