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
       node1 = ListNode(1, ListNode(2, None))
       node2 = ListNode(1, ListNode(3, None))
       self.assertNotEqual(node1, node2)

    def test_array_to_list_node(self):
       arr = [1, 2, 3]
       head = ListNode._array_to_list_node(arr)
       self.assertEqual(head.val, 1)
       self.assertEqual(head.next.val, 2)
       self.assertEqual(head.next.next.val, 3)
       self.assertIsNone(head.next.next.next)

    def test_arrays_to_linked_list(self):
       arr1 = [1, 2, 3]
       arr2 = [4, 5]
       linked_lists = ListNode.arrays_to_linked_list(arr1, arr2)

       self.assertEqual(linked_lists[0].val, 1)
       self.assertEqual(linked_lists[1].val, 4)
       self.assertIsNone(
          linked_lists[0].next.next.next)  # arr1 should end here
       self.assertEqual(linked_lists[1].next.val, 5)
       self.assertIsNone(linked_lists[1].next.next)  # arr2 should end here

