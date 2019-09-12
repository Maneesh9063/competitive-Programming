# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1=ListNode(2)
l1.next= ListNode(3)

l2=ListNode(1)
l2.next= ListNode(6)
print(l1.next.val)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1.next.val)
# Solution.addTwoNumbers(l1,l2)

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         s = l1.val+l2.val
#         head = ListNode(s%10)
#         n = head
#         dummy = ListNode(0)
#         s = s//10
#         while l1.next or l2.next or s:
#             l1 = l1.next or dummy
#             l2 = l2.next or dummy
#             s = s +l1.val+l2.val
#             n.next = ListNode(s%10)
#             n = n.next
#             s = s//10
#         return head
