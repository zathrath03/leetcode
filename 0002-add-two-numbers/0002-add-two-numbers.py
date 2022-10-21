# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, node, l1, l2, carry = self.combine_overlap(l1, l2)        
        
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        if carry:
            node, carry = self.carry_through(node)
        if carry:
            node.next = ListNode(1)        
        
        return head
    
    
    def combine_overlap(self, l1: ListNode, l2: ListNode) -> tuple[ListNode, ListNode, ListNode, ListNode, bool]:
        head = tail = ListNode()
        carry = False
        while l1 and l2:
            subtotal = l1.val + l2.val
            
            if carry:
                subtotal += 1
                
            if subtotal >= 10:
                carry = True
                subtotal -= 10
            else:
                carry = False
            
            tail.next = ListNode(subtotal)
            tail, l1, l2 = self.increment_nodes(tail, l1, l2)
            
        return (head.next, tail, l1, l2, carry)
    
    
    def increment_nodes(self, *args: ListNode) -> tuple[ListNode]:
        nodes = []
        for node in args:
            nodes.append(node.next)
        return tuple(nodes)
    
    
    def carry_through(self, node: ListNode) -> tuple[ListNode, bool]:
        carry = True
        while node.next and carry:
            node = node.next
            node.val += 1
            if node.val >= 10:
                node.val -= 10
            else:
                carry = False
        return node, carry