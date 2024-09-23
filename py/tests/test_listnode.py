from unittest import TestCase

from src.precompiled.listnode import ListNode


class TestListNode(TestCase):
    def test_eq_same_values(self):
        node1 = ListNode(1, None)
        node2 = ListNode(1, None)
        self.assertEqual(node1, node2)

    def test_eq_different_values(self):
        node1 = ListNode(1, None)
        node2 = ListNode(2, None)
        self.assertNotEqual(node1, node2)

    def test_eq_different_structure(self):
        node1 = ListNode.array_to_list_node([1, 2])
        node2 = ListNode.array_to_list_node([1, 3])
        self.assertNotEqual(node1, node2)

        self.assertNotEqual(node1, None)

    def test_array_to_list_node(self):
        arr = [1, 2, 3]
        head = ListNode.array_to_list_node(arr)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.next.val, 3)
        self.assertIsNone(head.next.next.next)

    def test_arrays_to_linked_list(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5]
        (l1, l2) = ListNode.arrays_to_linked_list(arr1, arr2)
        self.assertEqual(l1.val, 1)
        self.assertEqual(l2.val, 4)
        self.assertIsNone(l1.next.next.next)  # arr1 should end here
        self.assertEqual(l2.next.val, 5)
        self.assertIsNone(l2.next.next)  # arr2 should end here

    def test_index_valid(self):
        head = ListNode.array_to_list_node([1, 2, 3])
        self.assertEqual(head.index(0).val, 1)
        self.assertEqual(head.index(1).val, 2)  #
        self.assertEqual(head.index(2).val, 3)  #

        self.assertIsNone(head.index(3))
        self.assertIsNone(head.index(10))

        self.assertIsNone(head.index(-1))

    def test_iter_list(self):
        values = [node.val for node in
                  ListNode.iter_list(ListNode.array_to_list_node([1, 2, 3]))]
        self.assertEqual(values, [1, 2, 3])

    def test_iter_list_with_cnt(self):
        values = [(i, node.val) for i, node in
                  ListNode.iter_list_with_cnt(ListNode.array_to_list_node([1, 2, 3]))]
        self.assertEqual(values, [(0, 1), (1, 2), (2, 3)])

    def test_apply(self):
        result = []
        n = ListNode.array_to_list_node([5, 9])

        def collect_values(node):
            result.append(node.val)

        n.apply(collect_values)
        self.assertEqual(result, [5])

    def test_list_node_to_array(self):
        values = ListNode.list_node_to_array(
            ListNode.array_to_list_node([1, 2, 3]))
        self.assertEqual(values, [1, 2, 3])
