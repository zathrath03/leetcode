# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Catch edge cases of empty lists
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Initialize the mergedList with the smaller first value
        if list1.val < list2.val:
            mergedListHead = mergedList = ListNode(list1.val)
            list1 = list1.next                
        else:
            mergedListHead = mergedList = ListNode(list2.val)
            list2 = list2.next
        
        # Move through each list grabbing the smallest available
        while list1 and list2:
            if list1.val < list2.val:
                mergedList.next = ListNode(list1.val)
                mergedList = mergedList.next
                list1 = list1.next
            else:
                mergedList.next = ListNode(list2.val)
                mergedList = mergedList.next
                list2 = list2.next
        
        # Attach the remaining list to the end of the merged list
        if list1:
            mergedList.next = list1
        else:
            mergedList.next = list2
            
        return mergedListHead