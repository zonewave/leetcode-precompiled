
// partly copied from leetcode

#ifndef LISTNODE_H
#define LISTNODE_H

#include <iostream>
#include <vector>
#include <tuple>
#include <functional>
#include <optional>

struct ListNode{
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}


  ListNode* apply(const std::function<void(ListNode *)> &func);

  static bool eq(const ListNode* a, const ListNode* b);
  static std::optional<ListNode *> index(ListNode *head, int idx);
  static ListNode* arrayToListNode(const std::vector<int> &arr);
  static std::vector<ListNode *> arraysToLinkedList(const std::vector<std::vector<int>> &arrList);
  static std::vector<int> listNodeToArray(ListNode *node);
};

#endif // LISTNODE_H