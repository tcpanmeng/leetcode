# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 通常需要先初始化一个预先指针 pre，该指针的下一个节点指向真正的头结点head
        pre = ListNode(0)
        # 初始化链表指针
        node = pre 
        # 进位
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # 对每位求和
            sum = x+y+carry
            # 求得进位 0或1
            carry = sum//10
            node.next = ListNode(sum % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            # 更新指针
            node = node.next
        # 判断最后一位是否有进位
        if carry !=0:
            node.next = ListNode(1)

        return pre.next