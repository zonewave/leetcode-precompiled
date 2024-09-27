#include "ListNode.h"





bool ListNode::eq(const ListNode* a, const ListNode* b) {
    while (a != nullptr && b != nullptr) {
        if (a->val != b->val) {
            return false; // 值不相等
        }
        a = a->next; // 移动到下一个节点
        b = b->next;
    }
    return a == nullptr && b == nullptr; // 确保两个链表都结束
}

// Return the idx node of the linked list
std::optional<ListNode*> ListNode::index(ListNode* head, int idx) {
    if (idx < 0) return std::nullopt;

    ListNode* current = head;
    for (int i = 0; current != nullptr; i++) {
        if (i == idx) {
            return current;
        }
        current = current->next;
    }
    return std::nullopt;
}

// Apply function to the current node
ListNode* ListNode::apply(const std::function<void(ListNode*)>& func) {
    func(this);
    return this;
}

// Convert array to linked list node
ListNode* ListNode::arrayToListNode(const std::vector<int>& arr) {
    ListNode* head = nullptr;
    for (auto it = arr.rbegin(); it != arr.rend(); ++it) {
        ListNode* newNode = new ListNode(*it);
        newNode->next = head;
        head = newNode;
    }
    return head;
}

// Convert multiple arrays to linked list nodes
std::vector<ListNode*> ListNode::arraysToLinkedList(const std::vector<std::vector<int>>& arrList) {
    std::vector<ListNode*> result;
    for (const auto& arr : arrList) {
        result.push_back(arrayToListNode(arr));
    }
    return result;
}

// Convert linked list to array
std::vector<int> ListNode::listNodeToArray(ListNode* node) {
    std::vector<int> result;
    while (node) {
        result.push_back(node->val);
        node = node->next;
    }
    return result;
}