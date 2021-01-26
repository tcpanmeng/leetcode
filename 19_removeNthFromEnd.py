# 删除倒数第n个节点
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        # 快慢指针法
        fast,slow = dummy,dummy
        # 1 fast先走n
        while n:
            fast = fast.next
            n -= 1
        # 2 fast ,slow 一起走直到fast走到最后
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # 3 删除slow节点
        slow.next = slow.next.next

        return dummy.next

        # # 回溯法
        # if not head:
        #     self.count =0
        #     return head
        # head.next = self.removeNthFromEnd(head.next,n)
        # self.count += 1
        # if self.count == n:
        #     return head.next
        # else:
        #     return head
        




