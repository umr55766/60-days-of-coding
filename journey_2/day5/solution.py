class Solution:
    def __init__(self):
        pass

    def removeMiddleNode(self, head):
        if head is None or head.next is None:
            return None

        slow_runner = head
        fast_runner = head.next.next

        while fast_runner and fast_runner.next:
            slow_runner = slow_runner.next
            fast_runner = None if fast_runner.next is None else fast_runner.next.next

        slow_runner.next = slow_runner.next.next

        return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
