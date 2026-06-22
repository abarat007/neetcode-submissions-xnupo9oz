# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        l1 = head
        # Step 1: Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the list into two linked lists
        l2 = slow.next
        # print(f'middle pointer: {l2.val}')
        slow.next = None

        # head=[2,4,6,8,10]
        # l1 = 2 -> 4 -> 6
        # l2 = 8 -> 10
        # l2_rev = 10 -> 8
        # final = [2,10,4,8,6]

        # Step 3: Reverse the second linked list
        prev = None
        curr = l2

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l2 = prev
        # check if l2 got reversed:
        # while l2:
        #     print(f'val: {l2.val}')
        #     l2 = l2.next

        # Step 4: iterate through both linked lists and point nodes accordingly
        # head=[2,4,6,8,10]
        # l1 = 2 -> 4 -> 6
        # l2 = 10 -> 8
        # final = [2,10,4,8,6]
        while l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next

        