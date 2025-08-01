# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        leftprev,curr=dummy,head
        for i in range(left-1):
            leftprev,curr=curr,curr.next
        prev=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        leftprev.next.next=curr
        leftprev.next=prev
        return dummy.next