# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = res = ListNode()
        ll1, ll2 = [], []
        while l1 != None:
            ll1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            ll2.append(l2.val)
            l2 = l2.next
        ll1 = reversed(ll1)
        ll2 = reversed(ll2)
        x1 = int(''.join(list(map(str, ll1))))
        x2 = int(''.join(list(map(str, ll2))))
        for i in [int(x) for x in str(x1 + x2)][::-1]:
            dummy.next = ListNode()
            dummy = dummy.next
            dummy.val = i
        return res.next


l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

print(Solution().addTwoNumbers(l1, l2))
