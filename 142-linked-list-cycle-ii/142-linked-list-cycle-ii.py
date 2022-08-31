# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = {}
        index = 0
        while head:
            if head.next in nodes:
                return head.next
            nodes[head] = index
            index += 1
            head = head.next
        return None