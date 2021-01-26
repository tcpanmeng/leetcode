# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = head = ListNode(0)
        while l1 and l2:
            x,y = l1.val,l2.val
            print(x,y)
            if x<=y:
                dummy.next=l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next

        if l1:
            dummy.next =l1
        if l2:
            dummy.next = l2
        return head.next