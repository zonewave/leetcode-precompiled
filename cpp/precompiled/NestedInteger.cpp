#include "NestedInteger.h"
#include <stdexcept>

// Default constructor
NestedInteger::NestedInteger() : _hasInteger(false), _integer(0) {}

// Constructor with an integer value
NestedInteger::NestedInteger(int value) : _hasInteger(true), _integer(value) {}

// Check if this NestedInteger holds an integer
bool NestedInteger::isInteger() const {
    return _hasInteger;
}

// Get the integer value, assuming it's an integer
int NestedInteger::getInteger() const {
    if (!_hasInteger) {
        throw std::runtime_error("This NestedInteger does not hold an integer.");
    }
    return _integer;
}

// Get the list of NestedInteger
const vector<NestedInteger>& NestedInteger::getList() const {
    if (_hasInteger) {
        throw std::runtime_error("This NestedInteger holds an integer, not a list.");
    }
    return _list;
}

// Non-const version of getList
vector<NestedInteger>& NestedInteger::getList() {
    if (_hasInteger) {
        throw std::runtime_error("This NestedInteger holds an integer, not a list.");
    }
    return _list;
}

// Set the integer value
void NestedInteger::setInteger(int i) {
    _hasInteger = true;
    _integer = i;
    _list.clear(); // Clear the list if setting an integer
}

// Add a NestedInteger to the list
void NestedInteger::add(const NestedInteger &ni) {
    _hasInteger = false; // This NestedInteger is now a list
    _list.push_back(ni);
}