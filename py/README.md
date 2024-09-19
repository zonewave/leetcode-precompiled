# LeetCode Python Precompiled  Library

[中文文档](https://github.com/zonewave/leetcode-precomiled/blob/master/py/README_CN.md)
## Installation

You can install the library using the following commands:

### Using pip

```sh
pip install precompiled
```
### Using pdm

```sh
pdm add precompiled
```
## Usage Instructions

Once installed, you can use the following import statements in your Python code to access all data structures from LeetCode:

python

```python
from precompiled.listnode import ListNode 
from precompiled.nestedinteger import NestedInteger 
from precompiled.treenode import TreeNode`
```
### Common Data Structures and Methods

- **ListNode**: Linked list node
    - Default implementation of the`eq`method
    - `array_to_list_node`: Converts an array into a linked list, returning the head node
    - `arrays_to_list_node`: Converts multiple arrays into multiple linked lists, returning a tuple of linked lists
- **NestedInteger**: Nested integer
- **TreeNode**: Tree node

