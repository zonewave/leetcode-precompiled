from unittest import TestCase

from src.precompiled.treenode import TreeNode


class TestTreeNode(TestCase):
    def test_arr_to_tree(self):
        root = TreeNode.array_to_tree([2, 3, 4])
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.right.val, 4)
        self.assertEqual(root.val, 2)

        self.assertIsNone(TreeNode.array_to_tree([]))
