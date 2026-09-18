class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self,list1:ListNode | None,list2:ListNode | None):
        dummynode = ListNode(0)
        curr = dummynode
        l1=list1
        l2=list2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next=l1
                l1=l1.next
                curr=curr.next
            else:
                curr.next=l2
                l2=l2.next
                curr=curr.next
        curr.next=l1 if l1 else l2
        return dummynode.next
#测试
def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for num in vals:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

sol = Solution()
list1 = build_list([1,2,4])
list2 = build_list([1,3,4])
ans = sol.mergeTwoLists(list1, list2)
print(print_list(ans))