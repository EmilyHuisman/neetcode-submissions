# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''

        Given: linked list
        Goal: determine if its a palindrome



        2 pointers: one fast, one slow to find middle of LL
            - once the fast pointer reached the None, slow is in middle
        
        reverse the LL from the middle

        and then compare the two halves
        '''



        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse from middle (right portion)
        prev = slow
        cur = slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True



















        