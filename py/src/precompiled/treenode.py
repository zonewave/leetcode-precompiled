from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional['TreeNode']
    right: Optional['TreeNode']

