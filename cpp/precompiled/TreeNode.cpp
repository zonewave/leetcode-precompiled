#include "TreeNode.h"

// Convert array to binary tree
TreeNode *TreeNode::arrayToTree(const std::vector<std::optional<int>> &vals){
  if (vals.empty()){
    return nullptr;
  }

  TreeNode *root = new TreeNode(vals[0].value());
  std::deque<TreeNode *> queue;
  queue.push_back(root);
  size_t i = 1;
  size_t length = vals.size();

  while (!queue.empty() && i < length){
    TreeNode *node = queue.front();
    queue.pop_front();

    if (i < length && vals[i]){
      TreeNode *left = new TreeNode(vals[i].value());
      node->left = left;
      queue.push_back(left);
    }
    i++;

    if (i < length && vals[i]){
      TreeNode *right = new TreeNode(vals[i].value());
      node->right = right;
      queue.push_back(right);
    }
    i++;
  }

  return root;
}