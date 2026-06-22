# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head

        # head = [1,2,3,4], n = 2
        # Output: [1,2,4]

        # Step 1: Find the length of the linked list
        # while curr.next:
        #     length += 1
        #     curr = curr.next

        # print(f'Length of list: {length}')

        # Step 2: Move 'first' n times
        dummy = ListNode(0,head)
        # dummy -> 1 -> 2 -> 3 -> 4
        first = dummy
        second = dummy
        counter = 0
        while counter < n:
            first = first.next
            counter += 1
        
        # Step 3: Move 'first' and 'second' forward until val is null
        while first.next:
            first = first.next
            second = second.next
        
        # Step 4: 'second is now at the node before the node to be removed,
        # so we assign second.next to second.next.next
        second.next = second.next.next

        return dummy.next

        
        


        