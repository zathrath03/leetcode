# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current_node = head
        node_list = []
        while current_node is not None:
            node_list.append(current_node.val)
            current_node = current_node.next
        for i in range(len(node_list)):
            if node_list[i] != node_list[-(i+1)]:
                return False
        return True
