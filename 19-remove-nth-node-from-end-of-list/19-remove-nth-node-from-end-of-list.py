# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        slow = head
        if n == 1:
            while slow.next.next:
                slow = slow.next
            slow.next = None
            return head

        fast = head
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if not fast:
            head = slow.next
        else:
            slow.next = slow.next.next
        return head