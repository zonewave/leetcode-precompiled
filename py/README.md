# LeetCode Python 预编译库

欢迎使用 LeetCode Python 工具库！

[github](https://github.com/zonewave/leetcode-precompiled)

本库包含
1. LeetCode 官方声明的所有数据结构
2. 本地测试所需的各种工具函数 [api说明](#常用数据结构和方法)
## 安装


目前稳定版本为0.1.8。
可以通过以下命令安装该库：
### bash
``` sh
pip install precompiled  
```  
### pdm

```sh  
pdm add precompiled
```  

## 使用说明

安装完成后，您可以在 Python 代码中使用以下导入语句来访问LeetCode所有数据结构：

python

复制

```python  
from precompiled.listnode import ListNode
from precompiled.nestedinteger import NestedInteger
from precompiled.treenode import TreeNode
```  

### 常用数据结构和方法

- **ListNode**：链表节点
    - 默认实现eq方法
    - array_to_list_node 将数组转换成链表，返回头结点
    - arrays_to_list_node 将多个数组转成多个链表，返回以链表为元素的元组
    - index: 返回链表第 idx 个节点， 下标从 0 开始。
- **NestedInteger**：嵌套整数
- **TreeNode**：树节点  
