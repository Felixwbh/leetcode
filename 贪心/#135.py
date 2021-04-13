#老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。你需要按照以下要求，帮助老师给这些孩子分发糖果：每个孩子至少分配到 1 个糖果。评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。那么这样下来，老师至少需要准备多少颗糖果呢？


from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        r = len(ratings)
        c = [1] * r
        for i in range(r-1):
            if ratings[i] < ratings[i+1]:
                c[i+1] = c[i] + 1
        for i in range(r-1, 0, -1):
            if ratings[i] < ratings[i-1] and c[i] >= c[i-1]:
                c[i-1] = c[i] + 1
        return sum(c)







g = [1,2,2]
solution = Solution()
print(solution.candy(g))