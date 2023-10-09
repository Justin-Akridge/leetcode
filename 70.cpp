#include <iostream>
#include <cassert>

class Solution {
public:
  int climbStairs(int n) {
    :
  }
};

int main() {
  Solution s;
  assert(s.climbStairs(2) == 2);
  assert(s.climbStairs(3) == 3);
  assert(s.climbStairs(4) == 5);
  assert(s.climbStairs(5) == 8);
  assert(s.climbStairs(6) == 13);
}

// example:
//   3 steps:
//    1 1 1
//    1 2
//    2 1
//
//    4 steps:
//    1 1 1 1
//    1 1 2
//    1 2 1
//    2 1 1
//    2 2
//
//    5 step:
//    1 1 1 1 1
//    1 1 1 2
//    1 1 2 1
//    1 2 1 1
//    2 1 1 1
//    1 2 2 
//    2 1 2
//    2 2 1
//
//
//    6 steps:
//    1 1 1 1 1 1 
//    1 1 1 1 2
//    1 1 1 2 1
//    1 1 2 1 1
//    1 2 1 1 1
//    2 1 1 1 1
//    1 1 2 2 
//    1 2 2 1
//    1 2 1 2
//    2 2 1 1 
//    2 1 1 2
//    2 1 2 1
//    2 2 2
