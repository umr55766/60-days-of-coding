class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def odd_even_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        odd_node = head
        even_node = head.next
        even_head = even_node  # Save the head of even nodes to link at the end

        while even_node and even_node.next:
            # Link odd nodes
            odd_node.next = even_node.next
            odd_node = odd_node.next

            # Link even nodes
            even_node.next = odd_node.next
            even_node = even_node.next

        # Link the last odd node to the head of the even list
        odd_node.next = even_head

        return head