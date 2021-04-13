#2021.2.26
#给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        tmp1 = num1[::-1]
        sum1 = 0
        tmp2 = num2[::-1]
        sum2 = 0
        for i in range(len(tmp1)):
            sum1 += int(tmp1[i]) * 10 ** i
        for i in range(len(tmp2)):
            sum2 += int(tmp2[i]) * 10 ** i
        return str(sum1 * sum2)

num1 = "123"
num2 = "456"
solution = Solution()
print(solution.multiply(num1, num2))