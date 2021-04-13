#2021.3.8
#给你一个字符串 s，找到 s 中最长的回文子串。

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l+1 > len(ans):
                    ans = s[i:j+1]
        return ans
    def partition2(self, s: str) -> List[List[str]]:
        n = len(s)
        if n < 2:
            return s
        ans = ""
        anslength = 0

        for i in range(n):
            j, jlength = self.__find(s, i, i)
            o, olength = self.__find(s, i, i+1)
            if olength >= jlength and olength > anslength:
                ans = o
                anslength = olength
            elif jlength > olength and jlength > anslength:
                ans = j
                anslength = jlength
        return ans

    def __find(self, s:str, i:int, j:int):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j], j - i - 1


s = "aaab1a31ds3aadasfdfaaaa"
solution = Solution()
print(solution.partition2(s))
