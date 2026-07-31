# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length = length + 1
            curr = curr.next
            
        target = length - n
        if target == 0:
            return head.next
        
        curr = head
        index = 0
        while index < target - 1:
            curr = curr.next
            index += 1
        curr.next = curr.next.next ##removing nth node
        return head