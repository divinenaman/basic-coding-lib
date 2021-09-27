# https://leetcode.com/problems/add-two-numbers/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = ListNode(0,None)
        temp = ans
        c = 0
        while l1 != None or l2 != None:
            x = 0 if l1==None else l1.val
            y = 0 if l2==None else l2.val
            s = x + y + c
            c = s // 10
            temp.next = ListNode(s % 10)
            temp = temp.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        
        if c > 0:
            temp.next = ListNode(c)
        return ans.next