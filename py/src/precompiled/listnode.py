from dataclasses import dataclass
from functools import reduce
from typing import Optional, Tuple, List


@dataclass
class ListNode(object):
    val: int
    next: Optional['ListNode']

    def __eq__(self, other: 'ListNode') -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and (self.next == other.next)

    def index(self, idx: int) -> Optional['ListNode']:
        """
        返回链表第 idx 个节点， 下标从 0 开始。
        Returns the idx node of the linked list, starts at 0.
        """
        if idx < 0:
            return None
        n = self
        for _ in range(1, idx + 1):
            if n is None:
                return None
            n = n.next
        return n

    @staticmethod
    def array_to_list_node(arr: List[int]) -> Optional['ListNode']:
        """
        将数组转换为链表节点。
        Converts an array to a linked list node.
        """
        return reduce(lambda acc, val: ListNode(val, acc), reversed(arr), None)

    @staticmethod
    def arrays_to_linked_list(*arr_list: List[int]) -> Tuple[Optional['ListNode'], ...]:
        """
        将多个数组转换为链表节点元组。
        Converts multiple arrays to a tuple of linked list nodes.

        参数:
        *arr_list (list[int]): 输入的多个整数数组 (Input multiple integer arrays).

        返回:
        Tuple[Optional[ListNode]]: 链表头节点的元组，每个数组对应一个链表头节点。
        A tuple of head nodes of the linked lists, with each array corresponding to a linked list head node.
        """
        return tuple(ListNode.array_to_list_node(arr) for arr in arr_list)
