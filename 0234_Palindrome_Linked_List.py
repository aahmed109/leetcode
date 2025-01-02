# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ### There are 2 solutions: array based and stack based. Array based solution is commented out
        if head.next == None: return True
        if head.next.next == None: return head.val == head.next.val
        #nums = []
        stack = []
        n = 0
        ph = head
        while ph.next != None:
            #nums.append(ph.val)
            n += 1
            ph = ph.next
        
        #nums.append(ph.val)
        n += 1
        ph = head

        i=0
        while i != n//2:
            stack.append(ph.val)
            i+=1
            ph = ph.next
        
        if n%2 == 1: 
            i += 1
            ph = ph.next

        while i < n:
            p = stack.pop()
            if p != ph.val: return False
            ph = ph.next
            i += 1

        return True
        #left = nums[:len(nums)//2]
        #right = nums[len(nums)//2+(len(nums) % 2):]
        #right = right[::-1]
        #return left == right
