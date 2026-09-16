from typing import Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def reverseList(head:Optional[ListNode]):
    a=[]
    curr = head
    while curr is not None:
        a.append(curr.val)
        curr=curr.next
    return a
n1 = ListNode(2)
n2 = ListNode(4)
n3 = ListNode(6)
n4 = ListNode(8)
n5 = ListNode(9)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(reverseList(n1))
        