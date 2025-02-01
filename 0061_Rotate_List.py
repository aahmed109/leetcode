# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None or head.next == None: return head
        l = 1
        s = head
        while s.next != None:
            l +=1
            s = s.next

        tk = k%l
        if tk == 0: return head

        s = head
        i = 1
        while i < l - tk + 1:
            s = s.next
            i +=1
        q = s
        while q.next != None:
            q = q.next
        q.next = head
        i = 1
        q = s
        while i < l:
            q = q.next
            i += 1
        q.next = None
        return s
