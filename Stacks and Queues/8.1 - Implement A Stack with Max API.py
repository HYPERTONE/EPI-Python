
# Stacks support last-in, first-out semantics for inserts and deletes, whereas queues are first-in, first-out. Stacks and
# queues are usually building blocks in a solution to a complex problem.

# A stack supports two basic operations - push and pop. Elements are added (pushed) and removed (popped) in last-in, 
# first-out order. If the stack is empty, pop typically returns null or throws an exception.


# 8.1 - Implement A Stack With Max API

# Design a stack that includes a max operation, in addition to push and pop. The max method should return the maximum
# value stored in the stack.

import collections

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(
                x, self.max())))
        
        
newStack = Stack()
newStack.push(1)
newStack.push(3)
newStack.push(9)
print(newStack.max())
print(newStack.pop())
print(newStack.max())
