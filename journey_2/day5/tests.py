import unittest

from journey_2.day5.solution import Solution, ListNode


def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class SolutionTest(unittest.TestCase):
    def test_1(self):
        head = list_to_linkedlist([1, 3, 4, 7, 1, 2, 6])
        result = Solution().removeMiddleNode(head)
        self.assertEqual(linkedlist_to_list(result), [1, 3, 4, 1, 2, 6])

    def test_2(self):
        head = list_to_linkedlist([1, 2, 3, 4])
        result = Solution().removeMiddleNode(head)
        self.assertEqual(linkedlist_to_list(result), [1, 2, 4])

    def test_3(self):
        head = list_to_linkedlist([2, 1])
        result = Solution().removeMiddleNode(head)
        self.assertEqual(linkedlist_to_list(result), [2])
