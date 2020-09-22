# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        fast = slow = head
        for _ in range(n):          
            fast = fast.next
            
        if not fast:                    # for case [1,2] n = 2
            return head.next            # fast will be null, thus return [2]
        
        while fast.next:                # traverse until right before the end
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next      # for case [1,2] n =1
                                        # slow.next = None, thus return [1]
        return head