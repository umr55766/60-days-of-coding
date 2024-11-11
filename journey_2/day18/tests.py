import unittest

from journey_2.day18.solution import Solution, ListNode


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


class SolutionTest(unittest.TestCase):
    def test_example1(self):
        head = list_to_linked_list([1, 2, 3, 4, 5])
        expected_output = [1, 3, 5, 2, 4]
        self.assertEqual(linked_list_to_list(Solution().odd_even_list(head)), expected_output)

    def test_with_3_nodex(self):
        head = list_to_linked_list([1, 2, 3])
        expected_output = [1, 3, 2]
        self.assertEqual(linked_list_to_list(Solution().odd_even_list(head)), expected_output)

    def test_example2(self):
        head = list_to_linked_list([2, 1, 3, 5, 6, 4, 7])
        expected_output = [2, 3, 6, 7, 1, 5, 4]
        self.assertEqual(linked_list_to_list(Solution().odd_even_list(head)), expected_output)

    def test_empty_list(self):
        head = list_to_linked_list([])
        expected_output = []
        self.assertEqual(linked_list_to_list(Solution().odd_even_list(head)), expected_output)

    def test_single_element_list(self):
        head = list_to_linked_list([1])
        expected_output = [1]
        self.assertEqual(linked_list_to_list(Solution().odd_even_list(head)), expected_output)

    def test_two_elements_list(self):
        head = list_to_linked_list([1, 2])
        expected_output = [1, 2]
        self.assertEqual(linked_list_to_list(Solution().odd_even_list(head)), expected_output)
