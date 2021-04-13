#给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。



class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i = 0
        j = len(x) - 1
        while i < j :
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True



x = -101
solution = Solution()
print(solution.isPalindrome(x))