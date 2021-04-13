#2021.2.23
#给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#请你将两个数相加，并以相同形式返回一个表示和的链表。
#你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        len1 = len(l1)
        len2 = len(l2)
        num1 = num2 = 0
        for i in range(len1):
            num1 += l1[i] * 10 ** i
        for i in range(len2):
            num2 += l2[i] * 10 ** i
        sum = num1 + num2
        k = 0
        list = {}
        while (sum >= 1):
            print(sum)
            list[k] = sum%10
            sum = sum//10
            k += 1
        print(list)

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(l, r, i):
            if not l and not r and not i: return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            node = ListNode(s % 10)
            node.next = dfs(l.next if l else None, r.next if r else None, s // 10)
            return node
        return dfs(l1, l2, 0)

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = p = ListNode(None)
        tmp = 0
        while (l1 or l2 or tmp):
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + tmp
            p.next = ListNode(num % 10)
            tmp = num // 10
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
solution = Solution()
print(solution.addTwoNumbers2(l1, l2))