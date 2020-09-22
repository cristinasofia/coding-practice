# 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = head
        fast = head.next
        
        while fast:
            if slow.val == fast.val:        # if values are equal
                slow.next = fast.next       # slow does not move
                fast = fast.next            # fast moves forward
            else:                           # if not equal
                slow = slow.next            # slow moves forward
                fast = fast.next            # fast moves forward
        
        return head