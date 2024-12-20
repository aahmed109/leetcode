# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        
        li = []
        es = head
        li.append(es.val)
        while es.next != None:
            if es.next.val not in li:
                li.append(es.next.val)
                es = es.next
            else:
                es.next = es.next.next
        
        return head
