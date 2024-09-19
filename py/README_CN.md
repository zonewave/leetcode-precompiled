# LeetCode Python 预编译库  
  
欢迎使用 LeetCode Python 预编译库！  
  
## 安装  
  
您可以通过以下命令安装该库：  
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
from precompiled.nestedinteger import NestedInteger from precompiled.treenode import TreeNode`  
```  
### 常用数据结构和方法 
  
- **ListNode**：链表节点  
	- 默认实现eq方法
	- array_to_list_node 将数组转换成链表，返回头结点
	- arrays_to_list_node 将多个数组转成多个链表，返回以链表为元素的元组
- **NestedInteger**：嵌套整数  
- **TreeNode**：树节点  
  
  
## 贡献  
  
欢迎任何形式的贡献！如果您有新的数据结构或改进建议，请提交拉取请求或提出问题。  
  
## 许可证  
  
本项目采用 MIT 许可证，详细信息请查看 [LICENSE](https://github.com/zonewave/leetcode-precomiled/blob/master/LICENSE) 文件。  
  
## 联系信息  
  
如有疑问，请联系项目维护者。