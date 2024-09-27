// partly copied from leetcode

#ifndef LISTNODE_H
#define LISTNODE_H
#include <iostream>
#include <vector>
#include <deque>
#include <optional>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  static TreeNode* arrayToTree(const std::vector<std::optional<int>>& vals);
};
#endif