#2021.3.3
#给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。假设环境不允许存储 64 位整数（有符号或无符号）。


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 -1
        INT_MIN = -1 * 2 ** 31

        tmp = flag = 0
        while x != 0:
            if x < 0:
                flag = 1
                x *= -1
            tmp2 = x%10
            if (tmp > INT_MAX / 10 or (tmp == INT_MAX / 10 and tmp2 > 7)) :return 0;
            if (tmp < INT_MIN / 10 or (tmp == INT_MIN / 10 and tmp2 < -8)) :return 0;
            tmp = tmp * 10 +tmp2
            x //=10
        if flag ==1:
            return -tmp
        return tmp



x = 1534236469
solution = Solution()
print(solution.reverse(x))