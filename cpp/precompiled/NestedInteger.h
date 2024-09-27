#ifndef NESTEDINTEGER_H
#define NESTEDINTEGER_H

#include <vector>
using std::vector;

class NestedInteger {
public:
  NestedInteger();
  NestedInteger(int value);
  bool isInteger() const;
  int getInteger() const;
  const vector<NestedInteger> &getList() const;
  // http://stackoverflow.com/a/123995/490463
  vector<NestedInteger> &getList();
  void setInteger(int i);
  void add(const NestedInteger &ni);
private:
  bool _hasInteger;
  int _integer;
  vector<NestedInteger> _list;
};

#endif