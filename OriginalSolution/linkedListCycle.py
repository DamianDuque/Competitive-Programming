# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## My original
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = {}
        curr = head
        if head:
            while curr.next != None:
                if curr in values:
                    return True
                else:
                    values[curr] = 1
                    curr = curr.next
        return False
    
## Toroise and Hare Neetcode Solution 
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## turtoise = slow pointer, hare = fast pointer
        turtoise, hare = head, head
        while hare and hare.next:
            turtoise = turtoise.next
            hare = hare.next.next
            if turtoise == hare:
                return True
            
        return False