from dataclasses import dataclass
from typing import Optional, List

from .treenode_base import array_to_tree


@dataclass
class TreeNode(object):
    val: int
    left: Optional['TreeNode']
    right: Optional['TreeNode']

    def __init__(self, val, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def set_left(self, n: 'TreeNode'):
        self.left = n

    def set_right(self, n: 'TreeNode'):
        self.right = n

    @staticmethod
    def array_to_tree(arr: List[Optional[int]]) -> Optional['TreeNode']:
        return array_to_tree(TreeNode, arr)
