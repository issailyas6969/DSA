# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev,curr=None,slow.next
        slow.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        first,second=head,prev
        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2


        