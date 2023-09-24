class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        actual = head
        while actual and actual.next:
            if actual.val == actual.next.val:
                actual.next = actual.next.next
            else:
                actual = actual.next

        return head