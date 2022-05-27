# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = Solution.mergeTwoLists(self, list1.next, list2)
            return list1
        else:
            list2.next = Solution.mergeTwoLists(self, list1, list2.next)
            return list2


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(3, ListNode(123)))
    l2 = ListNode(2, ListNode(4, ListNode(12)))
    s = Solution().mergeTwoLists(l1, l2)
    a = s
    for i in range(6):
        print(a.val)
        a = a.next

