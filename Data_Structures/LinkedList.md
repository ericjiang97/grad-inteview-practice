# Linked Lists

```python
class Node:
    def __init__(value, next):
        self.value = value
        self.next = next # pointer to next node

class LinkedList:
    def __init__(value):
        self.node = Node(value, None)

```

- have a pointer pointed to the next node

| Operation | Best | Worst | Average |
| --------- | ---- | ----- | ------- |
| Insertion | O(1) | O(n)  | O(n)    |
| Deletion  | O(1) | O(n)  | O(n)    |
| Search    | O(1) | O(n)  | O(n)    |

- Insertion depends on where you insert it. For example if you insert at the beginning the complexity is `O(n)`.
