# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        index_to_remove = 0

        cur = head
        while cur:
            index_to_remove += 1
            cur = cur.next
        
        index_to_remove -= n
        
        dummy = ListNode()
        cur = dummy
        dummy.next = head
        while index_to_remove>0:
            cur = cur.next
            index_to_remove -= 1
        prev = cur
        cur = cur.next.next
        prev.next = cur

        return dummy.next
        