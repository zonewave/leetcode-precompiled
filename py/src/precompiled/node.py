from dataclasses import dataclass
from typing import Optional, List, Dict

from .listnode import ListNode
from .treenode import TreeNode


@dataclass
class Node(TreeNode, ListNode):
    random: Optional['Node']

    def __init__(self, val):
        TreeNode.__init__(self, val)
        ListNode.__init__(self, val, None)
        self.random = None

    @staticmethod
    def array_to_list_node(arr: List[int]) -> Optional['Node']:
        return ListNode.array_to_list_node(arr)

    @staticmethod
    def array_to_tree(vals: List[int]) -> Optional['Node']:
        return TreeNode.array_to_tree(vals)

    @staticmethod
    def arr_to_random_list(arr: List[List[int]]) -> Optional['Node']:
        if not arr:
            return None
        index_to_map: Dict[int, 'Node'] = {}
        current = head = Node(0)
        for idx, n in enumerate(arr):
            current.next = Node(n[0])
            current = current.next
            index_to_map[idx] = current

        current = head.next
        for n in arr:
            if n[1] is not None:
                current.random = index_to_map[n[1]]
            current = current.next

        return head.next
