# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        slow = head
        fast = head
        l1 = head

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list into two linked lists
        l2 = slow.next
        slow.next = None

        # Reverse the 2nd list
        prev = None
        curr = l2

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l2 = prev

        # iterate through both and point nodes accordingly
        while l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next

        
        

        