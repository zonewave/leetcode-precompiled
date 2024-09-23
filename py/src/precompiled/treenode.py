from collections import deque
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode(object):
    val: int
    left: Optional['TreeNode']
    right: Optional['TreeNode']

    def __init__(self, val):
        self.val = val

    def set_left(self, n: 'TreeNode'):
        self.left = n

    def set_right(self, n: 'TreeNode'):
        self.right = n

    # @staticmethod
    # def arr_to_tree(vals: List[int]) -> Optional['TreeNode']:
    #     return new_tree(lambda x: TreeNode(x, None, None), vals)

    @staticmethod
    def array_to_tree(vals: List[Optional[int]]) -> Optional['TreeNode']:
        if not vals:
            return None

        root = TreeNode(vals[0])
        queue = deque([root])
        i = 1
        length = len(vals)

        while queue:
            node = queue.popleft()
            if i < length and vals[i] is not None:
                left = TreeNode(vals[i])
                node.set_left(left)
                queue.append(left)
            i += 1

            if i < length and vals[i] is not None:
                right = TreeNode(vals[i])
                node.set_right(right)
                queue.append(right)
            i += 1

        return root
