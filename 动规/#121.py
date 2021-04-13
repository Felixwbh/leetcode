#给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = float('inf')
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            ans = max(ans, prices[i] - buy)
        return ans






nums = [7,6,4,3,1]
solution = Solution()
print(solution.maxProfit(nums))