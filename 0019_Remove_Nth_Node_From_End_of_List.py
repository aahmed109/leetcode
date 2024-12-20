# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        es = head
        cnt = 1
        while es.next != None:
            es = es.next
            cnt += 1
        if cnt == 1: return es.next
        es = head
        i = 0

        if cnt - n == 0:
            head = head.next
        else:
            while i < cnt - n- 1:
                es = es.next
                i+=1
            es.next = es.next.next

        return head
