class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    hn = head
    if head==None:
        return None
    while hn.next:
        if hn.val == hn.next.val:
            hn.next = hn.next.next
        else:
            hn = hn.next

    return head


my_listNode = ListNode(1,  ListNode(2))
deleL = deleteDuplicates(my_listNode)
a = deleL
while deleL.next:
    print(a.val)
    if a.next:
        a = a.next
    else:
        break
