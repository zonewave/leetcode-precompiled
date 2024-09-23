from unittest import TestCase

from src.precompiled.node import Node


class TestNode(TestCase):

    def test_arr_to_tree(self):
        root = Node.array_to_tree([2, 3, 4])
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 4)
        self.assertEqual(root.val, 2)

    def test_arrays_to_linked_list(self):
        head = Node.array_to_list_node([1, 2, 3])
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)
        self.assertIsNone(head.next.next.next)

    def test_arr_to_random_list(self):
        # Test data: Each sublist's first element is the node value,
        # and the second element is the index for the random pointer
        arr = [[1, 1], [2, 2], [3, None]]
        head = Node.arr_to_random_list(arr)

        # Validate the linked list structure
        self.assertIsNotNone(head)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)
        # Validate random pointers
        self.assertEqual(head.random.val, 2)  # First node's random pointer points to the second node
        self.assertEqual(head.next.random.val, 3)  # Second node's random pointer points to the third node
        self.assertIsNone(head.next.next.random)  # Third node's random pointer should be None

    def test_empty_array(self):
        # Test empty array
        head = Node.arr_to_random_list([])
        self.assertIsNone(head)  # The result should be None
