# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""


"""


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        result = ListNode()
        ptr = result

        while head1 and head2:
            if head1.val < head2.val:
                result.next = ListNode(head1.val)
                head1 = head1.next
            else:
                result.next = ListNode(head2.val)
                head2 = head2.next
            result = result.next
        
        while head1:
            result.next = ListNode(head1.val)
            head1 = head1.next
            result = result.next
        
        while head2:
            result.next = ListNode(head2.val)
            head2 = head2.next
            result = result.next
        
        return ptr.next