# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        c = 1
        while s.next != None:
            c +=1
            s = s.next
            
        i = 0
        while i < c//2:
            head = head.next
            i+=1
        return head
