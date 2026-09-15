class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def __repr__(self):
        return f"Node({self.val})"
if __name__ == '__main__':
    head=Node(1)
    head.next=Node(2)
    print(head)
    head=head.next
    head.next=Node(3)
    print(head)
    head=head.next
    head.next=Node(4)
    print(head)
    head=head.next
    head.next=Node(5)
    print(head)

