# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedListHead = mergedListTail = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                mergedListTail.next = list1
                list1 = list1.next
            else:
                mergedListTail.next = list2
                list2 = list2.next
            mergedListTail = mergedListTail.next
        
        if list1:
            mergedListTail.next = list1
        else:
            mergedListTail.next = list2
                
        return mergedListHead.next