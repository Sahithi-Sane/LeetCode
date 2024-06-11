# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        # This pointer will build the new list
        current = dummy
        
        # Traverse both lists and append the smaller value to the merged list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one of the lists has remaining nodes, connect the rest of the nodes to the merged list
        current.next = list1 if list1 else list2
        
        # The merged list is next to the dummy node
        return dummy.next

        