from dataclasses import dataclass
from functools import reduce
from typing import Optional


@dataclass
class ListNode(object):
  val: int
  next: Optional['ListNode']

  def __eq__(self, other: 'ListNode') -> bool:
    if not isinstance(other, ListNode):
      return False
    return self.val == other.val and (self.next == other.next)

  @staticmethod
  def _array_to_list_node(arr:list[int])->Optional['ListNode']:
   return reduce(lambda acc, val: ListNode(val,acc), reversed(arr), None)

  @staticmethod
  def arrays_to_linked_list(*arr_list:list[int]):
    return tuple(ListNode._array_to_list_node(arr) for arr in arr_list)





