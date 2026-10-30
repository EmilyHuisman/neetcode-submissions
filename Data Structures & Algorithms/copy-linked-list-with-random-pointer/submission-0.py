"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''

        A deep coopy of LL
            - Node has 2 pointers (1 to the next, 1 to random)

        iterate thru LL once, copy normal pointers
            - store node at index in hashmap/array
        
        iterte thru list again we can link it to the random ones by indexing into hashmap

        1. iterate thru list
            - copy nodes and make the normal links to .next nodes
            - store node in hashmap =

        2. iterate thru list again
            - using hashmap make random connections
        '''


        
        cur = head
        oldToNew = {None: None}

        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        

        cur = head
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]















