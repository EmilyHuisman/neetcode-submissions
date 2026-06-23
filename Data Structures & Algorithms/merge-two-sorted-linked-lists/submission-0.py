# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #6/23
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next























        '''
        cur1, cur2 = list1.head, list2.head
        dummy = ListNode()
        while cur1.next and cur2.next:
            if cur1 <= cur2:
                temp = cur1.next # 3
                cur1.next = cur2 # store pointer tp cur2
                cur1 = temp # moves forward to 3
            else:
                temp = cur2.next
                cur2.next = cur1
                cur2 = temp
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        # 06/10
        # loop thru list 1 and check if its value is less than in list 2
        # loop thru list 1 while its value is less than in list 2
        # then loop thru list 2 while its value is less than in list 1

        curr1 = list1.head
        curr2 = list2.head
        while curr1 and curr2:
            while curr1 < curr2:
                prev = curr1
                curr1 = curr1.next
            curr2 = 
        '''
