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
        slow, fast = head, head
        list1 = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow
        # slow pointer is at the middle of the LL
        list2 = slow.next
        slow.next = None
        prev = None
        cur = list2
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp


         


        '''
        cur 1 = list1
        cur2 = list2

        store list 1 .next in temp1
        relink list1.next to list2
        store link2 in temp2
        update link2.next to be temp1
        temp1.next in temp
        '''  
        list2 = prev
        while list2:
            temp1 = list1.next
            list1.next = list2
            list1 = temp1
            temp2 = list2.next
            list2.next = list1
            list2 = temp2


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        #first traverse through the list to get the length
        # then one pointer will be at the end of the list
        # go back half way reverseing order

        start = end = head
        length = 0
        while head:
            length+=1
            head = head.next
        
        for i in range(length//2):
            end = end.next
 
        cur, prev = end.next, None
        end.next = None
        while end:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # prev
        # start
        end = prev
        
        for i in range(length//2):
            startNext = start.next
            start.next = end
            endNext = end.next
            end.next = startNext
            start = startNext
            end = endNext
        return head
        '''



        
        