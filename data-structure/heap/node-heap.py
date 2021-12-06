from __future__ import annotations
from typing import List

# implement heap using node


class Node:
    _number: int
    _parent_node: Node
    _children_node: List[Node]

    def __init__(self, parent_node: Node, number: int) -> None:
        self._parent_node = parent_node
        self._number = number
        self._children_node = []

    def append_child_node(self, child_node: Node) -> None:
        if len(self._children_node) == 2:
            raise ValueError(
                f"this node has already {len(self._children_node)} nodes. can not append more child."
            )
        else:
            self._children_node.append(child_node)

    @property
    def parent_node(self) -> Node:
        return self._parent_node

    @property
    def children_node(self) -> List[Node]:
        return self._children_node

    @property
    def number(self) -> int:
        return self._number

    def __str__(self) -> str:
        if self.next_node:
            return (
                f"<Node number={self.number} children_node={len(self.children_node)}>"
            )
        else:
            return f"<Node number={self.number} children_node={0}>"


class Heap:
    """
    min heap

    TODO implement after implement DFS
    """

    root_node: Node
    height: int

    def __init__(self) -> None:
        self.root_node = None
        height = -1

    def get_last_node(self) -> Node:
        pass

    def heapify(self) -> None:
        pass

    def insert(self, number: int) -> None:
        if not self.root_node:
            self.root_node = Node(None, number)
            self.height += 1
        else:
            # parsing location using dfs
            pass

    def remove(self) -> None:
        if not self.root_node:
            raise AttributeError("heap has no node.")
        else:
            # pop root node

            pass
