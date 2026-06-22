# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            summation = val1 + val2 + carry

            keep = summation % 10
            carry = summation // 10
            curr.next = ListNode(keep)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        
        return dummy.next

        # Debug code to print out list values
        # while node:
        #     print(f'Node value: {node.val}')
        #     node = node.next



            