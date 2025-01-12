# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return head
        if head.next == None:
            if head.val == val:
                head = None
            return head
            
        k = l = head
        head = head.next
        while head != None:
            if head.val == val:
                l.next = head.next
            else: l = l.next
            head = head.next
            
        if k.val == val: k = k.next    

        return k
