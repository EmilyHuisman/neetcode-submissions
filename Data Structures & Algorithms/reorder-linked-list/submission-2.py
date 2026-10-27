# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        - 2 pointers
            - one starts at the start
            - second starts at the middle
        - weaving them tgth by alternating

        Steps:
        1. need to find the middle point of linked list
            - then from the m
    
        2. move second pointer to there
        3. move both pointers, linking alternatig


        need to find the middle of the list
        then from the middle reverse list
        then merge that list alternatively in
        '''
        slow, fast = head, head.next
        list1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        p2 = slow.next
        slow.next = None
        prev = None
        while p2:
            temp = p2.next
            p2.next = prev
            prev = p2
            p2 = temp


         
        
        p1, p2 = head, prev
    
        while p2:
            temp1, temp2 = p1.next, p2.next
            p1.next = p2
            p2.next = temp1
            p1, p2 = temp1, temp2




        
        