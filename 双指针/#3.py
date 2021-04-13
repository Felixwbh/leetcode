#给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        only = set()
        i, j, ans = 0, 0, 0
        while i < len(s) and j < len(s):
            while s[j] in only and j < len(s):
                only.remove(s[i])
                i += 1
            only.add(s[j])
            j += 1
            if len(only) > ans:
                ans = len(only)
        return ans





nums = "bbbbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(nums))