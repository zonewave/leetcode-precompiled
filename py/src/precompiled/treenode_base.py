from collections import deque
from typing import Callable, List, Optional


def array_to_tree(init_node: Callable[[int], any], arr: List[Optional[int]]) -> any:
    if not arr:
        return None

    root = init_node(arr[0])
    queue = deque([root])
    i = 1
    length = len(arr)

    while queue:
        node = queue.popleft()
        if i < length and arr[i] is not None:
            left = init_node(arr[i])
            node.set_left(left)
            queue.append(left)
        i += 1

        if i < length and arr[i] is not None:
            right = init_node(arr[i])
            node.set_right(right)
            queue.append(right)
        i += 1
    return root
