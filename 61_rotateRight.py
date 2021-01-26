# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k==0:
            return head
    
        # 先成环并计算长度
        length = 1
        cur =  head
        while cur.next:
            length += 1
            cur = cur.next
        cur.next = head

        # 尾部节点走length - k%length长度
        step = length-k%length
        while step:
            cur = cur.next
            step -=1
        # 断环
        head,cur.next = cur.next,None
        return head
