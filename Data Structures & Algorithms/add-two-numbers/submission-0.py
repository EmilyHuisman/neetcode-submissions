# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        5 -> 6 -> 3
        4 -> 5 -> 6

        dummy node where values get places onto
        carry node for remiander
        loop thru both pointers while they have next

        remainder is mod 10

        1. iterate thru both lists while they have next
            - add both values
            - if theres a carry move it forward
        
        2. add on remining l1 nodes
        3. add on remaning l2 nodes

        '''
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            curr.next = ListNode(total % 10)
            curr = curr.next
            carry = total // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next































        '''
        365 + 654

        keep track of last node and update value if overflow
        * prpblme what if that cuases overflow

        store future node in temp value 
        if 

        loop through l1
        store prev value
        # then add value and if its 
        if l2 add to l1, 


        while l1
            check if l2 empty, if yes
            store l1 value in prev
            move l1 to next
            add prev value to l2
            if greater than 9, subtract 10 and then update prev to remainder and add 1 to current
            
        while l2.next:
            add values to l1
        



        
        head = l1
        while l1:
            if not l2:
                return head
            prev = l1
            
            l1 = l1.next
            value = prev.val + l2.val
            remainder = 0
            if value > 9:
                remainder = l2.val - 10
                prev.val = remainder
                l1.val = l1.val + 1
            else:
                prev.val = value
            l2 = l2.next

        if l2:
            l1.next = l2
        
        return head
        '''














