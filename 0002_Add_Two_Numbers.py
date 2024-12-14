# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = s2 = ""
        ss1 = l1
        ss2 = l2
        while True:
            s1 += str(ss1.val)
            if ss1.next == None: break
            ss1 = ss1.next

        while True:
            s2 += str(ss2.val)
            if ss2.next == None: break
            ss2 = ss2.next

        num = str(int(s1[::-1]) + int(s2[::-1]))[::-1]

        fNode = ListNode(int(num[0]))
        cNode = fNode
        for d in num[1:]:
            new_node = ListNode(int(d))
            cNode.next = new_node
            cNode = cNode.next

        return fNode
