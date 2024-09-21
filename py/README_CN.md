# LeetCode Python 预编译库

欢迎使用 LeetCode Python 库！

[github](https://github.com/zonewave/leetcode-precomiled)

## 本地调试步骤

### 安装[leetcode-editor](https://github.com/shuzijun/leetcode-editor)

### 配置模板

![settingimag](https://github.com/zonewave/leetcode-precomiled/blob/master/py/img/templatesetting.jpg)

[template content](https://github.com/zonewave/leetcode-precomiled/blob/master/py/jetbrain_editor_template.md)

### 点击题目

![init](https://github.com/zonewave/leetcode-precomiled/blob/master/py/img/init.jpg)

### 配置参数和用例，并进行调试

![debug](https://github.com/zonewave/leetcode-precomiled/blob/master/py/img/debug.jpg)

## 安装工具库

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

安装完成后，您可以在 Python 代码中使用以下导入语句来访问leetcode所有数据结构：

python

复制

```python  
from precompiled.listnode import ListNode
from precompiled.nestedinteger import NestedInteger
from precompiled.treenode import TreeNode

`  
```  

### 常用数据结构和方法

- **ListNode**：链表节点
    - 默认实现eq方法
    - array_to_list_node 将数组转换成链表，返回头结点
    - arrays_to_list_node 将多个数组转成多个链表，返回以链表为元素的元组
    - index: 返回链表第 idx 个节点， 下标从 0 开始。
- **NestedInteger**：嵌套整数
- **TreeNode**：树节点  
