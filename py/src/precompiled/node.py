from dataclasses import dataclass
from typing import Optional, List, Dict, Callable
from functools import reduce

from .treenode_base import array_to_tree


@dataclass
class Node(object):
    val: int
    next: Optional['Node']
    random: Optional['Node']
    left: Optional['Node']
    right: Optional['Node']

    def __init__(self, val_: int = 0, next_=None, random_=None, left=None, right=None):
        self.val = val_
        self.next = next_
        self.random = random_
        self.left = left
        self.right = right

    def set_next(self, next_: Optional['Node']) -> 'Node':
        self.next = next_
        return self

    def set_left(self, n: 'Node'):
        self.left = n

    def set_right(self, n: 'Node'):
        self.right = n

    @staticmethod
    def array_to_list_node(arr: List[int]) -> Optional['Node']:
        fn: Callable[[Optional['Node'], int], Node] \
            = lambda acc, val: Node(val, acc)
        return reduce(fn, reversed(arr), None)

    @staticmethod
    def array_to_tree(arr: List[int]) -> Optional['Node']:
        return array_to_tree(Node, arr)

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
