#给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

#可以认为区间的终点总是大于它的起点。区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []:
            return 0
        intervals.sort(key=lambda x:x[1])
        start = intervals[0][1]
        ans = 1
        for i in range(len(intervals)):
            if intervals[i][0] >= start:
                ans += 1
                start = intervals[i][1]
            i += 1
        return len(intervals) - ans









g = [ [1,2], [2,3] ]
solution = Solution()
print(solution.eraseOverlapIntervals(g))